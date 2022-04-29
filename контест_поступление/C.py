n = int(input())
runners = []
klist = list(map(int, input().split()))
for i in range(n):
    runners.append(i + 1)
    k = klist[i]
    for j in range(i - 1, i - k - 1, -1):
        runners[j + 1] = runners[j]
    runners[i - k] = i + 1
print(*runners)
