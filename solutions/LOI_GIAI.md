# Lời giải chi tiết – Đề HSG Tin học lớp 9 Hà Nội 2025–2026

## Tổng quan độ khó

| Bài | Tên | Điểm | Độ khó | Kiến thức cần | Độ phức tạp |
|---|---|---|---|---|---|
| 1 | Chợ Xuân | 5 | ⭐ Rất dễ | Phép tính, kiểu dữ liệu | O(1) |
| 2 | Cân bằng | 5 | ⭐⭐ Dễ | Sắp xếp, tìm kiếm nhị phân / set | O(N log N) |
| 3 | Khoảng cách | 4 | ⭐⭐⭐ Trung bình | Mảng đếm cộng dồn | O(26·N + 26²·Q) |
| 4 | Xóa đoạn | 3 | ⭐⭐⭐⭐ Khá khó | Tổng tiền tố, deque đơn điệu | O(N) |
| 5 | Bắn súng | 3 | ⭐⭐⭐⭐⭐ Khó | Chặt nhị phân đáp án, cửa sổ trượt | O(N·log(max X)) |

Một học sinh khá có thể làm trọn **Bài 1, 2, 3** (14 điểm) và lấy thêm điểm subtask ở **Bài 4, 5**:
- Bài 4 có 60% số test với `A_i ≥ 0`, làm được bằng hai con trỏ.
- Bài 5 có subtask K = 1, giải được bằng một công thức.

---

## Bài 1. Chợ Xuân ⭐

### Phân tích
- Thuê 7 ngày, mỗi ngày `K` đồng, nên tổng tiền thuê là `7 × K`.
- Nếu `N ≥ 7K` thì lớp còn lại `N − 7K` đồng.
- Ngược lại lớp không đủ tiền, in `−1`.

### Lỗi hay gặp
`K` có thể bằng `10^9`, khi đó `7K = 7·10^9`. Con số này **vượt quá kiểu `int`** (giới hạn khoảng 2,1·10^9).
- C++ phải dùng `long long`.
- Pascal phải dùng `int64`.
- Python không cần lo vì số nguyên trong Python không bị tràn.

Rất nhiều bạn mất điểm bài dễ nhất vì lỗi này.

### Code (C++)
```cpp
long long n, k;
cin >> n >> k;
if (n >= 7 * k) cout << n - 7 * k;
else cout << -1;
```

---

## Bài 2. Cân bằng ⭐⭐

### Hiểu đề
Phần tử `x` được gọi là "cân bằng K" khi trong dãy có **cả** `x + K` **và** `x − K`.

Ví dụ 1: dãy `4 1 7 8 5 6`, K = 1.

| x | x − 1 có không? | x + 1 có không? | Cân bằng? |
|---|---|---|---|
| 4 | 3 – không | 5 – có | ✗ |
| 1 | 0 – không | 2 – không | ✗ |
| 7 | 6 – có | 8 – có | ✓ |
| 8 | 7 – có | 9 – không | ✗ |
| 5 | 4 – có | 6 – có | ✓ |
| 6 | 5 – có | 7 – có | ✓ |

Đáp án là **3**.

### Cách 1: duyệt trâu (70% điểm)
Với mỗi `x`, duyệt cả dãy để tìm xem có `x − K` và `x + K` hay không. Có N phần tử, mỗi phần tử duyệt N lần, nên mất **O(N²)**. Với N ≤ 10³ thì khoảng 10⁶ phép, chạy kịp. Với N = 10⁵ thì lên tới 10¹⁰ phép, quá thời gian.

### Cách 2: tra cứu nhanh (100% điểm)
Bài toán thực chất là hỏi nhiều lần: "**số v có nằm trong dãy không?**". Có hai cách trả lời câu hỏi này nhanh:
- **C++:** sắp xếp một bản sao `b` của dãy, rồi dùng `binary_search(b, b + n, v)`. Mỗi lần hỏi mất O(log N).
- **Python:** cho dãy vào `set`, rồi kiểm tra `v in s`. Mỗi lần hỏi trung bình mất O(1).

### Lỗi hay gặp
`x + K` có thể lên tới `2·10^9`, vượt `int`, nên C++ phải dùng `long long`.

