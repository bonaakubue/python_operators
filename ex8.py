#bitwise operators - ex8.py

#bitwise and

num1 = 0b10001
num2 = 0b11111

result = bin(num1 & num2)
print(result)

#bitwise or

result = bin(num1 | num2)
print(result)

#bitwise xor
result = bin(num1 ^ num2)
print(result)

#bitwise not
result = bin(~num1)
print(result)

result = bin(~num2)
print(result)

#bitwise left shift
result = bin(num1 << 1)
print(result)
result = bin(num1 << 2)
print(result)
result = bin(num1 << 3)
print(result)

#bitwise right shift
result = bin(num1 >> 1)
print(result)
result = bin(num1 >> 2)
print(result)
result = bin(num1 >> 3)
print(result)


