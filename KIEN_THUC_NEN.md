# Kiến thức nền tảng cho đề HSG Tin 9

Tài liệu này tổng hợp những kiến thức cần nắm để làm được đề thi năm 2025–2026, sắp xếp từ dễ đến khó. Mỗi mục gồm phần giải thích ngắn, code mẫu, tên bài trong đề có dùng kiến thức đó và gợi ý bài luyện tập.

## Bản đồ kiến thức

| # | Kiến thức | Mức độ | Dùng ở bài |
|---|---|---|---|
| 1 | Kiểu dữ liệu và tràn số | Bắt buộc | 1, 2, 4, 5 |
| 2 | Đọc/ghi file | Bắt buộc | Tất cả |
| 3 | Ước lượng độ phức tạp | Bắt buộc | Tất cả |
| 4 | Một số công thức toán nhỏ | Cơ bản | 1, 3, 5 |
| 5 | Sắp xếp và tìm kiếm nhị phân | Cơ bản | 2 |
| 6 | Set / map | Cơ bản | 2 |
| 7 | Mảng cộng dồn (prefix sum) | Quan trọng | 3, 4, 5 |
| 8 | Hai con trỏ / cửa sổ trượt | Quan trọng | 4, 5 |
| 9 | Deque đơn điệu | Nâng cao | 4 |
| 10 | Chặt nhị phân đáp án | Nâng cao | 5 |
| 11 | Mô phỏng và tối ưu mô phỏng | Nâng cao | 5 |

Lộ trình gợi ý:
- Nắm chắc mục 1–7 là đủ làm khoảng **14/20 điểm**, gồm Bài 1, 2, 3 và một phần Bài 4.
- Mục 8–11 dùng để lấy trọn Bài 4 và Bài 5.

---

## 1. Kiểu dữ liệu và tràn số

| Kiểu (C++) | Giới hạn khoảng | Ghi nhớ |
|---|---|---|
| `int` | ±2,1·10⁹ | Đủ dùng khi số ≤ 10⁹ |
| `long long` | ±9,2·10¹⁸ | Dùng khi số tới 10¹⁸ |

**Quy tắc:** nhân hoặc cộng hai số cỡ 10⁹ thì kết quả có thể vượt `int`, nên phải dùng `long long`.

```cpp
int k = 1000000000;
long long a = 7 * k;        // SAI: 7 * k tinh bang int, tran truoc khi gan
long long b = 7LL * k;      // DUNG
```

Pascal dùng `int64`. Python không lo tràn số, nhưng chạy chậm hơn C++ khoảng 10–50 lần.

Gặp trong đề:
- Bài 1: `7K` tới 7·10⁹.
- Bài 2: `A_i + K` tới 2·10⁹.
- Bài 4: tổng tới 10¹⁴.
- Bài 5: nếu đặt công thức theo vị trí tuyệt đối thì tổng trung gian tới khoảng 3·10¹⁹, vượt cả `long long`. Cách khắc phục là đặt công thức theo khoảng cách để các số luôn nhỏ. Khi số quá lớn, nên **đổi cách tính** thay vì tìm kiểu dữ liệu lớn hơn.

---

## 2. Đọc/ghi file

Đề thi luôn đọc từ file `.INP` và ghi ra file `.OUT`. Sai tên file là bị 0 điểm cả bài.

```cpp
int main() {
    freopen("TENBAI.INP", "r", stdin);
    freopen("TENBAI.OUT", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);   // doc nhanh khi input lon
    ...
}
```

```python
f = open("TENBAI.INP")
n = int(f.readline())
a = list(map(int, f.readline().split()))
open("TENBAI.OUT", "w").write(str(res))
```

Khi có nhiều dòng output (ví dụ Q truy vấn), C++ nên in `'\n'` thay vì `endl` vì `endl` chậm hơn. Python nên gom kết quả vào một list rồi ghi ra một lần bằng `"\n".join(...)`.

---

## 3. Ước lượng độ phức tạp

Máy chấm chạy được khoảng **10⁸ phép tính đơn giản mỗi giây** với C++. Với Python, con số này chỉ khoảng 10⁷. Dựa vào giới hạn N trong đề, có thể đoán được độ phức tạp cần dùng:

| Giới hạn N | Độ phức tạp chấp nhận được | Thuật toán thường gặp |
|---|---|---|
| ≤ 20 | O(2ᴺ) | Duyệt mọi tập con |
| ≤ 500 | O(N³) | Ba vòng lặp |
| ≤ 5000 | O(N²) | Hai vòng lặp, duyệt mọi đoạn |
| ≤ 10⁵ – 10⁶ | O(N log N) hoặc O(N) | Sắp xếp, nhị phân, prefix sum, hai con trỏ |
| ≤ 10⁹ trở lên | O(log N) hoặc O(1) | Công thức, chặt nhị phân |

**Mẹo đi thi:** đọc phần ràng buộc của từng subtask trước. Mỗi subtask là một gợi ý cho thuật toán cần dùng. Bài nào chưa nghĩ ra cách tối ưu thì cứ làm cách trâu để lấy điểm subtask nhỏ.