### Code (Python)
```python
s = set(a)
res = 0
for x in a:
    if x - k in s and x + k in s:
        res += 1
```

---

## Bài 3. Khoảng cách ⭐⭐⭐

### Bước 1: khoảng cách giữa hai chữ cái
Đánh số `a = 0, b = 1, ..., z = 25`. Từ chữ `x` sang chữ `y`, ta có hai hướng đi quanh vòng tròn:
- đi theo một chiều: `|x − y|` bước;
- đi theo chiều ngược lại: `26 − |x − y|` bước.

Khoảng cách là hướng ngắn hơn: **`min(|x − y|, 26 − |x − y|)`**. Giá trị lớn nhất là 13, khi hai chữ nằm đối diện nhau, ví dụ `a` và `n`.

Ví dụ: `a` và `z` có `|0 − 25| = 25`, đi chiều ngược lại chỉ mất `26 − 25 = 1` bước, nên khoảng cách là 1.

### Bước 2: nhận xét quan trọng nhất
Khoảng cách của một xâu **chỉ phụ thuộc vào những chữ cái có mặt** trong xâu. Thứ tự các chữ và số lần lặp lại không ảnh hưởng gì.

Ví dụ: `"bcyz"`, `"zzbbcy"`, `"ycbz"` đều có cùng tập chữ {b, c, y, z} nên có cùng khoảng cách.

Bảng chữ cái chỉ có **26 chữ**. Vì vậy mỗi truy vấn chỉ cần biết 26 thông tin "chữ c có mặt trong đoạn [L, R] hay không".

### Bước 3: biết nhanh chữ nào có mặt trong đoạn [L, R]
Dùng **mảng đếm cộng dồn**: `cnt[c][i]` là số lần chữ `c` xuất hiện trong `i` kí tự đầu tiên của xâu.

Khi đó số lần chữ `c` xuất hiện trong đoạn `[L, R]` là `cnt[c][R] − cnt[c][L−1]`. Hiệu này lớn hơn 0 nghĩa là chữ `c` có mặt.

Ví dụ với `S = "abcyzz"`, xét chữ `z`:

| i | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| S[i] | | a | b | c | y | z | z |
| cnt[z][i] | 0 | 0 | 0 | 0 | 0 | 1 | 2 |

Với truy vấn (2, 5): `cnt[z][5] − cnt[z][1] = 1 − 0 = 1 > 0`, vậy `z` có mặt trong đoạn.

### Bước 4: trả lời truy vấn
1. Duyệt 26 chữ cái và lấy ra danh sách `v` gồm các chữ có mặt.
2. Xét mọi cặp chữ trong `v`, tối đa 26·25/2 = 325 cặp, và lấy khoảng cách lớn nhất.

Ví dụ truy vấn (2, 5) cho đoạn `"bcyz"`, tập chữ là {b=1, c=2, y=24, z=25}:
- b–c: 1; y–z: 1
- b–y: min(23, 3) = 3; b–z: min(24, 2) = 2
- c–y: min(22, **4**) = 4; c–z: min(23, 3) = 3

Khoảng cách lớn nhất là **4**, khớp với đáp án mẫu.

### Độ phức tạp
- Tạo mảng đếm: 26·N ≈ 2,6·10⁶ phép.
- Mỗi truy vấn khoảng 26 + 325 phép, nhân với Q = 10⁵ truy vấn là khoảng 3,5·10⁷ phép.

Cả hai đều chạy kịp.

### Theo subtask
- Q = 1, hoặc N ≤ 10³ (50% đến 90% điểm): với mỗi truy vấn, duyệt trực tiếp từng kí tự trong đoạn `[L, R]` để đánh dấu chữ nào có mặt. Không cần mảng cộng dồn.
- Tổng quát (100%): dùng mảng cộng dồn như trên.

---

## Bài 4. Xóa đoạn ⭐⭐⭐⭐

### Bước 1: biến đổi đề bài
Gọi `T` là tổng cả dãy.
- Nếu `T ≤ S` thì không cần xóa gì, đáp án là **0**.
- Nếu xóa đoạn có tổng `X`, phần còn lại có tổng `T − X`. Điều kiện `T − X ≤ S` tương đương với `X ≥ T − S`.

