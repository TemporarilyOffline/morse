#!/usr/bin/env python3

import random
import subprocess

# open the bogwords.txt file and grab 
# a random set of SET words, made up of no 
# more than MAX_LETTERS

SET=3
MAX_LETTERS=4
RESULTS = []

f = open("bogwords.txt")

for line in f:
  if len(line.strip()) <= MAX_LETTERS:
    RESULTS.append(line.strip())
    
random.shuffle(RESULTS)
TEST_SET = RESULTS[len(RESULTS)-SET:]
for word in TEST_SET:
  subprocess.run(["./morse.py", word])

f.close()