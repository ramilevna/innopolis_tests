#  medians[i][0] - количество, medians[i][1] - сумма
n, k = map(int, input().split())
lefts = [0] * (n + 1)
s = [0] * (n + 2)
s2 = [0] * (n + 2)
rights = [0] * (n + 1)
medians = [[0, 0] for _ in range(n + 1)]
medians2 = [[0, 0] for _ in range(n + 1)]
for _ in range(k):
    l, r = map(int, input().split())
    m = (l + r) // 2
    lefts[l] += 1
    medians[m][0] += 1
    medians[m][1] += m - l + 1
    medians2[m + 1][0] += 1
    medians2[m + 1][1] += r - m
    rights[r] += 1

plus = 0
minus = 0
for i in range(1, n + 1):
    if lefts[i] > 0:
        plus += lefts[i]
    s[i] = s[i-1] + plus - minus
    plus -= medians[i][0]
    minus = medians[i][1]

plus = 0
minus = 0
for i in range(n, 0, -1):
    if rights[i] > 0:
        plus += rights[i]
    s2[i] += s2[i + 1] + plus - minus
    plus -= medians2[i][0]
    minus = medians2[i][1]
s = [s[i] + s2[i] for i in range(1, n+1)]
print(s)
print(max(s))

