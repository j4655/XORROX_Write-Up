flag = [102]
key = [124]
enc=[26, 188, 220, 228, 144, 1, 36, 185, 214, 11, 25, 178, 145, 47, 237, 70, 244, 149, 
    98, 20, 46, 187, 207, 136, 154, 231, 131, 193, 84, 148, 212, 126, 126, 226, 211, 10, 20, 119]
xorrox=[1, 209, 108, 239, 4, 55, 34, 174, 79, 117, 8, 222, 123, 99, 184, 202, 95, 255,
    175, 138, 150, 28, 183, 6, 168, 43, 205, 105, 92, 250, 28, 80, 31, 201, 46, 20, 50, 56]
flagstring = 'f'

'''
 The second xorrox value is only the key value XOR'd with 1
 so the second key value is equal to xorrox[1] XOR 1
 I did this outside of the loop so that I could use less code
 inside the loop, since the first key value will not be used
 as an XOR operand.
'''
key.append(xorrox[1]^1)

n = 2

while n < len(xorrox):
    # here is why I did the first key append outside of this loop,
    # it would have referenced the first key value if n was equal to 1
    m = (xorrox[n]^key[n-1])
    
    # I stopped the range at 1 because we already solved
    # for that element.
    for i in range((n-1), 1, -1):
        # XOR m with every prior key value in descending order
        m = (m^key[i-1])
    
    # After the for loop,
    # XOR m with 1, this is the exact reverse order of the encryption.
    m = m^1
    
    # append the key value and increment the n value
    key.append(m)
    n += 1

# I print the key and enc values to the screen for testing
print(f"{key=}\n")
print(f"{enc=}\n")

'''
 I take each key value and XOR it against the corresponding enc value.
 This returns an integer value, which I append to a flag array.
 I then use the chr() method to append the unicode character value
 to a string.
'''
for m in range(1, len(key)):
    flag.append(key[m]^enc[m])
    flagstring += chr(flag[m])

# Printing the flag array values and the flag string.
print(f"{flag=}\n")
print(f"{flagstring=}\n")
