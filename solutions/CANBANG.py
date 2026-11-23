f = open("CANBANG.INP")
n, k = map(int, f.readline().split())
a = list(map(int, f.readline().split()))

s = set(a)
res = 0
for x in a:
    if x - k in s and x + k in s:
        res += 1

open("CANBANG.OUT", "w").write(str(res))
