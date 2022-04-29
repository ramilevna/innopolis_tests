n = 10 ** 5
a = [0] * n
b = [0] * n
c = [0] * n
d = [0] * n
for i in range(3, n, 3):
    a[i] = 1
for i in range(7, n, 7):
    b[i] = 1
for i in range(4, n, 4):
    c[i] = 1
for i in range(5, n, 5):
    d[i] = 1
k = 0
for i in range(n):
    k += (a[i] + b[i] + c[i] + d[i]) % 2
print(k)


"""
"""


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b > 0:
        return gcd(b, a % b)
    else:
        return a


def lcm(a, b):
    return a * b // gcd(a, b)


k1 = n // 3 + n // 4 + n // 5 + n // 7 \
    - 2 * (n // lcm(3, 4) + n // lcm(3, 5) + n // lcm(3, 7) + n // lcm(4, 5) + n // lcm(4, 7) + n // lcm(5, 7)) \
    + 4 * (n // lcm(lcm(3, 4), 5) + n // lcm(lcm(3, 4), 7) + n // lcm(lcm(3, 5), 7) + n // lcm(lcm(4, 5), 7)) \
    - 8 * (n // lcm(lcm(3, 5), lcm(4, 7)))

print(k1)