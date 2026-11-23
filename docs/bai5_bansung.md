# Bài 5. Bắn súng (3 điểm) ⭐⭐⭐⭐⭐

| Chương trình | Dữ liệu vào | Kết quả ra | Độ khó |
|---|---|---|---|
| `BANSUNG.*` | `BANSUNG.INP` | `BANSUNG.OUT` | Khó |

## Đề bài

Trong một buổi tập bắn súng, có `N` tấm bia được xếp thành một hàng dọc, đánh số từ 1 tới `N`. Độ bền của các tấm bia được mô tả bởi dãy số `A`: tấm bia thứ `i` có độ bền ban đầu là `Aᵢ`. Một tấm bia được coi là bị phá hủy nếu độ bền của nó giảm xuống nhỏ hơn hoặc bằng 0 (khi này coi độ bền của tấm bia là 0).

Xạ thủ được quyền chọn một loại đạn có sức công phá `X` (với `X` là số nguyên dương tùy ý) để sử dụng cho toàn bộ buổi tập. Mỗi lần bắn, xạ thủ bắn một viên đạn thẳng dọc theo hàng các tấm bia. Viên đạn sẽ trúng tấm bia đầu tiên chưa bị phá hủy, tức là tấm bia thứ `i` có chỉ số nhỏ nhất và độ bền `Aᵢ > 0`. Do đạn có tính xuyên phá nên viên đạn gây ảnh hưởng lên tấm bia thứ `i` và các tấm bia thứ `j` phía sau nó (`j ≥ i`). Độ bền của tấm bia thứ `j` (i ≤ j ≤ N) bị giảm một lượng theo công thức:

```
max(0, X − (j − i)²)
```

**Ví dụ:** với `X = 5` và 6 tấm bia có độ bền lần lượt là `[0, 2, 5, 0, 1, 2]`. Viên đạn đầu tiên trúng vào tấm bia thứ 2 và gây ảnh hưởng lên các tấm bia thứ 2, 3, 5, 6 (vì tấm bia 1 và 4 có độ bền bằng 0). Độ bền của các tấm bia bị giảm như sau:
- Tấm bia thứ 2: max(0, 5 − (2 − 2)²) = max(0, 5 − 0²) = 5.
- Tấm bia thứ 3: max(0, 5 − (3 − 2)²) = max(0, 5 − 1²) = 4.
- Tấm bia thứ 5: max(0, 5 − (5 − 2)²) = max(0, 5 − 3²) = 0.
- Tấm bia thứ 6: max(0, 5 − (6 − 2)²) = max(0, 5 − 4²) = 0.

Vậy sau lượt bắn này, độ bền của các tấm bia là `[0, 0, 1, 0, 1, 2]`.

**Yêu cầu:** hãy tìm giá trị sức công phá `X` nhỏ nhất sao cho xạ thủ có thể phá hủy toàn bộ các tấm bia khi bắn không quá `K` lần.

**Dữ liệu vào từ file văn bản `BANSUNG.INP`:**
- Dòng đầu chứa hai số nguyên dương `N, K` (N ≤ 2·10⁵; K ≤ 10⁹), lần lượt là số tấm bia và số lần bắn tối đa.
- Dòng tiếp theo chứa `N` số nguyên dương mô tả dãy `A` (Aᵢ ≤ 10⁹; 1 ≤ i ≤ N).

**Kết quả ghi ra file văn bản `BANSUNG.OUT`:** gồm một số nguyên dương `X` nhỏ nhất tìm được.

**Ví dụ:**

| BANSUNG.INP | BANSUNG.OUT |
|---|---|
| 6 3<br>6 7 1 3 2 1 | 5 |
| 3 1<br>3 7 3 | 8 |

**Giải thích ví dụ 1:** chọn `X = 5`.
- **Lần bắn thứ nhất:** tấm bia `i` đầu tiên có `Aᵢ > 0` là tấm bia 1.
  - Sức công phá gây lên tấm bia 1 là max(0, 5 − (1 − 1)²) = 5.
  - Sức công phá gây lên tấm bia 2 là max(0, 5 − (2 − 1)²) = 4.
  - Tương tự, sức công phá gây lên các tấm bia thứ 3, 4, 5, 6 lần lượt là 1, 0, 0, 0.
  - Độ bền còn lại là `A = [1, 3, 0, 3, 2, 1]`.
- **Lần bắn thứ hai:** tấm bia đầu tiên có `Aᵢ > 0` vẫn là tấm bia 1.
  - Sức công phá lên các tấm bia thứ 1, 2, 4, 5, 6 lần lượt là 5, 4, 0, 0, 0.
  - Độ bền còn lại là `A = [0, 0, 0, 3, 2, 1]`.
- **Lần bắn thứ ba:** tấm bia đầu tiên có `Aᵢ > 0` là tấm bia 4. Sức công phá lên các tấm bia thứ 4, 5, 6 lần lượt là 5, 4, 1. Khi này tất cả các tấm bia đều bị phá hủy.

**Ràng buộc:**
- Có 30% số test ứng với 30% số điểm có N, K ≤ 30; Aᵢ ≤ 30.
- 20% số test tiếp theo ứng với 20% số điểm có K = 1.
- 30% số test tiếp theo ứng với 30% số điểm có N ≤ 1000.
- 20% số test còn lại ứng với 20% số điểm không có ràng buộc gì thêm.

