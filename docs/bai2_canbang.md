# Bài 2. Cân bằng (5 điểm) ⭐⭐

| Chương trình | Dữ liệu vào | Kết quả ra | Độ khó |
|---|---|---|---|
| `CANBANG.*` | `CANBANG.INP` | `CANBANG.OUT` | Dễ |

## Đề bài

Cho dãy số nguyên `A` gồm `N` phần tử phân biệt `A₁, A₂, …, A_N` và số nguyên dương `K`. Phần tử `Aᵢ` được gọi là **"cân bằng K"** nếu trong dãy xuất hiện phần tử có giá trị bằng `Aᵢ + K` và `Aᵢ − K`. Ví dụ, dãy số `5, 2, 4, 6` với `K = 1` có phần tử 5 là cân bằng K, vì dãy có phần tử `5 − 1 = 4` và `5 + 1 = 6`.

**Yêu cầu:** đếm số lượng phần tử "cân bằng K" của dãy số `A`.

**Dữ liệu vào từ file văn bản `CANBANG.INP`:**
- Dòng đầu tiên chứa hai số nguyên dương `N` và `K` (N ≤ 10⁵; K ≤ 10⁹).
- Dòng thứ hai chứa `N` số nguyên `A₁, A₂, …, A_N` (|Aᵢ| ≤ 10⁹; 1 ≤ i ≤ N).

**Kết quả ghi ra file văn bản `CANBANG.OUT`:** gồm một số nguyên là kết quả của bài toán.

**Ví dụ:**

| CANBANG.INP | CANBANG.OUT | Giải thích |
|---|---|---|
| 6 1<br>4 1 7 8 5 6 | 3 | Có 3 phần tử là 5, 6 và 7 là "cân bằng K". |
| 6 2<br>4 −1 7 8 5 6 | 1 | Có 1 phần tử 6 là "cân bằng K". |

**Ràng buộc:**
- Có 70% số test ứng với 70% số điểm có K = 1; N ≤ 10³ và 0 ≤ Aᵢ ≤ 10³.
- 20% số test tiếp theo ứng với 20% số điểm có K = 1; 0 ≤ Aᵢ ≤ 10⁶.
- 10% số test còn lại ứng với 10% số điểm không có ràng buộc gì thêm.

---

## Phân tích

### Đề cho gì, hỏi gì
- **Cho:** dãy `N` số **phân biệt** và số `K`.
- **Hỏi:** có bao nhiêu `x` trong dãy mà **cả** `x − K` **và** `x + K` đều có trong dãy.

### Ý nghĩa và mục tiêu
Bài kiểm tra khả năng **chuyển bài toán đếm thành bài toán tra cứu**: với mỗi phần tử, ta chỉ phải trả lời hai câu hỏi "giá trị v có trong dãy không?". Điểm phân loại nằm ở chỗ **trả lời câu hỏi này nhanh đến đâu**:
- duyệt cả dãy để tìm, mất O(N) mỗi lần hỏi;
- dùng mảng đánh dấu, mất O(1) nhưng chỉ dùng được khi giá trị nhỏ và không âm;
- dùng tìm kiếm nhị phân hoặc set, mất O(log N) và dùng được với mọi giá trị.

### Đọc subtask để đoán phương pháp

| Subtask | Ràng buộc | Phương pháp gợi ý | Độ phức tạp |
|---|---|---|---|
| 70% | K = 1; N ≤ 10³; 0 ≤ Aᵢ ≤ 10³ | Duyệt hai vòng lặp, hoặc mảng đánh dấu `co[v]` | O(N²) |
| 20% | K = 1; 0 ≤ Aᵢ ≤ 10⁶ | Mảng đánh dấu cỡ 10⁶ | O(N + 10⁶) |
| 10% | Không ràng buộc | Giá trị tới ±10⁹ nên không làm được mảng đánh dấu. Dùng **sắp xếp + tìm kiếm nhị phân**, hoặc **set** | O(N log N) |

Người ra đề cố ý dẫn dắt theo ba bậc: **duyệt trâu**, rồi **mảng đánh dấu**, rồi **tìm kiếm nhị phân / set**. Riêng subtask đầu đã chiếm 70% số điểm, nên chỉ cần hai vòng lặp là được 3,5 điểm.

### Điểm cần đọc kỹ
- Các phần tử **phân biệt**, nên đếm không lo trùng lặp.
- Phải có **cả hai** giá trị `x + K` và `x − K`, không phải chỉ một trong hai.
- `x + K` có thể bằng 2·10⁹, vượt `int`.
- Ví dụ 2 có số âm (`−1`) và K = 2, nhắc rằng subtask cuối bỏ hết các giả thiết `K = 1` và `Aᵢ ≥ 0`.

## Phương pháp

1. Sắp xếp một bản sao `b` của dãy.
2. Với mỗi `x` trong dãy, dùng `binary_search` để kiểm tra `x − K` và `x + K` có trong `b` không.
3. Đếm số phần tử thỏa mãn cả hai điều kiện.

Độ phức tạp O(N log N). Với Python, dùng `set` thì mỗi lần kiểm tra trung bình mất O(1).

**Kiến thức cần:** sắp xếp, tìm kiếm nhị phân hoặc set, kiểu `long long`.

Lời giải chi tiết: [`solutions/LOI_GIAI.md` – Bài 2](../solutions/LOI_GIAI.md#bài-2-cân-bằng-)
Code: [`solutions/CANBANG.cpp`](../solutions/CANBANG.cpp), [`solutions/CANBANG.py`](../solutions/CANBANG.py)
