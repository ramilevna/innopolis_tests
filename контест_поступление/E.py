n = int(input())
a = list(map(int, input().split()))
lmx = a[0]
ans = 0
iprev = 0
imx = -1
mx = 0
for i in range(n):
    if a[i] >= mx:
        mx = a[i]
        imx = i
n1 = n
n = imx + 1
i = 1
while i < n:
    s = 0
    while i < n and a[i] < lmx:
        s += a[i]
        i += 1
    if i < n:
        ans += lmx * (i - iprev - 1) - s
        iprev = i
        lmx = a[i]
        i += 1
a = a[imx:n1]
a.reverse()
n = n1 - imx
iprev = 0
i = 1
lmx = a[0]
while i < n:
    s = 0
    while i < n and a[i] < lmx:
        s += a[i]
        i += 1
    if i < n:
        ans += lmx * (i - iprev - 1) - s
        iprev = i
        lmx = a[i]
        i += 1
print(ans)
