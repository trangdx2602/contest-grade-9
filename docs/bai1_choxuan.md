# Bài 1. Chợ Xuân (5 điểm) ⭐

| Chương trình | Dữ liệu vào | Kết quả ra | Độ khó |
|---|---|---|---|
| `CHOXUAN.*` | `CHOXUAN.INP` | `CHOXUAN.OUT` | Rất dễ |

## Đề bài

Nhà trường tổ chức Hội chợ xuân kéo dài trong 7 ngày, giá thuê một gian hàng là `K` đồng/ngày. Lớp An có `N` đồng, muốn thuê một gian hàng trong 7 ngày để bán thiệp. Hỏi số tiền còn lại sau khi thuê gian hàng của lớp An là bao nhiêu?

**Dữ liệu vào từ file văn bản `CHOXUAN.INP`:**
- Dòng đầu tiên chứa một số nguyên dương `N` (N ≤ 10⁹) là số tiền lớp An có.
- Dòng thứ hai chứa một số nguyên dương `K` (K ≤ 10⁹) là giá thuê gian hàng trong một ngày.

**Kết quả ghi ra file văn bản `CHOXUAN.OUT`:** một số nguyên là số tiền còn lại của lớp An. Nếu không đủ tiền thuê trong 7 ngày thì ghi ra `−1`.

**Ví dụ:**

| CHOXUAN.INP | CHOXUAN.OUT | Giải thích |
|---|---|---|
| 1000000<br>50000 | 650000 | Lớp An có 1000000 đồng, tổng tiền thuê là 50000 × 7 = 350000 đồng. Vậy lớp An còn lại 1000000 − 350000 = 650000 đồng. |
| 350000<br>50000 | 0 | Lớp An có 350000 đồng, tổng tiền thuê là 350000 đồng. Vậy lớp An còn lại 0 đồng. |
| 200000<br>50000 | −1 | Lớp An có 200000 đồng, tổng tiền thuê là 350000 đồng. Lớp An không đủ tiền để thuê. |

---

## Phân tích

### Đề cho gì, hỏi gì
- **Cho:** số tiền `N` và giá thuê một ngày `K`.
- **Hỏi:** `N − 7K` nếu `N ≥ 7K`, ngược lại in `−1`.

### Ý nghĩa và mục tiêu
Đây là bài khởi động. Thuật toán không có gì khó, bài chỉ kiểm tra **kỹ năng thi cơ bản**:
1. **Đọc/ghi file đúng tên.** Sai tên file là mất trọn 5 điểm.
2. **Chọn kiểu dữ liệu.** `7 × K` có thể bằng 7·10⁹, vượt giới hạn `int` (khoảng 2,1·10⁹). Đây là **bẫy chính** của bài.
3. **Xử lý trường hợp biên:** vừa đủ tiền thì in `0`, thiếu tiền thì in `−1`. Ba ví dụ trong đề ứng với đúng ba tình huống: còn tiền, vừa đủ, và không đủ.

### Điểm cần đọc kỹ
- "Thuê **trong 7 ngày**": tiền thuê là `7K`.
- `N = 7K` vẫn là **đủ** tiền, nên in `0` chứ không in `−1`.
- Đề không có subtask. Chỉ cần sai kiểu dữ liệu là mất điểm ở các test lớn.

## Phương pháp

Tính trực tiếp, độ phức tạp O(1).

```cpp
long long n, k;
cin >> n >> k;
if (n >= 7 * k) cout << n - 7 * k;
else cout << -1;
```

**Kiến thức cần:** kiểu `long long` / `int64`, đọc/ghi file.

Code đầy đủ: [`solutions/CHOXUAN.cpp`](../solutions/CHOXUAN.cpp), [`solutions/CHOXUAN.py`](../solutions/CHOXUAN.py)
