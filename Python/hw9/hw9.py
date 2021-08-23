# Homework 9
#
# ###############################################################################
#
# problem9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

res = [print("Problem #9\n\n a: {}, b: {}, c: {}".format(a, b, c)) for a in range(1, 501) for b in range(a + 1, 501) for c in range(b + 1, 501)
       if ((a * a + b * b == c * c) and (a+b+c) == 1000)]

print("==============================================================================================")

# problem6
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

print("Problem #6\n\n", pow(sum([i for i in range(1, 101)]), 2) - sum([i*i for i in range(1, 101)]))

print("==============================================================================================")

# problem48
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

print("Problem #48\n\n", sum([pow(n, n) for n in range(1, 1000 + 1)]) % 10**10)

print("==============================================================================================")

# problem40
#
# Champernowne's constant

s = "".join(str(i) for i in range(1, 1000000))
ans = 1
for i in range(7):
    ans *= int(s[10**i - 1])

print("Problem #40\n\n", ans)

print("==============================================================================================")
