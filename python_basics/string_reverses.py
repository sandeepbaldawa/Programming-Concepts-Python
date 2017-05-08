Reverse just each word contents in a string
============================================
str
'I am sandeep'

" ".join([each[::-1] for each in str.split(" ")])
'I ma peednas'

Reverse just each word contents and word order in a string
==========================================================
" ".join([each[::-1] for each in reversed(str.split(" "))])
'peednas ma I'

Reverse just word order
==========================================================
" ".join([each for each in reversed(str.split(" "))])
'sandeep am I'

