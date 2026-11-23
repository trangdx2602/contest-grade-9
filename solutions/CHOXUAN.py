f = open("CHOXUAN.INP")
n, k = map(int, f.read().split())

res = n - 7 * k
if res < 0:
    res = -1
open("CHOXUAN.OUT", "w").write(str(res))
