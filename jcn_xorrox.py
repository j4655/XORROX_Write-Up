#!/usr/bin/env python3

import random

# I changed the name of the file to open so I could run the algorithm with a fake flag for testing.
with open("fakeflag.txt", "rb") as filp:
    # strip() removes leanding and trailing spaces in a string.
    flag = filp.read().strip()

# returns a random int for every character in the flag
key = [random.randint(1, 256) for _ in range(len(flag))]

# empty arrays to be filled
xorrox = []
enc = []

# i will contain the index of the current element,
# v will contain the value
for i, v in enumerate(key):

    # k is set to 1 to begin every iteration
    k = 1

    # Looping from the current value of i, decrementing until 0
    # This part doesn't run on the first iteration due to i being 0
    # The loop stops when i = 0, so the first key is not used in this loop
    for j in range(i, 0, -1):
        # x ^= 3 is the same as saying x = x ^ 3
        # ^ is the XOR operator, it sets each bit to 1 if only one of two bits is 1.
        k ^= key[j]

    # appends the k value to the first empty array
    # the first element of this array will always be set to 1 because the
    # internal loop doesn't run the first round.
    xorrox.append(k)

    # appends the result of the current flag character
    # XOR'd with the current value of the key array.
    enc.append(flag[i] ^ v)

# I changed the filename so I could differentiate between the
# test one and the original output file.
with open("jcn_output.txt", "w") as filp:
    # using f-strings to write output, aka "Literal String Interpolation"
    filp.write(f"{xorrox=}\n")
    filp.write(f"{enc=}\n")
    
    # I added this line while reverse engineering this algorithm, the key elements are different everytime but I could test
    # my decryption methods to make sure I was deriving the correct key values based on the given information
    #filp.write(f"{key=}\n")
