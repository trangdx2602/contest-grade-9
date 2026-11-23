# sinh test dang Themis: tests/BAI/TestXX/BAI.INP, BAI.OUT
# chay: python gen_tests.py [BAI ...]
import os, sys, shutil, subprocess
from random import randint, choice, sample, shuffle, seed

ROOT = os.path.dirname(os.path.abspath(__file__))
seed(2026)


def save(name, tests):
    for i, (inp, brute) in enumerate(tests, 1):
        d = os.path.join(ROOT, "tests", name, "Test%02d" % i)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, name + ".INP"), "w").write(inp)
        subprocess.run([sys.executable, os.path.join(ROOT, "solutions", name + ".py")], cwd=d, check=True)
        out = open(os.path.join(d, name + ".OUT")).read().split()
        if brute:
            assert out == brute(inp).split(), "%s Test%02d sai" % (name, i)
        print(name, "Test%02d" % i, " ".join(out[:3]))


def arr(a):
    return " ".join(map(str, a))


# ---------- Bai 1
def choxuan():
    t = [(1000000, 50000), (350000, 50000), (200000, 50000), (7, 1), (6, 1),
         (10**9, 1), (10**9, 10**9), (10**9, 142857142), (10**9, 142857143), (1, 1)]
    return [("%d\n%d\n" % (n, k), None) for n, k in t]


# ---------- Bai 2
def bf_canbang(inp):
    d = list(map(int, inp.split()))
    k, a = d[1], d[2:]
    return str(sum(x - k in a and x + k in a for x in a))


def canbang():
    def make(a, k):
        shuffle(a)
        return "%d %d\n%s\n" % (len(a), k, arr(a))

    t = ["6 1\n4 1 7 8 5 6\n", "1 1\n0\n", "3 1\n0 1 2\n",
         make(list(range(0, 1000, 2)), 1), make(list(range(1000)), 1)]
    t += [make(sample(range(1001), randint(10, 1000)), 1) for _ in range(9)]
    t += [make(sample(range(2001), 1000), 1),
          make(sample(range(10**6 + 1), 100000), 1),
          make(sample(range(150001), 100000), 1),
          make(sample(range(900000, 10**6 + 1), 100000), 1)]
    t.append("6 2\n4 -1 7 8 5 6\n")

    # tong quat: chen nhieu cap so cong buoc k de co dap an
    k = randint(1, 10**9)
    s = set()
    while len(s) < 100000:
        x = randint(-10**9, 10**9 - 2 * k)
        for j in range(randint(1, 5)):
            if x + j * k <= 10**9:
                s.add(x + j * k)
        s.add(randint(-10**9, 10**9))
    t.append(make(list(s)[:100000], k))
    return [(x, bf_canbang if len(x) < 5000 else None) for x in t]


# ---------- Bai 3
def dist(x, y):
    d = abs(ord(x) - ord(y))
    return min(d, 26 - d)


def bf_khoangcach(inp):
    d = inp.split()
    s, res = d[0], []
    for i in range(int(d[1])):
        l, r = int(d[2 + 2 * i]), int(d[3 + 2 * i])
        v = set(s[l - 1:r])
        res.append(max(dist(x, y) for x in v for y in v))
    return "\n".join(map(str, res))


def rand_str(n, kind):
    abc = "abcdefghijklmnopqrstuvwxyz"
    pool = {"all": abc, "wrap": "xyzabc", "near": abc[:randint(2, 8)],
            "few": "".join(sample(abc, randint(1, 4)))}[kind]
    return "".join(choice(pool) for _ in range(n))


def khoangcach():
    def make(s, q, short=False):
        n, lines = len(s), [s, str(q)]
        for _ in range(q):
            l = randint(1, n)
            r = min(n, l + randint(0, 20)) if short else randint(l, n)
            lines.append("%d %d" % (l, r))
        return "\n".join(lines) + "\n"

    t = ["abcyzz\n1\n2 5\n", "a\n1\n1 1\n", "an\n1\n1 2\n", "az\n1\n1 2\n"]
    t += [make(rand_str(randint(1, 1000), k), 1) for k in ["all", "few", "wrap", "near", "few", "wrap"]]
    t += [make(rand_str(100000, k), 1) for k in ["all", "wrap", "near", "few"]]
    t.append("abcyzz\n3\n1 3\n2 5\n5 6\n")
    t += [make(rand_str(1000, k), 100000, sh) for k, sh in [("all", 1), ("wrap", 0), ("near", 1)]]
    t += [make(rand_str(100000, "all"), 100000, True), make(rand_str(100000, "wrap"), 100000)]
    return [(x, bf_khoangcach if len(x) < 5000 else None) for x in t]


