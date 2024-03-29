
```
$ unicodehaz --help
Usage: unicodehaz [OPTIONS] [CODEPOINTS]...

Options:
  --all            Include unnamed codepoints in output
  --null           NULL terminalted output
  --glyphs-only    Do not print index numbers
  --stats          Only print statistics
  --start INTEGER
  --stop INTEGER
  --utf8           CODEPOINTS are utf8 instead of int
  --help           Show this message and exit.


$ unicodehaz | grep -i snowman
9731 '☃' SNOWMAN
9924 '⛄' SNOWMAN WITHOUT SNOW
9927 '⛇' BLACK SNOWMAN

$ unicodehaz | grep ☃
9731 '☃' SNOWMAN

$ unicodehaz ☃ --utf8
9731 '☃' SNOWMAN

$ echo '๏☃' | unicodehaz --utf8
3663 '๏' THAI CHARACTER FONGMAN
9731 '☃' SNOWMAN

$ unicodehaz --all | wc -l
1114112

$ unicodehaz | wc -l
131808

$ unicodehaz | grep -i superscript
178 '²' SUPERSCRIPT TWO
179 '³' SUPERSCRIPT THREE
185 '¹' SUPERSCRIPT ONE
1648 'ٰ' ARABIC LETTER SUPERSCRIPT ALEF
1809 'ܑ' SYRIAC LETTER SUPERSCRIPT ALAPH
8304 '⁰' SUPERSCRIPT ZERO
8305 'ⁱ' SUPERSCRIPT LATIN SMALL LETTER I
8308 '⁴' SUPERSCRIPT FOUR
8309 '⁵' SUPERSCRIPT FIVE
8310 '⁶' SUPERSCRIPT SIX
8311 '⁷' SUPERSCRIPT SEVEN
8312 '⁸' SUPERSCRIPT EIGHT
8313 '⁹' SUPERSCRIPT NINE
8314 '⁺' SUPERSCRIPT PLUS SIGN
8315 '⁻' SUPERSCRIPT MINUS
8316 '⁼' SUPERSCRIPT EQUALS SIGN
8317 '⁽' SUPERSCRIPT LEFT PARENTHESIS
8318 '⁾' SUPERSCRIPT RIGHT PARENTHESIS
8319 'ⁿ' SUPERSCRIPT LATIN SMALL LETTER N
64603 'ﱛ' ARABIC LIGATURE THAL WITH SUPERSCRIPT ALEF ISOLATED FORM
64604 'ﱜ' ARABIC LIGATURE REH WITH SUPERSCRIPT ALEF ISOLATED FORM
64605 'ﱝ' ARABIC LIGATURE ALEF MAKSURA WITH SUPERSCRIPT ALEF ISOLATED FORM
64611 'ﱣ' ARABIC LIGATURE SHADDA WITH SUPERSCRIPT ALEF ISOLATED FORM
64656 'ﲐ' ARABIC LIGATURE ALEF MAKSURA WITH SUPERSCRIPT ALEF FINAL FORM
64729 'ﳙ' ARABIC LIGATURE HEH WITH SUPERSCRIPT ALEF INITIAL FORM

$ unicodehaz | grep -i "modifier letter capital"
7468 'ᴬ' MODIFIER LETTER CAPITAL A
7469 'ᴭ' MODIFIER LETTER CAPITAL AE
7470 'ᴮ' MODIFIER LETTER CAPITAL B
7471 'ᴯ' MODIFIER LETTER CAPITAL BARRED B
7472 'ᴰ' MODIFIER LETTER CAPITAL D
7473 'ᴱ' MODIFIER LETTER CAPITAL E
7474 'ᴲ' MODIFIER LETTER CAPITAL REVERSED E
7475 'ᴳ' MODIFIER LETTER CAPITAL G
7476 'ᴴ' MODIFIER LETTER CAPITAL H
7477 'ᴵ' MODIFIER LETTER CAPITAL I
7478 'ᴶ' MODIFIER LETTER CAPITAL J
7479 'ᴷ' MODIFIER LETTER CAPITAL K
7480 'ᴸ' MODIFIER LETTER CAPITAL L
7481 'ᴹ' MODIFIER LETTER CAPITAL M
7482 'ᴺ' MODIFIER LETTER CAPITAL N
7483 'ᴻ' MODIFIER LETTER CAPITAL REVERSED N
7484 'ᴼ' MODIFIER LETTER CAPITAL O
7485 'ᴽ' MODIFIER LETTER CAPITAL OU
7486 'ᴾ' MODIFIER LETTER CAPITAL P
7487 'ᴿ' MODIFIER LETTER CAPITAL R
7488 'ᵀ' MODIFIER LETTER CAPITAL T
7489 'ᵁ' MODIFIER LETTER CAPITAL U
7490 'ᵂ' MODIFIER LETTER CAPITAL W
11389 'ⱽ' MODIFIER LETTER CAPITAL V
43000 'ꟸ' MODIFIER LETTER CAPITAL H WITH STROKE

$ unicodehaz --stats
last named unicode char: 917999 '󠇯' VARIATION SELECTOR-256
unnamed codepoints: 982304

```

Wishlist: superscript uppercase (aka "MODIFIER LETTER CAPITAL") C F Q S X Y and Z.

Related:

https://qntm.org/safe
