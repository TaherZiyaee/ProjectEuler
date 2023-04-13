# TODO: Even Fibonacci numbers

def memoize(func):
    memory = {}

    def wrapper_decorator(n):
        if n % 2 == 0:
            memory[n] = func(n)
            return memory[n]

    print(memory.values())
    return wrapper_decorator


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(10))
print()