---

## Phân tích

### Đề cho gì, hỏi gì
- **Cho:** độ bền `N` tấm bia và số phát tối đa `K`.
- **Hỏi:** sức công phá `X` nhỏ nhất để phá hết bia trong không quá `K` phát.

### Ý nghĩa và mục tiêu
Đây là bài phân loại thí sinh giỏi nhất. Bài kiểm tra ba tầng kỹ năng:

1. **Đọc hiểu và mô phỏng đúng luật chơi.** Đạn **tự động** trúng bia sống đầu tiên, người bắn không được chọn bia. Vì vậy với mỗi `X`, quá trình bắn là **tất định**: duyệt bia từ trái sang phải, gặp bia `i` còn độ bền `rem > 0` thì bắt buộc phải bắn vào nó đúng `⌈rem / X⌉` phát.
2. **Nhận ra tính đơn điệu và chặt nhị phân đáp án.** `X` càng lớn thì càng cần ít phát. Đề hỏi "giá trị **nhỏ nhất** sao cho…" là dấu hiệu quen thuộc của **chặt nhị phân theo đáp án**: chỉ cần viết hàm `check(X)` kiểm tra "với X này có phá hết bia trong ≤ K phát không".
3. **Tối ưu mô phỏng.** Mỗi phát ảnh hưởng tới khoảng √X bia phía sau, nên cập nhật từng bia một là quá chậm. Phải giữ tổng sát thương bằng **cửa sổ trượt**, và dùng biến đổi đại số `(d + 1)² = d² + 2d + 1` để cập nhật trong O(1) mỗi bước.

### Đọc subtask để đoán phương pháp

| Subtask | Ràng buộc | Phương pháp gợi ý | Độ phức tạp |
|---|---|---|---|
| 30% | N, K ≤ 30; Aᵢ ≤ 30 | Thử X = 1, 2, 3, … và mô phỏng từng phát | Nhỏ, chạy kịp |
| 20% | K = 1 | **Công thức:** X = max(Aⱼ + (j − 1)²) | O(N) |
| 30% | N ≤ 1000 | Chặt nhị phân X + mô phỏng trực tiếp | O(N² log X) |
| 20% | Không ràng buộc | Chặt nhị phân X + mô phỏng bằng cửa sổ trượt | O(N log X) |

**Subtask K = 1 là phần thưởng cho tư duy toán học.** Chỉ có một phát và phát đó trúng bia 1. Bia thứ `j` nhận `X − (j − 1)²` sát thương, nên cần `X ≥ Aⱼ + (j − 1)²` với mọi `j`. Không cần chặt nhị phân hay mô phỏng mà vẫn được 0,6 điểm.

### Điểm cần đọc kỹ
- Đạn trúng bia **chưa bị phá có chỉ số nhỏ nhất**. Đây là chi tiết quan trọng nhất của bài: hiểu nhầm thành "được chọn bia để bắn" thì bài toán khác hẳn.
- Sát thương chỉ tác động lên các bia **phía sau** (`j ≥ i`), không tác động ngược về trước. Bia cách quá xa (`(j − i)² ≥ X`) thì không bị ảnh hưởng.
- `X` dùng **chung cho mọi phát**, chọn một lần từ đầu.
- Ví dụ minh họa có bia độ bền 0 (`[0, 2, 5, 0, 1, 2]`) để làm rõ luật "bỏ qua bia đã bị phá". Tuy vậy, dữ liệu vào thật có `Aᵢ ≥ 1`.
- `X` có thể tới khoảng `max(A) + (N − 1)² ≈ 4·10¹⁰`, nên cận chặt nhị phân và các biến phải dùng `long long`. Nếu tính tổng sát thương theo vị trí tuyệt đối của bia thì có thể **tràn cả `long long`**. Phải tính theo khoảng cách (xem lời giải).

## Phương pháp

1. **Chặt nhị phân** `X` trong đoạn `[1, max(A) + (N − 1)²]`.
2. **Hàm `check(X)`:**
   - duyệt bia từ trái sang phải;
   - giữ ba tổng `s0 = Σc`, `t1 = Σc·d`, `t2 = Σc·d²` của các phát còn tác dụng (với `d` là khoảng cách từ chỗ bắn tới bia đang xét);
   - sát thương lên bia hiện tại bằng `X·s0 − t2`;
   - nếu bia còn sống thì bắn `⌈rem / X⌉` phát, và dừng ngay khi tổng số phát vượt `K`.
3. In `X` nhỏ nhất mà `check(X)` cho kết quả đúng.

**Kiến thức cần:** chặt nhị phân đáp án, mô phỏng, cửa sổ trượt, biến đổi đại số, kiểu `long long`.

Lời giải chi tiết, có chạy tay X = 5 và X = 4: [`solutions/LOI_GIAI.md` – Bài 5](../solutions/LOI_GIAI.md#bài-5-bắn-súng-)
Code: [`solutions/BANSUNG.cpp`](../solutions/BANSUNG.cpp), [`solutions/BANSUNG.py`](../solutions/BANSUNG.py)
