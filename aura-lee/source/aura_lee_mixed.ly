\version "2.24.0"
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
words = \lyricmode { As the black -- bird in the spring, 'neath the wil -- low tree __ sat and piped, I heard him sing, sing of Au -- ra Lee. Au -- ra Lee, Au -- ra Lee, maid of gold -- en hair, Sun -- shine came a -- long with thee, and swal -- lows in the air. On her cheek the rose was born, 'twas mu -- sic when she spake. __ In her eyes the rays of morn with sud -- den splen -- dor break. Au -- ra Lee, Au -- ra Lee, maid of gold -- en hair, Sun -- shine came a -- long with thee, and swal -- lows in the air. }

tenor = { \global \clef treble
  \mark \markup \smallCaps "Chorus 1" c''4 c'' des'' c'' | % 1
  d''4 d'' d''2 | % 2
  des''4 des'' d'' des'' | % 3
  c''2( des'') | % 4
  c''4 c'' des'' c'' | % 5
  d''4 d'' d''2 | % 6
  des''4 des'' d'' des'' | % 7
  c''2. r4 | \bar "||" % 8
  ees''4. ees''8 e''2 | % 9
  f''4 f'' ges''2 | % 10
  f''4 f'' f'' f'' | % 11
  e''1 | % 12
  ees''4 ees'' f''4. ees''8 | % 13
  d''4 d'' d''4\fermata d'' | % 14
  des''4 des'' ees'' des'' | % 15
  c''2. r4 | \bar "||" % 16
  \mark \markup \smallCaps "Chorus 2" c''4 c'' des'' c'' | % 17
  d''4 d'' d'' d'' | % 18
  des''4 des'' d'' des'' | % 19
  c''2( des'') | % 20
  c''4 c'' des'' c'' | % 21
  d''4 d'' d'' d'' | % 22
  des''4 des'' d'' des'' | % 23
  c''2. r4 | \bar "||" % 24
  ees''4. ees''8 e''2 | % 25
  f''4 f'' ges''2 | % 26
  f''4 f'' f'' f'' | % 27
  e''1 | % 28
  ees''4 ees'' f''4. ees''8 | % 29
  d''4 d'' d''4\fermata d'' | % 30
  des''4 des'' c'' bes'' | % 31
  aes''2. r4 | \bar "|." % 32
}
lead = { \global \clef treble
  \mark \markup \smallCaps "Chorus 1" ees'4 aes' g' aes' | % 1
  bes'4 f' bes'2 | % 2
  aes'4 g' f' g' | % 3
  aes'2( ees') | % 4
  ees'4 aes' g' aes' | % 5
  bes'4 f' bes'2 | % 6
  aes'4 g' f' g' | % 7
  aes'2. r4 | \bar "||" % 8
  c''4. c''8 c''2 | % 9
  c''4 c'' c''2 | % 10
  c''4 bes' aes' bes' | % 11
  c''1 | % 12
  c''4 c'' des''4. c''8 | % 13
  bes'4 f' bes'4\fermata aes' | % 14
  aes'4 g' c'' bes' | % 15
  aes'2. r4 | \bar "||" % 16
  \mark \markup \smallCaps "Chorus 2" ees'4 aes' g' aes' | % 17
  bes'4 f' bes' bes' | % 18
  aes'4 g' f' g' | % 19
  aes'2( ees') | % 20
  ees'4 aes' g' aes' | % 21
  bes'4 f' bes' bes' | % 22
  aes'4 g' f' g' | % 23
  aes'2. r4 | \bar "||" % 24
  c''4. c''8 c''2 | % 25
  c''4 c'' c''2 | % 26
  c''4 bes' aes' bes' | % 27
  c''1 | % 28
  c''4 c'' des''4. c''8 | % 29
  bes'4 f' bes'4\fermata aes' | % 30
  aes'4 g' ees'' des'' | % 31
  c''2. r4 | \bar "|." % 32
}
bari = { \global \clef bass
  \mark \markup \smallCaps "Chorus 1" aes4 ees ees ees | % 1
  aes4 aes aes2 | % 2
  bes4 bes aes bes | % 3
  ees2( g) | % 4
  aes4 ees ees ees | % 5
  aes4 aes aes2 | % 6
  bes4 bes aes bes | % 7
  ees2. r4 | \bar "||" % 8
  aes4. aes8 bes2 | % 9
  aes4 aes aes2 | % 10
  aes4 aes des' g | % 11
  g2( bes) | % 12
  a4 a a4. a8 | % 13
  aes4 aes aes4\fermata f | % 14
  fes4 ees g g | % 15
  ees2. r4 | \bar "||" % 16
  \mark \markup \smallCaps "Chorus 2" aes4 ees ees ees | % 17
  aes4 aes aes aes | % 18
  bes4 bes aes bes | % 19
  ees2( g) | % 20
  aes4 ees ees ees | % 21
  aes4 aes aes aes | % 22
  bes4 bes aes bes | % 23
  ees2. r4 | \bar "||" % 24
  aes4. aes8 bes2 | % 25
  aes4 aes aes2 | % 26
  aes4 aes des' g | % 27
  g2( bes) | % 28
  a4 a a4. a8 | % 29
  aes4 aes aes4\fermata f | % 30
  fes4 ees g g | % 31
  ees2. r4 | \bar "|." % 32
}
bass = { \global \clef bass
  \mark \markup \smallCaps "Chorus 1" aes,4 aes, bes, aes, | % 1
  f4 bes, f2 | % 2
  fes4 ees bes, ees | % 3
  aes,2( bes,) | % 4
  aes,4 aes, bes, aes, | % 5
  f4 bes, f2 | % 6
  fes4 ees bes, ees | % 7
  aes,2. r4 | \bar "||" % 8
  aes,4. aes8 g2 | % 9
  f4 f ees2 | % 10
  des4 des des des | % 11
  c2( g) | % 12
  f4 f f4. f8 | % 13
  f4 bes, f4\fermata bes, | % 14
  bes,4 bes, ees ees | % 15
  aes,2. r4 | \bar "||" % 16
  \mark \markup \smallCaps "Chorus 2" aes,4 aes, bes, aes, | % 17
  f4 bes, f f | % 18
  fes4 ees bes, ees | % 19
  aes,2( bes,) | % 20
  aes,4 aes, bes, aes, | % 21
  f4 bes, f f | % 22
  fes4 ees bes, ees | % 23
  aes,2. r4 | \bar "||" % 24
  aes,4. aes8 g2 | % 25
  f4 f ees2 | % 26
  des4 des des des | % 27
  c2( g) | % 28
  f4 f f4. f8 | % 29
  f4 bes, f4\fermata bes, | % 30
  bes,4 bes, ees <ees, \parenthesize ees> | % 31
  aes,2. r4 | \bar "|." % 32
}
\score {
  \new ChoirStaff <<
    \new Staff \with { instrumentName = \markup \center-column { "Tenor" \small "(woman)" } shortInstrumentName = "Ten." }
      { \new Voice = "tenor" \tenor }
    \new Lyrics \lyricsto "tenor" \words
    \new Staff \with { instrumentName = \markup \center-column { "Lead" \small "(woman, melody)" } shortInstrumentName = "Lead" }
      { \new Voice = "lead" \lead }
    \new Lyrics \lyricsto "lead" \words
    \new Staff \with { instrumentName = \markup \center-column { "Baritone" \small "(man)" } shortInstrumentName = "Bari" }
      { \new Voice = "bari" \bari }
    \new Lyrics \lyricsto "bari" \words
    \new Staff \with { instrumentName = \markup \center-column { "Bass" \small "(man)" } shortInstrumentName = "Bass" }
      { \new Voice = "bass" \bass }
    \new Lyrics \lyricsto "bass" \words
  >>
  \layout { \context { \Score \accidentalStyle modern-cautionary \override BarNumber.break-visibility = ##(#f #t #t) } indent = 22 short-indent = 8 }
}