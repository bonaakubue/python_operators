#arithmetic operator precedence

result = 2 + 2 - 2
print(result)

result = 2 + (2 - 2)
print(result)

result = 2 * 2 - 2
print(result)

#evaluates by precedence
result = 2 + 2 - 2 * 2 / 2 ** 2 % 2
print(result)

#using parenthesis to confirm precedence
result = 2 + 2 - ((2 * (2 / (2 ** 2))) % 2)
print(result)

#using parenthesis to evaluate from right
result = (2 + (2 - (2 * (2 / (2 ** (2 % 2))))))
print(result)

#using parenthesis to evaluate from left
result = ((((((2 + 2) - 2) * 2) / 2) ** 2) % 2)
print(result)


