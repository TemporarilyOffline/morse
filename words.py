#!/usr/bin/env python3

import random
import subprocess

# open the OSPD4_stripped.txt file and grab 
# a random set of SET words, made up of no 
# more than MAX_LETTERS

SET=25
MAX_LETTERS=4
#MAX_LETTERS += 1
RESULTS = []

#f = open("OSPD4_stripped.txt")
f = open("bogwords.txt")

for line in f:
  if len(line.strip()) <= MAX_LETTERS:
    RESULTS.append(line.strip())
    
random.shuffle(RESULTS)
#print("\n".join(RESULTS[len(RESULTS)-SET:]))

for word in RESULTS:
  subprocess.run(["./morse.py", word])

f.close()