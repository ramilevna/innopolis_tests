n = 10 ** 5 + 1
s = 0
k = 0
s += n - 1                          # на первом месте стоит самое большое число
for i in range(2, n//2 + 1):
    if i % 2 != 0:
        s += n - i - k
    else:
        k += 1
        s += k
for i in range(n//2 + 1, n):
    if i % 2 != 0:
        s += (n - i) // 2
    else:
        s += (n - i) // 2 + 1
print(s)