factors_list = list()


def factors(n):
    for i in range(1, (n + 1) // 2):
        if n % i == 0:
            factors_list.append(i)
    return factors_list


def prime_factors(lst):
    prime_list = list()
    flag = True
    for item in lst:
        if flag:
            prime_list.append(item)
        flag = True
        for j in range(2, (item + 1) // 2):
            if item % j == 0:
                flag = False
                break
    return prime_list


# n=600851475143
n = 13195
print(f"Factors of {n:,} are :\n{factors(n)}")
print(f"Prime of factors of {n:,} are :\n{prime_factors(factors(n))}")
