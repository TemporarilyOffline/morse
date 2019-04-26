# morse.py
Python program to translate text to audio morse code

`pip install pyaudio` (and its dependencies that it complains about)

`morse.py string to encode`

Edit the top of the program to set the morse code play back parameters.  You can effect the side tone, the WPM and the farnsworth spacing.

You can change the intra-letter spacing and the intra-word spacing.

If you're just learning morse code, try to keep the MORSE_UNIT at .1 (which feels like 20wpm to me) but increase the WORD_SPACE and LETTER_SPACE to give you some room to decode. (This is the farnsworth method)

```
MORSE_UNIT = .1

DIT = MORSE_UNIT
DAH = MORSE_UNIT*3
LETTER_SPACE = MORSE_UNIT*3
# later in the program we have an if block that would pause for WORD_SPACE and LETTER_SPACE
# remove LETTER_SPACE here
WORD_SPACE = MORSE_UNIT*7-LETTER_SPACE

TONE = 550
```

# goals:
Pick a target word size and play a random 25 words from the OSPD4 (included).  
Allow for some user interaction to advance to the next word
Allow for some user interaction to type in the word heard
Report the results 

# attribution:

Waveform Generator taken from: https://stackoverflow.com/a/53231212/7503114 (Thanks!)