# ---------- Bai 4
def bf_xoadoan(inp):
    d = list(map(int, inp.split()))
    n, a, s = d[0], d[1:-1], d[-1]
    tot = sum(a)
    if tot <= s:
        return "0"
    for ln in range(1, n + 1):
        for i in range(n - ln + 1):
            if tot - sum(a[i:i + ln]) <= s:
                return str(ln)
    return "-1"


def max_sub(a):
    best = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return max(best, sum(a))


def xoadoan():
    def make(a, kind):
        tot, m = sum(a), max_sub(a)
        s = {"zero": tot + randint(0, 10),          # khong can xoa
             "none": tot - m - randint(1, 10),      # khong xoa duoc -> -1
             "all": tot - m}.get(kind)              # phai xoa doan tong lon nhat
        if s is None:
            s = tot - max(1, int(m * randint(5, 60) / 100))
        s = max(-10**14, min(10**14, s))
        return "%d\n%s\n%d\n" % (len(a), arr(a), s)

    def rnd(n, lo, hi):
        return [randint(lo, hi) for _ in range(n)]

    t = ["3\n4 2 1\n0\n", "3\n1 2 0\n5\n", "1\n7\n6\n", "4\n0 0 0 0\n0\n"]
    t += [make(rnd(randint(1, 100), 0, choice([10, 10**9])), k) for k in ["mid", "mid", "all", "mid"]]
    t += [make(rnd(5000, 0, 10**9), k) for k in ["mid", "none", "zero", "all"]]
    t += [make(rnd(100000, 0, 10**9), "mid"), make(rnd(100000, 0, 100), "mid"),
          make(rnd(100000, 0, 10**9), "all"),
          make([x if randint(1, 10) == 1 else 0 for x in rnd(100000, 0, 10**9)], "mid")]
    t += ["5\n4 -5 4 4 -2\n0\n", "3\n1 2 3\n-2\n",
          make(rnd(300, -20, 20), "mid"), make(rnd(100000, -10**9, 10**9), "mid")]
    return [(x, bf_xoadoan if len(x) < 5000 else None) for x in t]


# ---------- Bai 5
def bf_bansung(inp):
    d = list(map(int, inp.split()))
    n, k, a = d[0], d[1], d[2:]

    def ok(x):
        b = a[:]
        for _ in range(k):
            alive = [i for i in range(n) if b[i] > 0]
            if not alive:
                break
            i = alive[0]
            for j in range(i, n):
                b[j] -= max(0, x - (j - i) ** 2)
        return max(b) <= 0

    l, r = 1, max(a) + (n - 1) ** 2
    while l < r:
        mid = (l + r) // 2
        if ok(mid):
            r = mid
        else:
            l = mid + 1
    return str(l)


def bansung():
    def make(n, k, mx):
        return "%d %d\n%s\n" % (n, k, arr(randint(1, mx) for _ in range(n)))

    t = ["6 3\n6 7 1 3 2 1\n", "1 1\n1\n", "30 30\n%s\n" % arr([30] * 30)]
    t += [make(randint(5, 30), randint(1, 30), 30) for _ in range(3)]
    t += ["3 1\n3 7 3\n", make(1000, 1, 10**9), make(200000, 1, 10**9),
          "200000 1\n%s\n" % arr([10**9] * 200000)]
    t += [make(n, k, mx) for n, k, mx in [(200, 5, 1000), (1000, 1000, 10**9), (1000, 10, 10**9),
                                         (1000, 10**9, 10**9), (1000, 3, 100), (1000, 50, 1)]]
    t += [make(200000, k, mx) for k, mx in [(10**9, 10**9), (200000, 10**9), (50, 10**9), (1000, 10)]]
    return [(x, bf_bansung if len(x) < 2000 else None) for x in t]


if __name__ == "__main__":
    probs = {"CHOXUAN": choxuan, "CANBANG": canbang, "KHOANGCACH": khoangcach,
             "XOADOAN": xoadoan, "BANSUNG": bansung}
    for name in sys.argv[1:] or probs:
        shutil.rmtree(os.path.join(ROOT, "tests", name), ignore_errors=True)
        save(name, probs[name]())
