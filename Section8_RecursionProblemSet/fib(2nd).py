def fib(num):
    if num <= 0: return None
    if num == 1 or num == 2: return 1 
    
    return fib(num - 2) + fib(num - 1)

print(fib(6))