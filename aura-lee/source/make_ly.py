import sys
sys.path.insert(0, '.')
from song import PARTS, LYRICS

def music(name):
    bars = list(PARTS[name])
    if name == 'Bass':  # optional upper octave on the low Eb, as in the original
        bars[30] = "bes,4 bes, ees <ees, \\parenthesize ees>"
    out = []
    for i, b in enumerate(bars, 1):
        if i == 1:
            b = '\\mark \\markup \\smallCaps "Chorus 1" ' + b
        if i == 17:
            b = '\\mark \\markup \\smallCaps "Chorus 2" ' + b
        bl = {8: ' \\bar "||"', 16: ' \\bar "||"', 24: ' \\bar "||"', 32: ' \\bar "|."'}.get(i, '')
        out.append(f"  {b} |{bl} % {i}")
    return "\n".join(out)

STAVES = [("Tenor", "tenor", "treble", "Tenor", "(woman)"),
          ("Lead", "lead", "treble", "Lead", "(woman, melody)"),
          ("Baritone", "bari", "bass", "Baritone", "(man)"),
          ("Bass", "bass", "bass", "Bass", "(man)")]

ly = [r'''\version "2.24.0"
\paper { #(set-paper-size "a4") top-margin = 12 bottom-margin = 12 left-margin = 16 right-margin = 14
  system-system-spacing.basic-distance = #16 markup-system-spacing.basic-distance = #8 }
\header {
  title = "Aura Lee"
  subtitle = "Barbershop quartet, set for two women and two men"
  poet = "Words: W. W. Fosdick"
  composer = "Music: George R. Poulton (1861)"
  arranger = "Arr. SPEBSQSA (1973); women sing tenor and lead an octave up"
  tagline = ##f
}
global = { \key aes \major \time 4/4 \tempo "Gently" 4 = 72 }
words = \lyricmode { ''' + LYRICS + r''' }
''']
for name, var, clef, inst, sub in STAVES:
    ly.append(f"{var} = {{ \\global \\clef {clef}\n{music(name)}\n}}")
ly.append(r'''\score {
  \new ChoirStaff <<''')
for name, var, clef, inst, sub in STAVES:
    ly.append(f'''    \\new Staff \\with {{ instrumentName = \\markup \\center-column {{ "{inst}" \\small "{sub}" }} shortInstrumentName = "{ {"Tenor":"Ten.","Lead":"Lead","Baritone":"Bari","Bass":"Bass"}[inst] }" }}
      {{ \\new Voice = "{var}" \\{var} }}
    \\new Lyrics \\lyricsto "{var}" \\words''')
ly.append(r'''  >>
  \layout { \context { \Score \accidentalStyle modern-cautionary \override BarNumber.break-visibility = ##(#f #t #t) } indent = 22 short-indent = 8 }
}''')
open('aura_lee_mixed.ly', 'w').write("\n".join(ly))