Đặt `need = T − S`. Đề bài trở thành: **tìm đoạn con ngắn nhất có tổng ≥ need**. Nếu không có đoạn nào như vậy thì in −1.

Lưu ý: được phép xóa cả dãy (xem ví dụ 2), vì đoạn `[1, N]` cũng là một đoạn con.

### Bước 2: tổng tiền tố
Đặt `p[0] = 0` và `p[i] = A[1] + ... + A[i]`. Khi đó tổng đoạn `[l+1, r]` bằng `p[r] − p[l]`, còn độ dài đoạn là `r − l`.

Ta cần cặp `l < r` sao cho **`p[r] − p[l] ≥ need`** và **`r − l` nhỏ nhất**.

### Cách 1: duyệt mọi cặp (40% đến 60% điểm)
Thử mọi cặp `(l, r)`, mất O(N²). Chạy kịp với N ≤ 5000.

### Cách 2: hai con trỏ khi A[i] ≥ 0 (80% điểm)
Khi mọi phần tử không âm, mở rộng đoạn thì tổng chỉ tăng lên, còn thu hẹp đoạn thì tổng chỉ giảm xuống. Vì vậy dùng được cửa sổ trượt:
- tăng `r` dần;
- khi tổng của cửa sổ đã ≥ need thì tăng `l` để thu hẹp đoạn càng ngắn càng tốt.

### Cách 3: deque đơn điệu (100% điểm, dãy có số âm)
Khi dãy có số âm, hai con trỏ không còn đúng nữa. Ta duyệt `r` từ 0 đến N và giữ một hàng đợi hai đầu `dq` chứa các chỉ số `l` "đáng giữ lại". Các chỉ số trong `dq` có **`p[l]` tăng dần**.

Mỗi khi xét đến `r`, làm 3 việc:

1. **Lấy ở đầu hàng:** khi `p[r] − p[dq.đầu] ≥ need`, ta đã tìm được một đoạn hợp lệ, cập nhật `res = min(res, r − dq.đầu)`. Sau đó **bỏ đầu hàng ra**.
   *Vì sao được bỏ?* Các `r` lớn hơn ở sau, nếu ghép với `l` này thì chỉ cho đoạn dài hơn. Chỉ số `l` này đã dùng xong.
2. **Dọn ở cuối hàng:** khi `p[dq.cuối] ≥ p[r]`, **bỏ cuối hàng ra**.
   *Vì sao được bỏ?* `r` nằm sau và có `p[r]` nhỏ hơn hoặc bằng. Sau này, nếu ghép với `l` cũ mà đạt `need` thì ghép với `r` cũng đạt `need`, lại cho đoạn ngắn hơn. Vậy `l` cũ không bao giờ tốt hơn `r`.
3. Đẩy `r` vào cuối hàng.

Mỗi chỉ số được đẩy vào và lấy ra khỏi hàng nhiều nhất một lần, nên tổng thời gian là **O(N)**.

### Chạy tay ví dụ 1
`A = [4, −5, 4, 4, −2]`, `S = 0`. Ta có `T = 5` nên `need = 5`. Tổng tiền tố `p = [0, 4, −1, 3, 7, 5]`.

| r | p[r] | Lấy ở đầu hàng | Dọn ở cuối hàng | dq sau bước | res |
|---|---|---|---|---|---|
| 0 | 0 | – | – | [0] | ∞ |
| 1 | 4 | 4−0=4 < 5 | – | [0, 1] | ∞ |
| 2 | −1 | – | bỏ 1 (p=4), bỏ 0 (p=0) | [2] | ∞ |
| 3 | 3 | 3−(−1)=4 < 5 | – | [2, 3] | ∞ |
| 4 | 7 | 7−(−1)=8 ≥ 5, res = 4−2 = **2**, bỏ 2 | – | [3, 4] | 2 |
| 5 | 5 | 5−3=2 < 5 | bỏ 4 (p=7) | [3, 5] | 2 |

Đáp án là **2**, ứng với việc xóa đoạn `A[3..4] = 4, 4`.

