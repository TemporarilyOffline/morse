# morse.py
Python program to translate text to audio morse code

`pip install pyaudio` (and its dependencies that it complains about)

`morse.py string to encode`

The program will then sit and wait as you try to type in what you heard

```
± ./morse.py this is a test
this is a test
Correct: this is a test
```

Edit the top of the program to set the morse code play back parameters.  You can effect the side tone, the WPM and the farnsworth spacing.

You can change the intra-letter spacing and the intra-word spacing.

If you're just learning morse code, try to keep the MORSE_UNIT at .1 (which feels like 20wpm to me) but increase the WORD_SPACE and LETTER_SPACE to give you some room to decode. (This is the farnsworth method)

```
MORSE_UNIT = .1
DIT = MORSE_UNIT
DAH = MORSE_UNIT*3
LETTER_SPACE = MORSE_UNIT*3
WORD_SPACE = MORSE_UNIT*7-LETTER_SPACE
TONE = 550
```

# words.py:
Pick words of MAX_LETTERS from bogwords.txt and play a random SET using morse.py to test your skills

edit words.py to change MAX_LETTERS and SET:

```
SET=3
MAX_LETTERS=4
```

```
± ./words.py
rump
Correct: rump
wont
Correct: wont
wish
Correct: wish
aver
Correct: aver
rood
Correct: rood
surf
Try Again: serf
tao
Correct: tao
take
Correct: take
have
Try Again: shin
hoae
Try Again: hone
mob
Try Again: job
mare
Correct: mare
face
Correct: face

Try Again: star
emit
Correct: emit
```

# attribution:

Waveform Generator taken from: https://stackoverflow.com/a/53231212/7503114 (Thanks!)
