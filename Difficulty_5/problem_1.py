# TODO: Multiples of 3 or 5

lst = []
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        lst.append(i)

print("Multiples of 3 or 5 is :\n", lst)
print("Sum of multiples of 3 or 5 is :", sum(lst))
