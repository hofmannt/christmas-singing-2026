import sys, os, subprocess
sys.path.insert(0, '.')
import numpy as np, mido, soundfile as sf
from parse import ALL

BPM = 72
SPB = 60 / BPM
FERMATA_STRETCH = 2.2
SF2 = '/usr/share/sounds/sf2/FluidR3_GM.sf2'
SR = 44100
LEAD_IN = 2.4 + 4 * SPB  # pitch pipe, pause, then 4 count-in clicks

# beats where a fermata holds (all voices share them)
ferm = sorted({s for p in ALL.values() for s, d, m, f, b in p if f})

def sec(beat):
    """Map score beat to seconds, stretching fermata beats."""
    t = beat * SPB
    for fb in ferm:
        if beat > fb:
            t += (min(beat, fb + 1) - fb) * SPB * (FERMATA_STRETCH - 1)
    return LEAD_IN + t

def write_midi(events, path, program):
    """events: list of (t_on, t_off, midi, vel). One channel."""
    mf = mido.MidiFile(ticks_per_beat=480)
    tr = mido.MidiTrack(); mf.tracks.append(tr)
    tr.append(mido.MetaMessage('set_tempo', tempo=500000))  # 120 bpm: 1 s = 960 ticks
    ch = 9 if program is None else 0
    if program is not None:
        tr.append(mido.Message('program_change', program=program, channel=ch))
        tr.append(mido.Message('control_change', control=91, value=40, channel=ch))  # reverb
    msgs = []
    for on, off, m, v in events:
        msgs.append((on, 1, mido.Message('note_on', note=m, velocity=v, channel=ch)))
        msgs.append((off, 0, mido.Message('note_off', note=m, velocity=0, channel=ch)))
    msgs.sort(key=lambda x: (x[0], x[1]))
    last = 0
    for t, _, msg in msgs:
        tick = int(round(t * 960))
        msg.time = tick - last; last = tick
        tr.append(msg)
    mf.save(path)

def render(mid, wav):
    subprocess.run(['fluidsynth', '-ni', '-g', '0.6', '-r', str(SR), '-F', wav, SF2, mid],
                   check=True, capture_output=True)
    x, _ = sf.read(wav, always_2d=True)
    return x

os.makedirs('stems', exist_ok=True)
stems = {}
for name, notes in ALL.items():
    ev = []
    for s, d, m, f, b in notes:
        if m is None: continue
        on, off = sec(s), sec(s + d)
        off = on + (off - on) * 0.94  # small gap so repeated notes re-sound
        ev.append((on, off, m, 96))
    write_midi(ev, f'stems/{name}.mid', 52)  # Choir Aahs
    stems[name] = render(f'stems/{name}.mid', f'stems/{name}.wav')

# lead-in: pitch pipe Ab4 (harmonica), then 4 soft clicks on the tempo
pipe = [(0.2, 1.6, 68, 90)]
write_midi(pipe, 'stems/pipe.mid', 22)
clicks = [(LEAD_IN - 4 * SPB + i * SPB, LEAD_IN - 4 * SPB + i * SPB + 0.1, 76 if i else 77, 70) for i in range(4)]
write_midi(clicks, 'stems/click.mid', None)
extra = {'pipe': render('stems/pipe.mid', 'stems/pipe.wav'),
         'click': render('stems/click.mid', 'stems/click.wav')}

L = max(len(x) for x in list(stems.values()) + list(extra.values()))
def pad(x): return np.pad(x, ((0, L - len(x)), (0, 0)))
stems = {k: pad(v) for k, v in stems.items()}
extra = {k: pad(v) for k, v in extra.items()}

def mix(gains, out):
    y = sum(stems[k] * g for k, g in gains.items()) + extra['pipe'] * 0.8 + extra['click'] * 0.5
    y = y / np.max(np.abs(y)) * 0.89
    sf.write(out + '.wav', y, SR)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', out + '.wav', '-b:a', '192k', out + '.mp3'], check=True)
    os.remove(out + '.wav')

os.makedirs('out', exist_ok=True)
parts = ['Tenor', 'Lead', 'Baritone', 'Bass']
mix({p: 1.0 for p in parts}, 'out/Aura_Lee_all_parts')
for p in parts:
    mix({q: (1.0 if q == p else 0.28) for q in parts}, f'out/Aura_Lee_{p}_loud')
for p in ['Baritone', 'Bass']:
    mix({q: (0.0 if q == p else 1.0) for q in parts}, f'out/Aura_Lee_{p}_missing_singalong')
print(sorted(os.listdir('out')))
