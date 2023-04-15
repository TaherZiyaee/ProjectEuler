prime_list=list()
def factors(n):
    for i in range(1,(n+1)//2):
        if n%i==0:
            prime_list.append(i)
    return prime_list

def prime_factors(lst):
    for item in lst:
        for j in range(2,(item+1)//2):
            if item%j==0:
                break
            else:

# n=600851475143
n=13195
print(f"Prime factors of {n:,} are :\n{factors(n)}")