### Lỗi hay gặp
- `|S| ≤ 10^14`, nên tổng và `need` phải dùng `long long`.
- Quên trường hợp đáp án 0, khi `T ≤ S`.
- Quên trường hợp đáp án −1, khi biến `res` không được cập nhật lần nào.

---

## Bài 5. Bắn súng ⭐⭐⭐⭐⭐

### Bước 1: chặt nhị phân theo X
Nhận xét: **X càng lớn thì mỗi phát bắn càng mạnh, nên số phát cần dùng càng ít** (hoặc giữ nguyên). Đáp án vì thế có tính chất:

```
X:      1  2  3  4 | 5  6  7 ...
Đủ K?   ✗  ✗  ✗  ✗ | ✓  ✓  ✓ ...
```

Ta **chặt nhị phân** để tìm X nhỏ nhất cho kết quả ✓. Chỉ cần viết thêm một hàm `check(X)` trả lời câu hỏi "với sức công phá X, bắn không quá K phát có phá hết bia không?".

Cận trên của X: chọn `X = max(A) + (N−1)²`. Với X này, một phát vào bia 1 đã phá được mọi bia, vì bia thứ `j` (đánh số từ 1) nhận được `X − (j−1)² ≥ max(A)` sát thương.

### Bước 2: hàm check(X) – mô phỏng
Đạn **luôn trúng bia còn sống đầu tiên**, nên quá trình bắn được xác định hoàn toàn, không có lựa chọn nào. Ta duyệt bia từ trái sang phải:
- Khi đến bia `i`, mọi bia trước nó đã bị phá. Tính độ bền còn lại `rem = A[i] − (sát thương từ các phát bắn trước)`.
- Nếu `rem > 0`, bia `i` là bia sống đầu tiên, nên các phát tiếp theo đều trúng nó. Cần bắn đúng `c[i] = ⌈rem / X⌉` phát thì bia mới vỡ.
- Cộng `c[i]` vào tổng số phát. Nếu tổng vượt K thì trả về sai ngay.

**Cách trâu (subtask N ≤ 1000):** sau mỗi lần bắn ở `i`, cập nhật sát thương cho mọi bia `j > i`. Mỗi lần check mất O(N²).

### Bước 3: tính sát thương nhanh (100% điểm)
Phát bắn ở `p` gây cho bia `i` sát thương `X − (i−p)²` nếu `(i−p)² < X`, còn lại thì gây 0. Gọi `w` là khoảng cách lớn nhất còn gây sát thương (`w² < X`). Như vậy chỉ các bia `p` trong cửa sổ `[i−w, i−1]` ảnh hưởng tới `i`.

Gọi `d = i − p` là **khoảng cách** từ chỗ bắn `p` tới bia `i`. Sát thương tổng lên bia `i`:

```
Σ c[p] · (X − d²)  =  X·s0 − t2
```

với ba tổng lấy trên các phát còn tác dụng:
- `s0 = Σ c[p]` là tổng số phát;
- `t1 = Σ c[p]·d`;
- `t2 = Σ c[p]·d²`.

**Cập nhật khi chuyển từ bia `i−1` sang bia `i`:** mọi khoảng cách `d` tăng thêm 1. Vì `(d+1)² = d² + 2d + 1`, ta có:
```
t2 += 2·t1 + s0
t1 += s0
```
Sau đó bỏ phát bắn ở `j = i − w − 1` ra khỏi ba tổng vì nó đã quá xa. Phát này đang ở khoảng cách `w + 1`:
```
s0 -= c[j];  t1 -= c[j]·(w+1);  t2 -= c[j]·(w+1)²
```
Nếu phải bắn vào bia `i` thì cộng `c[i]` vào `s0`. Phát này có khoảng cách `d = 0` nên `t1`, `t2` giữ nguyên.

Nhờ vậy mỗi lần check chỉ mất **O(N)**. Tổng cộng khoảng N × log₂(4·10¹⁰) ≈ 2·10⁵ × 36 ≈ 7·10⁶ phép.

