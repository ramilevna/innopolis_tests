n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif int(i ** 0.5) ** 2 == i:
        dp[i] = dp[int(i ** 0.5)] * 2
    elif i % 2 != 0:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i // 2] + dp[2]
print(dp[n])