n = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())
arr = [0] * (n + 1)
arr[0] = 1
k = 0
for i in range(a, b + 1):
    arr[i] += 1
for i in range(c, d + 1):
    arr[i] += 1
for i in range(n + 1):
    if arr[i] == 0:
        k += 1
print(k)