n = int(input())
a = list(map(int, input().split()))
b = []
if a[0] != a[1]:
    b.append(a[0])
k = 0
for i in range(1, n):
    if a[i] == a[i-1]:
        k += 1
    else:
        k = 1
    if k < 3:
        b.append(a[i])
print(*b)