**Vì sao không dùng vị trí `p` trực tiếp?** Khai triển `(i − p)² = i² − 2ip + p²` cũng ra công thức O(N). Khi đó phải giữ tổng `Σ c[p]·p²`, với `p` lên tới 2·10⁵ nên tổng này có thể tới khoảng 3·10¹⁹, **vượt `long long`**. Test 20 của bộ test bắt đúng trường hợp này. Còn khoảng cách `d` luôn ≤ √X, nên mọi giá trị trong cách trên chỉ cỡ 4·10¹⁰ và `long long` chứa thoải mái.

### Chạy tay ví dụ 1
`A = [6, 7, 1, 3, 2, 1]` và K = 3, đánh số bia từ 0.

**Thử X = 5** (w = 2, vì 2² = 4 < 5):

| Bia i | A[i] | Sát thương nhận được | rem | Bắn c[i] | Tổng số phát |
|---|---|---|---|---|---|
| 0 | 6 | 0 | 6 | ⌈6/5⌉ = 2 | 2 |
| 1 | 7 | 2·(5−1) = 8 | −1 | 0 | 2 |
| 2 | 1 | 2·(5−4) = 2 | −1 | 0 | 2 |
| 3 | 3 | 0 (bia 0 đã ra khỏi cửa sổ) | 3 | 1 | 3 |
| 4 | 2 | 1·(5−1) = 4 | −2 | 0 | 3 |
| 5 | 1 | 1·(5−4) = 1 | 0 | 0 | 3 |

Tổng 3 phát, không quá K, nên X = 5 đạt ✓.

Các giá trị `s0, t1, t2` trong lần chạy trên. Cột "Sát thương" là `5·s0 − t2`, đúng bằng cột "Sát thương nhận được" ở bảng trên:

| i | Dịch khoảng cách | Bỏ phát ở j | s0 | t1 | t2 | Sát thương | Bắn thêm |
|---|---|---|---|---|---|---|---|
| 0 | – | – | 0 | 0 | 0 | 0 | 2, nên s0 = 2 |
| 1 | t2 += 0+2, t1 += 2 | – | 2 | 2 | 2 | 10−2 = 8 | – |
| 2 | t2 += 4+2, t1 += 2 | – | 2 | 4 | 8 | 10−8 = 2 | – |
| 3 | t2 += 8+2, t1 += 2 | j = 0: bỏ 2 phát ở khoảng cách 3 | 0 | 0 | 0 | 0 | 1, nên s0 = 1 |
| 4 | t2 += 0+1, t1 += 1 | – | 1 | 1 | 1 | 5−1 = 4 | – |
| 5 | t2 += 2+1, t1 += 1 | – | 1 | 2 | 4 | 5−4 = 1 | – |

**Thử X = 4** (w = 1):

| Bia i | A[i] | Sát thương nhận được | rem | Bắn c[i] | Tổng số phát |
|---|---|---|---|---|---|
| 0 | 6 | 0 | 6 | 2 | 2 |
| 1 | 7 | 2·(4−1) = 6 | 1 | 1 | 3 |
| 2 | 1 | 1·3 = 3 | −2 | 0 | 3 |
| 3 | 3 | 0 | 3 | 1 | **4 > 3** ✗ |

Vậy X = 4 không đạt, và đáp án là **5**.

### Subtask K = 1 (20% điểm, không cần chặt nhị phân)
Chỉ có đúng 1 phát bắn, và nó trúng bia 1. Bia thứ `j` nhận `X − (j−1)²` sát thương. Để phá hết bia cần `X ≥ A[j] + (j−1)²` với mọi `j`, nên:

**Đáp án = max(A[j] + (j−1)²)**

Kiểm tra với ví dụ 2: `max(3+0, 7+1, 3+4) = 8` ✓.

### Lỗi hay gặp
- X có thể lên tới khoảng 4·10¹⁰, nên phải dùng `long long`.
- Nếu tính theo vị trí tuyệt đối `p` (tổng `Σ c[p]·p²`), số trung gian sẽ **vượt `long long`**. Phải tính theo khoảng cách `d` như trên. Python không bị tràn số nên không gặp lỗi này, nhưng Pascal và C++ thì có.
- Tính `w` bằng `sqrt` số thực có thể bị lệch 1 đơn vị, nên cần chỉnh lại bằng vòng `while`.
- Phải dừng ngay khi số phát vượt K, nếu không số phát có thể rất lớn và làm chương trình chậm đi.
