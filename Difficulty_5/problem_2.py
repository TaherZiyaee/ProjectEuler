# TODO: Even Fibonacci numbers
# Display all numbers and their sum
def even_fibo(n):
    a, b = 0, 1
    i = 1
    sum = 0
    while b < n:
        a, b = b, a + b
        if a % 2 == 0:
            print(f"\t\t{i}) {a:,}")
            sum += a
        else:
            print(f"{i}) {a:,}")
        i += 1
    return sum


n = 4000000
my_sum=even_fibo(n)
print("-" * 30)
print(f"fibo({n:,}): {my_sum}")
