# Phân tích đề HSG Tin học lớp 9 Hà Nội 2025–2026

> Đề chính thức, thi ngày 10/01/2026, làm bài trong 150 phút, gồm 5 bài với tổng 20 điểm. Ảnh đề gốc là các file `1.png` đến `4.png` trong thư mục này.
>
> Tài liệu này chỉ **đọc và phân tích đề**: đề cho gì, hỏi gì, người ra đề muốn kiểm tra điều gì, và phương pháp giải đi theo hướng nào. Lời giải chi tiết, có chạy tay ví dụ, nằm ở [`../solutions/LOI_GIAI.md`](../solutions/LOI_GIAI.md).

---

## 1. Tổng quan cấu trúc đề

| STT | Bài | File | Điểm | Dạng bài | Kiến thức trọng tâm | Độ khó |
|---|---|---|---|---|---|---|
| 1 | Chợ Xuân | `CHOXUAN` | 5 | Tính toán | Kiểu dữ liệu, tràn số | ⭐ |
| 2 | Cân bằng | `CANBANG` | 5 | Đếm, tra cứu | Sắp xếp + tìm kiếm nhị phân / set | ⭐⭐ |
| 3 | Khoảng cách | `KHOANGCACH` | 4 | Xâu, truy vấn đoạn | Mảng đếm cộng dồn | ⭐⭐⭐ |
| 4 | Xóa đoạn | `XOADOAN` | 3 | Mảng, đoạn con | Tổng tiền tố, hai con trỏ, deque | ⭐⭐⭐⭐ |
| 5 | Bắn súng | `BANSUNG` | 3 | Mô phỏng, tối ưu | Chặt nhị phân đáp án, cửa sổ trượt | ⭐⭐⭐⭐⭐ |

### Ý đồ của người ra đề
- **Độ khó tăng dần, còn điểm thì giảm dần (5 → 3).** Hai bài dễ nhất chiếm 50% số điểm, nghĩa là đề **ưu tiên phân loại ở mức cơ bản đến khá**. Thí sinh làm chắc Bài 1, 2 đã có 10/20 điểm.
- **Subtask chia rất kỹ.** Bài nào cũng có 2–4 mức ràng buộc. Ở Bài 4 và 5, chỉ cần cách trâu hoặc cách trung bình đã lấy được 60–80% số điểm của bài. Đề thưởng cho người **biết lấy điểm từng phần**, không chỉ cho người giải trọn bài.
- **Kiểm tra kỹ năng thi đấu cơ bản:** đọc/ghi file, chọn kiểu dữ liệu, ước lượng độ phức tạp từ giới hạn N. Lỗi tràn số xuất hiện ở 4 trên 5 bài.
- **Kiến thức nằm trong chương trình bồi dưỡng HSG THCS:** tổng tiền tố, tìm kiếm nhị phân, hai con trỏ. Không cần quy hoạch động hay đồ thị. Hai bài cuối đòi hỏi **kết hợp nhiều kỹ thuật** và có **nhận xét toán học**.

### Phân bổ điểm theo năng lực (ước lượng)

| Mức thí sinh | Làm được | Điểm khoảng |
|---|---|---|
| Biết lập trình cơ bản | Bài 1, Bài 2 subtask 1 (duyệt trâu), Bài 3 subtask 1 | 5 + 3,5 + 2 ≈ **10,5** |
| Khá | Bài 1, 2, 3 trọn; Bài 4 làm cho `A_i ≥ 0`; Bài 5 trâu + công thức K = 1 | 14 + 2,4 + 1,5 ≈ **18** |
| Giỏi | Trọn cả đề | **20** |

Ước lượng này giả định làm đúng hết các subtask nêu trong cột "Làm được".

---

## 2. Phân tích từng bài

Mỗi bài có một file riêng, gồm **đề bài đầy đủ** (chép lại từ ảnh đề), ý nghĩa và mục tiêu của bài, cách đọc subtask để đoán phương pháp, những điểm cần đọc kỹ, và hướng giải.

