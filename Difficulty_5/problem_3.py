def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def factors(n):
    for i in range(2,(n+1)//2):
        if n%i==0 and is_prime(i):
            # print(i,end=' - ')
            print(i)


# factors(600851475143)
factors(6008568362)
