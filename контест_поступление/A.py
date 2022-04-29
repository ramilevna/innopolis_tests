n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = 0
arr = []
for i in range(n):
    if a[i] - b[i] > 0:
        k += 1
        arr.append(i + 1)
print(k)
print(*arr)
