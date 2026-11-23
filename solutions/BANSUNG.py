from math import isqrt

f = open("BANSUNG.INP")
n, k = map(int, f.readline().split())
a = list(map(int, f.readline().split()))


def check(x):
    # ban o p anh huong toi i khi (i-p)^2 < x
    w = isqrt(x - 1)
    c = [0] * n
    s0 = s1 = s2 = 0
    shots = 0
    for i in range(n):
        j = i - w - 1
        if j >= 0 and c[j]:
            s0 -= c[j]
            s1 -= c[j] * j
            s2 -= c[j] * j * j

        # sum c[p] * (x - (i-p)^2)
        rem = a[i] - (x * s0 - (i * i * s0 - 2 * i * s1 + s2))
        if rem <= 0:
            continue

        c[i] = (rem + x - 1) // x
        shots += c[i]
        if shots > k:
            return False
        s0 += c[i]
        s1 += c[i] * i
        s2 += c[i] * i * i
    return True


l, r = 1, max(a) + (n - 1) ** 2
while l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1

open("BANSUNG.OUT", "w").write(str(l))
