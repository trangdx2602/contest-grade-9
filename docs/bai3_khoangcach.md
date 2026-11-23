# Bài 3. Khoảng cách (4 điểm) ⭐⭐⭐

| Chương trình | Dữ liệu vào | Kết quả ra | Độ khó |
|---|---|---|---|
| `KHOANGCACH.*` | `KHOANGCACH.INP` | `KHOANGCACH.OUT` | Trung bình |

## Đề bài

Điền 26 kí tự Tiếng Anh in thường theo thứ tự từ điển thành một vòng tròn, các kí tự cách đều nhau 1 đơn vị (xem hình trong đề, trang 2). **Khoảng cách giữa hai kí tự** là số bước di chuyển ngắn nhất từ kí tự này đến kí tự kia. Ví dụ, khoảng cách giữa hai kí tự `'a'` và `'c'` là 2, khoảng cách giữa `'a'` và `'z'` là 1.

**Khoảng cách của một xâu** là khoảng cách lớn nhất giữa hai kí tự bất kì của xâu đó. Ví dụ, tính khoảng cách của xâu `"adc"`:
- Khoảng cách của `'a'` và `'d'` là 3.
- Khoảng cách của `'a'` và `'c'` là 2.
- Khoảng cách của `'d'` và `'c'` là 1.

Vậy khoảng cách của xâu `"adc"` là `max(3, 2, 1) = 3`.

Cho xâu `S` gồm `N` kí tự được đánh chỉ số từ 1 đến `N`, và `Q` truy vấn. Mỗi truy vấn yêu cầu tính khoảng cách của xâu con từ vị trí `L` đến vị trí `R` trong xâu `S` (1 ≤ L ≤ R ≤ N).

**Dữ liệu vào từ file văn bản `KHOANGCACH.INP`:**
- Dòng đầu tiên chứa xâu `S` gồm `N` kí tự Tiếng Anh in thường (1 ≤ N ≤ 10⁵).
- Dòng thứ hai chứa số nguyên dương `Q` (Q ≤ 10⁵).
- `Q` dòng tiếp theo, mỗi dòng gồm hai số nguyên `L, R` (1 ≤ L ≤ R ≤ N) mô tả đoạn con của xâu `S` cần tính khoảng cách.

**Kết quả ghi ra file văn bản `KHOANGCACH.OUT`:** gồm `Q` dòng, mỗi dòng một số nguyên là kết quả của truy vấn tương ứng.

**Ví dụ:**

| KHOANGCACH.INP | KHOANGCACH.OUT | Giải thích |
|---|---|---|
| abcyzz<br>3<br>1 3<br>2 5<br>5 6 | 2<br>4<br>0 | Truy vấn 1: khoảng cách của xâu `"abc"` là 2.<br>Truy vấn 2: khoảng cách của xâu `"bcyz"` là 4.<br>Truy vấn 3: khoảng cách của xâu `"zz"` là 0. |

**Ràng buộc:**
- Có 50% số test ứng với 50% số điểm có Q = 1; N ≤ 10³.
- 20% số test tiếp theo ứng với 20% số điểm có Q = 1.
- 20% số test tiếp theo ứng với 20% số điểm có N ≤ 10³.
- 10% số test còn lại ứng với 10% số điểm không có ràng buộc gì thêm.

---

## Phân tích

### Đề cho gì, hỏi gì
- **Cho:** xâu `S` và `Q` đoạn `[L, R]`.
- **Hỏi:** với mỗi đoạn, khoảng cách lớn nhất trên vòng tròn giữa hai kí tự bất kì trong đoạn.

### Ý nghĩa và mục tiêu
Bài kiểm tra ba kỹ năng, xếp từ dễ đến khó:
1. **Mô hình hóa vòng tròn.** Khoảng cách giữa hai chữ `x`, `y` (đánh số từ 0 đến 25) là `min(|x − y|, 26 − |x − y|)`. Giá trị lớn nhất là 13.
2. **Nhận xét rút gọn bài toán (ý chính của bài).** Khoảng cách của một xâu **chỉ phụ thuộc vào tập chữ cái có mặt** trong xâu, không phụ thuộc thứ tự hay số lần lặp. Bảng chữ cái chỉ có 26 chữ, nên mỗi đoạn chỉ cần mô tả bằng 26 giá trị "có / không có".
3. **Trả lời nhiều truy vấn đoạn nhanh.** Dùng **mảng đếm cộng dồn** để biết ngay trong O(1) chữ `c` có xuất hiện trong `[L, R]` hay không.

### Đọc subtask để đoán phương pháp

| Subtask | Ràng buộc | Phương pháp gợi ý | Độ phức tạp |
|---|---|---|---|
| 50% | Q = 1; N ≤ 10³ | Duyệt mọi cặp kí tự trong đoạn | O(N²) |
| 20% | Q = 1 (N tới 10⁵) | Duyệt đoạn một lần để đánh dấu chữ có mặt, rồi xét các cặp chữ | O(N + 26²) |
| 20% | N ≤ 10³ (Q tới 10⁵) | Cách trên mất O(N·Q) ≈ 10⁸, sát giới hạn thời gian. Có thể tính sẵn kết quả cho mọi đoạn | O(N²·26 + Q) |
| 10% | Không ràng buộc | Mảng đếm cộng dồn `cnt[26][N]` | O(26·N + 26²·Q) |

Hai subtask đầu (70% số điểm) chỉ có **một truy vấn**, nên chỉ cần hiểu đúng định nghĩa khoảng cách. Hai subtask sau mới cần đến **kỹ thuật trả lời nhiều truy vấn đoạn**.

### Điểm cần đọc kỹ
- Khoảng cách đi theo **chiều ngắn hơn** trên vòng tròn. Ví dụ `'a'` và `'z'` cách nhau 1, không phải 25. Ví dụ truy vấn 2 kiểm tra đúng chỗ này: `"bcyz"` có cặp c–y cách nhau 4 (đi qua z, a, b), chứ không phải 22.
- Xâu có các kí tự giống hệt nhau thì khoảng cách bằng `0` (truy vấn 3: `"zz"`).
- Hình vòng tròn trong đề chỉ để giúp hình dung, không cần mô phỏng việc di chuyển.

## Phương pháp

1. Lập mảng đếm cộng dồn: `cnt[c][i]` là số lần chữ `c` xuất hiện trong `i` kí tự đầu của `S`.
2. Với mỗi truy vấn `(L, R)`, chữ `c` có mặt khi `cnt[c][R] − cnt[c][L−1] > 0`.
3. Xét mọi cặp chữ có mặt (tối đa 325 cặp) và lấy khoảng cách lớn nhất.

**Kiến thức cần:** xử lý xâu, mảng cộng dồn, công thức khoảng cách trên vòng tròn.

Lời giải chi tiết: [`solutions/LOI_GIAI.md` – Bài 3](../solutions/LOI_GIAI.md#bài-3-khoảng-cách-)
Code: [`solutions/KHOANGCACH.cpp`](../solutions/KHOANGCACH.cpp), [`solutions/KHOANGCACH.py`](../solutions/KHOANGCACH.py)
