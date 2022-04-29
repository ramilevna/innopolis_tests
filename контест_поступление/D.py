n = int(input())
s = input()
if "or" in s or "ro" in s:
    print("Yes")
    exit()
for i in range(n - 2):
    if s[i] == "o" and s[i + 2] == "r":
        print("Yes")
        exit()
print("No")
