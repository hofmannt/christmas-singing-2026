import re
from song import PARTS

STEP = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}
ACC = {'': 0, 'es': -1, 'is': 1, 'eses': -2, 'isis': 2}
TOK = re.compile(r"([a-gr])(eses|isis|es|is|s)?([',]*)(\d+)?(\.)?(\\fermata)?")


def parse_part(bars):
    """Return list of notes: (start_beat, dur_beats, midi or None, fermata, bar)."""
    notes, t, dur = [], 0.0, 1.0
    for bi, bar in enumerate(bars, 1):
        bar_start = t
        for tok in bar.replace('(', ' ').replace(')', ' ').split():
            m = TOK.fullmatch(tok)
            if not m:
                raise ValueError(f"bad token {tok!r} in bar {bi}")
            n, acc, octs, d, dot, ferm = m.groups()
            if d:
                dur = 4 / int(d) * (1.5 if dot else 1)
            if n == 'r':
                midi = None
            else:
                acc = acc or ''
                if n in 'ae' and acc == 's':
                    acc = 'es'
                midi = 48 + STEP[n] + ACC[acc] + 12 * (octs.count("'") - octs.count(','))
            notes.append((t, dur, midi, bool(ferm), bi))
            t += dur
        assert abs(t - bar_start - 4) < 1e-6, f"bar {bi} has {t - bar_start} beats"
    return notes


ALL = {k: parse_part(v) for k, v in PARTS.items()}
