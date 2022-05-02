#!/usr/bin/env python3
# THIS IS THE ORIGINAL PYTHON SCRIPT THAT WAS GIVEN FOR THE XORROX CHALLENGE AT NAHAMCON 2022
# THE ONLY ALTERATIONS MADE TO THIS FILE ARE COMMENTS ADDED FOR CLARITY.

import random

with open("flag.txt", "rb") as filp:
    # strip() removes leanding and trailing spaces in a string.
    flag = filp.read().strip()

# returns a random int for every character in the flag
key = [random.randint(1, 256) for _ in range(len(flag))]

# empty arrays to be filled
xorrox = []
enc = []

# I believe that i will contain the index of the current element,
# v should contain the value
for i, v in enumerate(key):
    # k is set to 1 to begin every iteration
    k = 1

    # Looping from the current value of i, decrementing until 0 (including 0 I believe)
    for j in range(i, 0, -1):

        # x ^= 3 is the same as saying x = x ^ 3
        # ^ is the XOR operator, it sets each bit to 1 if only one of two bits is 1.
        k ^= key[j]

    # appends the k value to the first empty array
    xorrox.append(k)

    # appends the result of the current flag character (should go in order)
    # XOR'd with the current value of the key array.
    enc.append(flag[i] ^ v)

with open("output.txt", "w") as filp:
    # using f-strings to write output, aka "Literal String Interpolation"
    filp.write(f"{xorrox=}\n")
    filp.write(f"{enc=}\n")
