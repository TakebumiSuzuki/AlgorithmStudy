def power(base, exponent):
    if exponent == 0: return 1
    if exponent == 1: return base #この行はなくてもよい
    return base * power(base, exponent - 1)

print(power(2, 0))