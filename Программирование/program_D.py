n, k = map(int, input().split())
but = [0] * (n + 1)
arr = []
for i in range(k):
    s = input().split()
    arr.append((int(s[0]), int(s[1])))
for i in range(k):
    l = arr[i][0]
    r = arr[i][1]
    m = (l + r) // 2
    for j in range(l, m + 1):
        but[j] += j - l + 1
    for k in range(m + 1, r + 1):
        but[k] += r - k + 1
print(max(but))