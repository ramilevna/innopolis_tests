n = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())
if c < a:
    a, c = c, a
    b, d = d, b
if b < c:
    print(n - (b - a + 1) - (d - c + 1))
elif c <= b < d:
    print(n - (b - a + 1) - (d - b))
elif d <= b:
    print(n - (b - a + 1))