---

## 4. Một số công thức toán nhỏ

**Chia làm tròn lên** ⌈a/b⌉ với a, b > 0:
```cpp
long long c = (a + b - 1) / b;
```
Không nên dùng `ceil(a / b)` vì phép chia số thực có thể sai với số lớn. Bài 5 dùng công thức này để tính số phát cần bắn.

**Căn bậc hai nguyên** (số `w` lớn nhất có w² ≤ x):
```cpp
long long w = sqrt((double)x);
while (w * w > x) w--;
while ((w + 1) * (w + 1) <= x) w++;
```
Trong Python dùng `math.isqrt(x)`. Bài 5 dùng công thức này để tính cửa sổ ảnh hưởng của một phát bắn.

**Khoảng cách trên vòng tròn có `m` vị trí:**
```cpp
int d = abs(x - y);
d = min(d, m - d);
```
Bài 3 dùng công thức này với m = 26 chữ cái.

---

## 5. Sắp xếp và tìm kiếm nhị phân

**Tìm kiếm nhị phân** trả lời câu hỏi "**số x có trong dãy đã sắp xếp không?**" trong O(log N): mỗi bước so x với phần tử ở giữa rồi bỏ đi một nửa dãy.

```cpp
sort(b, b + n);
bool co = binary_search(b, b + n, x);       // co x hay khong
int vt = lower_bound(b, b + n, x) - b;      // vi tri dau tien >= x
```

Tự viết (nên thuộc lòng, vì mục 10 cũng dùng khung code này):
```cpp
int l = 0, r = n - 1;
while (l <= r) {
    int mid = (l + r) / 2;
    if (b[mid] == x) return true;
    if (b[mid] < x) l = mid + 1;
    else r = mid - 1;
}
return false;
```

Gặp trong đề: Bài 2, để kiểm tra `x − K` và `x + K` có trong dãy không.

---

## 6. Set / map

| | C++ | Python | Thời gian mỗi thao tác |
|---|---|---|---|
| Tập hợp | `set<long long>`, `unordered_set` | `set()` | O(log N) hoặc O(1) |
| Đếm số lần xuất hiện | `map<long long, int>` | `dict`, `Counter` | O(log N) hoặc O(1) |

```cpp
set<long long> s(a, a + n);
if (s.count(x)) ...
```
```python
s = set(a)
if x in s: ...
```

Gặp trong đề: Bài 2. Với C++, sắp xếp + `binary_search` hay `set` đều được.

---

## 7. Mảng cộng dồn (prefix sum)

Đây là **kiến thức quan trọng nhất của đề này**. Nó xuất hiện ở Bài 3, 4 và cả Bài 5.

**Ý tưởng:** đặt `p[i] = a[1] + a[2] + ... + a[i]`, với `p[0] = 0`. Khi đó tổng đoạn bất kì tính được ngay trong O(1):

```
tổng a[l..r] = p[r] − p[l−1]
```

```cpp
for (int i = 1; i <= n; i++) p[i] = p[i - 1] + a[i];
```

**Biến thể "đếm cộng dồn":** `cnt[c][i]` là số lần chữ `c` xuất hiện trong `i` kí tự đầu. Mảng này cho biết ngay trong O(1) đoạn `[l, r]` có bao nhiêu chữ `c` (Bài 3).

**Biến thể "tổng có trọng số":** giữ đồng thời `Σ c`, `Σ c·d`, `Σ c·d²` để tính nhanh các tổng dạng `Σ c·(X − d²)` (Bài 5).

Bài luyện: tổng đoạn con, đếm số đoạn có tổng bằng K, tổng hình chữ nhật trên mảng 2 chiều.

---

## 8. Hai con trỏ / cửa sổ trượt

Áp dụng khi xét các đoạn `[l, r]` mà **mở rộng đoạn thì tổng tăng, thu hẹp đoạn thì tổng giảm**. Trường hợp điển hình là dãy không có số âm. Cả `l` và `r` chỉ tiến về phía trước, nên tổng thời gian là O(N) thay vì O(N²).

Mẫu: tìm đoạn ngắn nhất có tổng ≥ X với dãy `a[i] ≥ 0`.
```cpp
int l = 1, res = INF;
long long sum = 0;
for (int r = 1; r <= n; r++) {
    sum += a[r];
    while (sum >= X) {              // con thu hep duoc
        res = min(res, r - l + 1);
        sum -= a[l++];
    }
}
```

**Cửa sổ trượt kích thước cố định:** khi `r` tăng thì thêm `a[r]` vào, đồng thời bỏ `a[r − w]` ra. Bài 5 dùng cách này để giữ ba tổng `s0, t1, t2`.

Gặp trong đề:
- Bài 4, subtask `A_i ≥ 0` (60% số test).
- Bài 5.

---

## 9. Deque đơn điệu

