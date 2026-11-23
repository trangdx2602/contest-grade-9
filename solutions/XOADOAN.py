from collections import deque

f = open("XOADOAN.INP")
n = int(f.readline())
a = list(map(int, f.readline().split()))
s = int(f.readline())

p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] + a[i]

if p[n] <= s:
    res = 0
else:
    # tim doan ngan nhat co tong >= need
    need = p[n] - s
    res = n + 1
    dq = deque()
    for r in range(n + 1):
        while dq and p[r] - p[dq[0]] >= need:
            res = min(res, r - dq.popleft())
        while dq and p[dq[-1]] >= p[r]:
            dq.pop()
        dq.append(r)
    if res > n:
        res = -1

open("XOADOAN.OUT", "w").write(str(res))
