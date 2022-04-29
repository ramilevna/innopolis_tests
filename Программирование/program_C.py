n = int(input())
a = list(map(int, input().split()))
d = {}
max = 0
k = 1
for i in range(n - 1):
    if a[i] == a[i + 1]:
        k += 1
    else:
        if a[i] in d:
            if d[a[i]] + k > max:
                max = d[a[i]] + k
            if d[a[i]] < k:
                d[a[i]] = k
        else:
            if k > max:
                max = k
            d[a[i]] = k
        k = 1
print(max)