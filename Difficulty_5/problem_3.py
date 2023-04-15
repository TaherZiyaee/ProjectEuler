factors_list = list()


def factors(n):
    for i in range(2, (n + 1) // 2):
        if n % i == 0 and is_prime(i):
            yield i
    #         factors_list.append(i)
    # return factors_list


def is_prime(n):
    for i in range(2,(n+1)//2):
        if n%i==0:
            return False
    return True


# n=600851475143
n = 13195
# print(f"Factors of {n:,} are :\n{factors(n)}")
# print(f"Prime of factors of {n:,} are :\n{prime_factors(factors_list)}")

y=factors(n)
print(list(y))