Khi dãy có **số âm**, hai con trỏ không còn đúng. Ta dùng **hàng đợi hai đầu** (`deque`) và luôn giữ các phần tử trong đó **tăng dần** (hoặc giảm dần). Phần tử nào chắc chắn không bao giờ tốt hơn phần tử khác thì bỏ đi ngay.

Ứng dụng kinh điển:
1. **Min/max trên cửa sổ trượt** (bài nên học đầu tiên):
   ```cpp
   deque<int> dq;                                   // chi so, a[] tang dan
   for (int i = 1; i <= n; i++) {
       while (!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back();
       dq.push_back(i);
       if (dq.front() <= i - k) dq.pop_front();     // ra khoi cua so
       if (i >= k) cout << a[dq.front()] << ' ';    // min cua so [i-k+1, i]
   }
   ```
2. **Đoạn ngắn nhất có tổng ≥ X, dãy có số âm.** Đây chính là Bài 4, chạy trên mảng tổng tiền tố. Xem chi tiết trong `solutions/LOI_GIAI.md`.

Mỗi phần tử vào và ra deque nhiều nhất một lần, nên tổng thời gian là O(N).

---

## 10. Chặt nhị phân đáp án

**Nhận biết:** đề hỏi "tìm **giá trị nhỏ nhất** (hoặc lớn nhất) của X sao cho thỏa điều kiện", và điều kiện có tính chất **đơn điệu**: nếu X thỏa thì mọi giá trị lớn hơn X cũng thỏa.

```
X:      1  2  3  4  5  6  7  8
check:  ✗  ✗  ✗  ✗  ✓  ✓  ✓  ✓   → tìm số ✓ đầu tiên
```

**Cách làm:** thay vì đi tìm X, ta viết hàm `check(X)` trả lời câu hỏi "X có đạt không?", việc này thường dễ hơn nhiều. Sau đó chặt nhị phân:

```cpp
long long l = 1, r = MAX;             // r chac chan dat
while (l < r) {
    long long mid = (l + r) / 2;
    if (check(mid)) r = mid;          // mid dat -> dap an <= mid
    else l = mid + 1;                 // mid khong dat -> dap an > mid
}
// l la dap an
```

Thời gian là O(log MAX) lần gọi `check`. Với MAX = 10¹¹ thì chỉ khoảng 37 lần.

Bài luyện kinh điển:
- Chia dãy thành K đoạn sao cho tổng lớn nhất của các đoạn là nhỏ nhất.
- Cắt gỗ thành các khúc dài nhất có thể.
- Tìm thời gian ngắn nhất để N máy sản xuất đủ M sản phẩm.

Gặp trong đề: Bài 5.

---

## 11. Mô phỏng và tối ưu mô phỏng

**Mô phỏng:** làm đúng theo những gì đề mô tả, từng bước một. Cách này luôn nên viết trước vì hai lý do:
1. Lấy được điểm các subtask nhỏ.
2. Dùng làm **lời giải trâu** để so sánh kết quả với lời giải tối ưu.

**Tối ưu mô phỏng:** khi mô phỏng quá chậm, tìm chỗ tính lặp đi lặp lại rồi thay bằng một trong các cách sau:
- mảng cộng dồn hoặc mảng hiệu (cập nhật cả đoạn trong O(1));
- khai triển công thức để cập nhật tổng nhanh khi chuyển sang phần tử kế tiếp. Bài 5 dùng `(d + 1)² = d² + 2d + 1` để cập nhật tổng bình phương khoảng cách trong O(1);
- cửa sổ trượt.

---

## Kỹ năng đi thi

1. **Đọc hết đề trước**, ước lượng độ khó của từng bài và làm bài dễ trước. Bài 1, 2 chiếm 10 điểm và chỉ mất khoảng 20 phút.
2. **Đọc ràng buộc subtask** để biết mỗi mức cần độ phức tạp nào (xem mục 3).
3. **Lấy điểm từng phần:** chưa nghĩ ra cách tối ưu thì nộp cách trâu.
4. **Tự sinh test:** viết một lời giải trâu và một chương trình sinh test ngẫu nhiên nhỏ, rồi so kết quả với lời giải tối ưu. Script `gen_tests.py` trong thư mục này làm đúng việc đó.
5. **Kiểm tra trước khi nộp:**
   - tên file `.INP`, `.OUT` đúng chưa;
   - có dùng `long long` chỗ cần chưa;
   - đã xử lý các trường hợp biên chưa (N = 1, đáp án 0 hoặc −1);
   - đã bỏ hết lệnh in debug chưa.

## Nguồn luyện tập gợi ý
- **VNOI Wiki** (vnoi.info/wiki): bài viết về prefix sum, hai con trỏ, deque, chặt nhị phân.
- **oj.vnoi.info**, **Codeforces** (lọc độ khó 800–1400), **CSES Problem Set** (phần *Sorting and Searching*).
- Đề HSG Tin 9 các tỉnh những năm trước: phần lớn dùng đúng các kiến thức trong tài liệu này.