| Bài | File | Ý chính người ra đề muốn kiểm tra |
|---|---|---|
| 1. Chợ Xuân | [bai1_choxuan.md](bai1_choxuan.md) | Đọc/ghi file, chọn kiểu dữ liệu (`7K` tràn `int`), trường hợp biên |
| 2. Cân bằng | [bai2_canbang.md](bai2_canbang.md) | Chuyển bài đếm thành bài tra cứu, đi từ duyệt trâu đến mảng đánh dấu rồi đến tìm kiếm nhị phân |
| 3. Khoảng cách | [bai3_khoangcach.md](bai3_khoangcach.md) | Mô hình hóa vòng tròn, nhận ra chỉ có 26 chữ cái, mảng đếm cộng dồn |
| 4. Xóa đoạn | [bai4_xoadoan.md](bai4_xoadoan.md) | Biến đổi thành bài "đoạn ngắn nhất có tổng ≥ X", đi từ hai con trỏ đến deque |
| 5. Bắn súng | [bai5_bansung.md](bai5_bansung.md) | Mô phỏng đúng luật, chặt nhị phân đáp án, tối ưu bằng cửa sổ trượt |

---

## 3. Chiến thuật làm bài đề xuất (150 phút)

| Thời gian | Việc | Mục tiêu |
|---|---|---|
| 0–10' | Đọc cả đề, đánh dấu ràng buộc từng subtask | Biết trước bài nào lấy trọn, bài nào lấy từng phần |
| 10–25' | Bài 1 + Bài 2 | Chắc chắn 10 điểm, kiểm tra kỹ `long long` |
| 25–55' | Bài 3 | Ít nhất làm cách trâu (50%), sau đó nâng lên mảng cộng dồn |
| 55–95' | Bài 4 | Làm hai con trỏ cho `A_i ≥ 0` trước (80%), còn thời gian thì làm deque |
| 95–135' | Bài 5 | Viết công thức K = 1 và mô phỏng trâu trước, rồi đến chặt nhị phân |
| 135–150' | Rà soát | Tên file, kiểu dữ liệu, các trường hợp biên (0, −1, N = 1) |

**Nguyên tắc:** viết cách trâu trước, nộp được điểm rồi mới tối ưu. Cách trâu còn dùng để **đối chiếu kết quả** với cách tối ưu trên test nhỏ tự sinh.

---

## 4. Nhận xét chung về đề

- **Điểm mạnh:**
  - Đề phân loại tốt.
  - Subtask chia hợp lý và mỗi subtask là một "bậc thang" kiến thức.
  - Ví dụ minh họa đủ các trường hợp biên (đặc biệt ở Bài 4).
  - Bài 5 có ví dụ mô phỏng từng phát bắn, giúp hiểu luật chính xác.
- **Trọng tâm kiến thức:** tổng tiền tố xuất hiện, trực tiếp hoặc gián tiếp, ở Bài 3, 4, 5. Đây là kỹ thuật cần luyện kỹ nhất.
- **Bẫy chung:** tràn số. Bài 1 có `7K`, Bài 2 có `A_i + K`, Bài 4 có tổng dãy và `S`, Bài 5 có X và tổng sát thương.
- **Mức độ so với mặt bằng:** Bài 1–3 ở mức HSG cấp quận/huyện. Bài 4–5 tiệm cận mức thi vào lớp chuyên Tin, cần đã luyện các dạng "đoạn con" và "chặt nhị phân đáp án".

Xem thêm:
- [`../KIEN_THUC_NEN.md`](../KIEN_THUC_NEN.md): kiến thức nền tảng, có code mẫu.
- [`../solutions/LOI_GIAI.md`](../solutions/LOI_GIAI.md): lời giải chi tiết, có chạy tay ví dụ.
