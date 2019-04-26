#!/usr/bin/env python3
import pyaudio
import struct
import math
import time
import sys

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

"""
20 wpm seems to be about
MORSE_UNIT = .1
DIT = MORSE_UNIT
DAH = MORSE_UNIT*3
LETTER_SPACE = MORSE_UNIT*3
WORD_SPACE = MORSE_UNIT*7
"""
MORSE_UNIT = .1
DIT = MORSE_UNIT
DAH = MORSE_UNIT*3
LETTER_SPACE = MORSE_UNIT*14
WORD_SPACE = LETTER_SPACE*2

TONE = 550

p = pyaudio.PyAudio()

# we are going to be playing a lot of streams, open globally
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

def data_for_freq(frequency: float, time: float = None):
    """
    get frames for a fixed frequency for a specified time or
    number of frames, if frame_count is specified, the specified
    time is ignored
    """
    frame_count = int(RATE * time)

    remainder_frames = frame_count % RATE
    wavedata = []

    for i in range(frame_count):
        a = RATE / frequency  # number of frames per wave
        b = i / a
        # explanation for b
        # considering one wave, what part of the wave should this be
        # if we graph the sine wave in a
        # displacement vs i graph for the particle
        # where 0 is the beginning of the sine wave and
        # 1 the end of the sine wave
        # which part is "i" is denoted by b
        # for clarity you might use
        # though this is redundant since math.sin is a looping function
        # b = b - int(b)

        c = b * (2 * math.pi)
        # explanation for c
        # now we map b to between 0 and 2*math.PI
        # since 0 - 2*PI, 2*PI - 4*PI, ...
        # are the repeating domains of the sin wave (so the decimal values will
        # also be mapped accordingly,
        # and the integral values will be multiplied
        # by 2*PI and since sin(n*2*PI) is zero where n is an integer)
        d = math.sin(c) * 32767
        e = int(d)
        wavedata.append(e)

    for i in range(remainder_frames):
        wavedata.append(0)

    number_of_bytes = str(len(wavedata))  
    wavedata = struct.pack(number_of_bytes + 'h', *wavedata)

    return wavedata


def play(frequency: float, time: float):
    # play a frequency for a fixed time!
    frames = data_for_freq(frequency, time)
    stream.write(frames)


def morse_translate(phrase):
    # take incoming string and play it back as morse code
    morsetab = {
            'A': '.-',              'a': '.-',
            'B': '-...',            'b': '-...',
            'C': '-.-.',            'c': '-.-.',
            'D': '-..',             'd': '-..',
            'E': '.',               'e': '.',
            'F': '..-.',            'f': '..-.',
            'G': '--.',             'g': '--.',
            'H': '....',            'h': '....',
            'I': '..',              'i': '..',
            'J': '.---',            'j': '.---',
            'K': '-.-',             'k': '-.-',
            'L': '.-..',            'l': '.-..',
            'M': '--',              'm': '--',
            'N': '-.',              'n': '-.',
            'O': '---',             'o': '---',
            'P': '.--.',            'p': '.--.',
            'Q': '--.-',            'q': '--.-',
            'R': '.-.',             'r': '.-.',
            'S': '...',             's': '...',
            'T': '-',               't': '-',
            'U': '..-',             'u': '..-',
            'V': '...-',            'v': '...-',
            'W': '.--',             'w': '.--',
            'X': '-..-',            'x': '-..-',
            'Y': '-.--',            'y': '-.--',
            'Z': '--..',            'z': '--..',
            '0': '-----',           ',': '--..--',
            '1': '.----',           '.': '.-.-.-',
            '2': '..---',           '?': '..--..',
            '3': '...--',           ';': '-.-.-.',
            '4': '....-',           ':': '---...',
            '5': '.....',           "'": '.----.',
            '6': '-....',           '-': '-....-',
            '7': '--...',           '/': '-..-.',
            '8': '---..',           '(': '-.--.-',
            '9': '----.',           ')': '-.--.-',
            ' ': ' ',               '_': '..--.-',
    }
    
    # walk through string one letter at a time and play back the sound accordingly
    for c in range(len(phrase)):
      # print letter on screen
      # print (phrase[c], end='', flush=True)
      # lookup morse code of letter
      morse_code = (morsetab[phrase[c]])
      # play sound of letter
      for s in range(len(morse_code)):
        if morse_code[s] == '.':
          play(TONE, DIT)
        if morse_code[s] == '-':
          play(TONE, DAH)
        if morse_code[s] == ' ':
          time.sleep(WORD_SPACE-LETTER_SPACE)
      #don't play letter space until after the letter is played all the way through
      time.sleep(LETTER_SPACE) 
    
if __name__ == "__main__":

    # remove command name leaving words:
    str(sys.argv.pop(0))
    cli = " ".join(sys.argv)
    #print (cli)
    morse_translate(cli)
    answer = input()
    if answer == cli:
      print(f'Correct: {cli}')
    else:
      print(f'Try Again: {cli}')

#close global stream
stream.stop_stream()
stream.close()