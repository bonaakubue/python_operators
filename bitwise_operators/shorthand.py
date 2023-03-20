#shorthands for bitwise operators

#bitwise and operator
num = 0b1110
num &= 0b1011
print(bin(num))

#bitwise or operator
num = 0b1110
num |= 0b1011
print(bin(num))

#bitwise xor operator
num = 0b1110
num &= 0b1011
print(bin(num))

#bitwise leftshift operator
num = 0b1110
num <<= 1
print(bin(num))

#bitwise rightshift operator
num = 0b1110
num >>= 1
print(bin(num))