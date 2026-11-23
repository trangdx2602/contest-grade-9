from math import isqrt

f = open("BANSUNG.INP")
n, k = map(int, f.readline().split())
a = list(map(int, f.readline().split()))


def check(x):
    # ban cach bia i mot khoang d gay x - d^2, chi co tac dung khi d <= w
    w = isqrt(x - 1)
    c = [0] * n
    s0 = t1 = t2 = 0    # tong c, c*d, c*d^2 cua cac phat con tac dung
    shots = 0
    for i in range(n):
        if i > 0:
            # sang bia moi, moi khoang cach d tang len 1
            t2 += 2 * t1 + s0
            t1 += s0
            j = i - w - 1
            if j >= 0 and c[j]:
                s0 -= c[j]
                t1 -= c[j] * (w + 1)
                t2 -= c[j] * (w + 1) * (w + 1)

        rem = a[i] - (x * s0 - t2)
        if rem <= 0:
            continue

        c[i] = (rem + x - 1) // x
        shots += c[i]
        if shots > k:
            return False
        s0 += c[i]
    return True


l, r = 1, max(a) + (n - 1) ** 2
while l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1

open("BANSUNG.OUT", "w").write(str(l))
