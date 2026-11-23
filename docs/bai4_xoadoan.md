# Bài 4. Xóa đoạn (3 điểm) ⭐⭐⭐⭐

| Chương trình | Dữ liệu vào | Kết quả ra | Độ khó |
|---|---|---|---|
| `XOADOAN.*` | `XOADOAN.INP` | `XOADOAN.OUT` | Khá khó |

## Đề bài

Cho dãy số nguyên `A` gồm `N` phần tử `A₁, A₂, …, A_N` và số nguyên `S`. Bạn có thể xóa đi một đoạn con liên tiếp bất kỳ trong dãy, tức là chọn hai chỉ số `L, R` với 1 ≤ L ≤ R ≤ N và xóa các phần tử `A_L, A_{L+1}, …, A_R`. **Quy ước:** nếu xóa hết dãy thì tổng còn lại bằng 0.

**Yêu cầu:** tìm độ dài nhỏ nhất của đoạn con cần xóa sao cho tổng các phần tử còn lại của dãy không vượt quá `S`. Nếu không cần xóa đoạn nào thì kết quả là `0`. Nếu không có cách xóa thỏa mãn thì kết quả là `−1`.

**Dữ liệu vào từ file văn bản `XOADOAN.INP`:**
- Dòng đầu tiên chứa số nguyên dương `N` (N ≤ 10⁵).
- Dòng thứ hai chứa `N` số nguyên `A₁, A₂, …, A_N` (|Aᵢ| ≤ 10⁹; 1 ≤ i ≤ N).
- Dòng thứ ba chứa số nguyên `S` (|S| ≤ 10¹⁴).

**Kết quả ghi ra file văn bản `XOADOAN.OUT`:** gồm một số nguyên là kết quả của bài toán.

**Ví dụ:**

| XOADOAN.INP | XOADOAN.OUT | Giải thích |
|---|---|---|
| 5<br>4 −5 4 4 −2<br>0 | 2 | Tổng dãy ban đầu là 5, cần tổng dãy nhỏ hơn hoặc bằng 0. Có thể xóa đoạn [3, 4] có tổng là 8, khi đó tổng còn lại là 5 − 8 = −3 ≤ 0. Kết quả là 2. |
| 3<br>4 2 1<br>0 | 3 | Tổng dãy ban đầu là 7, cần tổng dãy nhỏ hơn hoặc bằng 0. Có thể xóa đoạn [1, 3] có tổng là 7, khi đó tổng còn lại là 7 − 7 = 0 ≤ 0. Kết quả là 3. |
| 3<br>1 2 3<br>−2 | −1 | Tổng dãy ban đầu là 6, cần tổng dãy nhỏ hơn hoặc bằng −2. Không có cách xóa thỏa mãn. |
| 3<br>1 2 0<br>5 | 0 | Tổng dãy ban đầu là 3, cần tổng dãy nhỏ hơn hoặc bằng 5. Không cần xóa đoạn nào. |

**Ràng buộc:**
- Có 40% số test ứng với 40% số điểm có N ≤ 100; Aᵢ ≥ 0.
- 20% số test tiếp theo ứng với 20% số điểm có N ≤ 5000; Aᵢ ≥ 0.
- 20% số test tiếp theo ứng với 20% số điểm có Aᵢ ≥ 0.
- 20% số test còn lại ứng với 20% số điểm không có ràng buộc gì thêm.

---

## Phân tích

### Đề cho gì, hỏi gì
- **Cho:** dãy `A` (có thể có số âm) và ngưỡng `S` (có thể âm).
- **Hỏi:** đoạn liên tiếp ngắn nhất cần xóa để tổng phần còn lại ≤ `S`.

### Ý nghĩa và mục tiêu
Mấu chốt của bài là **biến đổi đề bài**. Gọi `T` là tổng cả dãy. Xóa đoạn có tổng `X` thì phần còn lại có tổng `T − X`, và:

```
T − X ≤ S   ⟺   X ≥ T − S
```

Vậy bài toán trở thành bài kinh điển: **tìm đoạn con ngắn nhất có tổng ≥ need**, với `need = T − S`.

Sau bước biến đổi, đề phân loại thí sinh theo mức hiểu về **bài toán đoạn con**:
1. Biết dùng **tổng tiền tố** để tính tổng đoạn trong O(1).
2. Biết **hai con trỏ**, và hiểu cách này chỉ đúng khi dãy **không âm** (mở rộng đoạn thì tổng tăng).
3. Biết xử lý dãy **có số âm** bằng **deque đơn điệu**.

### Đọc subtask để đoán phương pháp

| Subtask | Ràng buộc | Phương pháp gợi ý | Độ phức tạp |
|---|---|---|---|
| 40% | N ≤ 100; Aᵢ ≥ 0 | Thử mọi đoạn, cộng trực tiếp | O(N³) |
| 20% | N ≤ 5000; Aᵢ ≥ 0 | Tổng tiền tố + thử mọi cặp (L, R) | O(N²) |
| 20% | Aᵢ ≥ 0 (N tới 10⁵) | Hai con trỏ | O(N) |
| 20% | Không ràng buộc (có số âm) | Tổng tiền tố + deque đơn điệu | O(N) |

**Ba subtask đầu (80% số điểm) đều có `Aᵢ ≥ 0`.** Đây là tín hiệu rõ ràng rằng số âm mới là thứ làm bài khó lên. Thí sinh không biết deque vẫn lấy được 2,4/3 điểm.

### Điểm cần đọc kỹ
- **Bốn ví dụ ứng với bốn tình huống đầu ra**, và người ra đề cố ý nhắc thí sinh xử lý đủ:
  - xóa một đoạn ngắn (đáp án 2), trong đó dãy có số âm;
  - phải xóa cả dãy (đáp án 3 = N), dùng quy ước tổng còn lại bằng 0;
  - không thể xóa (đáp án −1), vì `S` âm trong khi xóa hết cũng chỉ đưa tổng về 0;
  - không cần xóa (đáp án 0), vì ngay từ đầu `T ≤ S`.
- Đoạn bị xóa phải **liên tiếp**, và chỉ được xóa **một** đoạn.
- `|S| ≤ 10¹⁴` và tổng dãy tới 10¹⁴, nên mọi tổng phải dùng `long long`.

## Phương pháp

1. Tính `T`. Nếu `T ≤ S` thì in `0`.
2. Đặt `need = T − S`. Tính tổng tiền tố `p[0..N]`.
3. Tìm `r − l` nhỏ nhất sao cho `p[r] − p[l] ≥ need`, bằng một deque chứa các chỉ số có `p` tăng dần:
   - khi `p[r] − p[đầu] ≥ need`: cập nhật đáp án rồi bỏ đầu ra;
   - khi `p[cuối] ≥ p[r]`: bỏ cuối ra;
   - đẩy `r` vào cuối.
4. Không tìm được đoạn nào thì in `−1`.

**Kiến thức cần:** tổng tiền tố, hai con trỏ, deque đơn điệu, kiểu `long long`.

Lời giải chi tiết, có chạy tay deque: [`solutions/LOI_GIAI.md` – Bài 4](../solutions/LOI_GIAI.md#bài-4-xóa-đoạn-)
Code: [`solutions/XOADOAN.cpp`](../solutions/XOADOAN.cpp), [`solutions/XOADOAN.py`](../solutions/XOADOAN.py)
