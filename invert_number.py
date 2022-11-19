# How to invert any number

original = int(input('Input a number: '))
inverted = 0
while original != 0:
    inverted = inverted * 10 + original % 10
    original //= 10
print(inverted)