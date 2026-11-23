f = open("KHOANGCACH.INP")
s = f.readline().strip()
q = int(f.readline())
n = len(s)

cnt = [[0] * (n + 1) for _ in range(26)]
for c in range(26):
    ch = chr(ord('a') + c)
    row = cnt[c]
    for i in range(n):
        row[i + 1] = row[i] + (s[i] == ch)

dist = [[min(abs(x - y), 26 - abs(x - y)) for y in range(26)] for x in range(26)]

ans = []
for _ in range(q):
    l, r = map(int, f.readline().split())
    v = [c for c in range(26) if cnt[c][r] > cnt[c][l - 1]]
    res = 0
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            res = max(res, dist[v[i]][v[j]])
    ans.append(res)

open("KHOANGCACH.OUT", "w").write("\n".join(map(str, ans)))
