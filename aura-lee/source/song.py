# Aura Lee, SPEBSQSA 1973 TTBB arrangement, transcribed bar by bar.
# Pitches in LilyPond absolute notation, at the pitch sung in the MIXED version:
# tenor and lead (women) one octave above the TTBB sounding pitch, i.e. as written
# in the original treble-8 clef; baritone and bass (men) as written.

TEN = {
 1: "c''4 c'' des'' c''", 2: "d''4 d'' d''2", 3: "des''4 des'' d'' des''",
 4: "c''2( des'')", 8: "c''2. r4",
 9: "ees''4. ees''8 e''2", 10: "f''4 f'' ges''2", 11: "f''4 f'' f'' f''",
 12: "e''1", 13: "ees''4 ees'' f''4. ees''8", 14: "d''4 d'' d''4\\fermata d''",
 15: "des''4 des'' ees'' des''", 16: "c''2. r4",
 'x': "d''4 d'' d'' d''",
 31: "des''4 des'' c'' bes''", 32: "aes''2. r4",
}
LEAD = {
 1: "ees'4 aes' g' aes'", 2: "bes'4 f' bes'2", 3: "aes'4 g' f' g'",
 4: "aes'2( ees')", 8: "aes'2. r4",
 9: "c''4. c''8 c''2", 10: "c''4 c'' c''2", 11: "c''4 bes' aes' bes'",
 12: "c''1", 13: "c''4 c'' des''4. c''8", 14: "bes'4 f' bes'4\\fermata aes'",
 15: "aes'4 g' c'' bes'", 16: "aes'2. r4",
 'x': "bes'4 f' bes' bes'",
 31: "aes'4 g' ees'' des''", 32: "c''2. r4",
}
BARI = {
 1: "aes4 ees ees ees", 2: "aes4 aes aes2", 3: "bes4 bes aes bes",
 4: "ees2( g)", 8: "ees2. r4",
 9: "aes4. aes8 bes2", 10: "aes4 aes aes2", 11: "aes4 aes des' g",
 12: "g2( bes)", 13: "a4 a a4. a8", 14: "aes4 aes aes4\\fermata f",
 15: "fes4 ees g g", 16: "ees2. r4",
 'x': "aes4 aes aes aes",
 31: "fes4 ees g g", 32: "ees2. r4",
}
BASS = {
 1: "aes,4 aes, bes, aes,", 2: "f4 bes, f2", 3: "fes4 ees bes, ees",
 4: "aes,2( bes,)", 8: "aes,2. r4",
 9: "aes,4. aes8 g2", 10: "f4 f ees2", 11: "des4 des des des",
 12: "c2( g)", 13: "f4 f f4. f8", 14: "f4 bes, f4\\fermata bes,",
 15: "bes,4 bes, ees ees", 16: "aes,2. r4",
 'x': "f4 bes, f f",
 31: "bes,4 bes, ees ees,", 32: "aes,2. r4",
}
# repeats: 5-7 = 1-3, 17-24 = 1-8, 25-30 = 9-14
def full(d):
    out = dict(d)
    for b in (5, 6, 7): out[b] = d[b - 4]
    for b in range(17, 25): out[b] = out[b - 16]
    for b in range(25, 31): out[b] = d[b - 16]
    for b in (18, 22): out[b] = d.get('x', out[b])  # 4 quarters in chorus 2
    return [out[b] for b in range(1, 33)]

PARTS = {"Tenor": full(TEN), "Lead": full(LEAD), "Baritone": full(BARI), "Bass": full(BASS)}

LYR1 = ("As the black -- bird in the spring, 'neath the wil -- low tree __ "
        "sat and piped, I heard him sing, sing of Au -- ra Lee. "
        "Au -- ra Lee, Au -- ra Lee, maid of gold -- en hair, "
        "Sun -- shine came a -- long with thee, and swal -- lows in the air. ")
LYR2 = ("On her cheek the rose was born, 'twas mu -- sic when she spake. __ "
        "In her eyes the rays of morn with sud -- den splen -- dor break. "
        "Au -- ra Lee, Au -- ra Lee, maid of gold -- en hair, "
        "Sun -- shine came a -- long with thee, and swal -- lows in the air.")
LYRICS = LYR1 + LYR2
