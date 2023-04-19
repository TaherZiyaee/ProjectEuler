# https://www.geeksforgeeks.org/find-largest-prime-factor-number/
# Python3 code to find largest prime
# factor of number
import math


# A function to find largest prime factor
def maxPrimeFactors(n):
    # Initialize the maximum prime factor
    # variable with the lowest one
    maxPrime = -1

    # Print the number of 2s that divide n
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1  # equivalent to n /= 2

    # n must be odd at this point
    while n % 3 == 0:
        maxPrime = 3
        n = n / 3

    # now we have to iterate only for integers
    # who does not have prime factor 2 and 3
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        while n % i == 0:
            maxPrime = i
            n = n / i
        while n % (i + 2) == 0:
            maxPrime = i + 2
            n = n / (i + 2)

    # This condition is to handle the
    # case when n is a prime number
    # greater than 4
    if n > 4:
        maxPrime = n

    return int(maxPrime)


# Driver code to test above function
n = 21
print(maxPrimeFactors(n))

# n = 25698751364526
# print(maxPrimeFactors(n))

# ---------------method 2----------------------
# Python3 code to find largest prime
# factor of number
def maxPrimeFactors(n):
	"""
	Find the largest prime factor of a positive integer 'n'
	:param n: positive integer ( 1 <= n <= 10^15)
	:return: largest prime factor of n
	"""
	largest_prime = -1
	i = 2
	while i * i <= n:
		while n % i == 0:
			largest_prime = i
			n = n // i
		i = i + 1
	if n > 1:
		largest_prime = n
	return largest_prime

n = 15
print(maxPrimeFactors(n))

n = 25698751364526
print(maxPrimeFactors(n))

# This code is contributed by Susobhan Akhuli
