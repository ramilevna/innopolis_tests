n = int(input())            # S0 - a0 + a3 = s2 - a3 + a0; a3 = x; x = s1 - s0 + 2a0
l2 = set()
l = []
s0 = 0
s1 = 0
for i in range(n):
    a = int(input())
    l.append(a)
    if i % 2 == 0:
        s0 += a
    else:
        s1 += a
        l2.add(a)
for i in range(0, n, 2):
    x = s1 - s0 + 2 * l[i]
    if x >= 0 and x % 2 == 0:
        x //= 2
        if x in l2:
            print("Yes")
            exit()
print("No")
