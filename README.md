# Đề HSG Tin học lớp 9 Hà Nội 2025–2026

Lời giải và bộ test cho đề thi chọn học sinh giỏi lớp 9 cấp thành phố Hà Nội, môn Tin học, thi ngày 10/01/2026.

## Danh sách bài

| STT | Tên bài | File | Điểm | Độ khó | Ý tưởng chính |
|---|---|---|---|---|---|
| 1 | Chợ Xuân | `CHOXUAN` | 5 | ⭐ | Tính `N − 7K`, chú ý tràn số |
| 2 | Cân bằng | `CANBANG` | 5 | ⭐⭐ | Set hoặc sắp xếp + tìm kiếm nhị phân |
| 3 | Khoảng cách | `KHOANGCACH` | 4 | ⭐⭐⭐ | Mảng đếm cộng dồn cho 26 chữ cái |
| 4 | Xóa đoạn | `XOADOAN` | 3 | ⭐⭐⭐⭐ | Tổng tiền tố + deque đơn điệu |
| 5 | Bắn súng | `BANSUNG` | 3 | ⭐⭐⭐⭐⭐ | Chặt nhị phân X + cửa sổ trượt |

Tài liệu kèm theo:
- Lời giải chi tiết từng bài, có chạy tay ví dụ và hướng làm từng subtask: **[solutions/LOI_GIAI.md](solutions/LOI_GIAI.md)**
- Kiến thức nền tảng cần nắm, có code mẫu và lộ trình học: **[KIEN_THUC_NEN.md](KIEN_THUC_NEN.md)**

## Cấu trúc thư mục

```
hsg_lop9/
├── docs/              Ảnh đề thi (4 trang)
├── solutions/         Lời giải: mỗi bài có bản .cpp và .py
│   └── LOI_GIAI.md    Giải thích chi tiết
├── KIEN_THUC_NEN.md   Kiến thức nền tảng
├── tests/             Bộ test theo định dạng Themis
│   └── <TÊNBÀI>/TestXX/<TÊNBÀI>.INP, .OUT
└── gen_tests.py       Script sinh lại bộ test
```

## Chạy lời giải

Chương trình đọc file `<TÊNBÀI>.INP` và ghi file `<TÊNBÀI>.OUT` trong **thư mục hiện tại**.

**C++** (cần g++ 64-bit hỗ trợ `__int128`, ví dụ bản đi kèm Code::Blocks hoặc Dev-C++ mới):
```bash
g++ -O2 -std=c++17 BANSUNG.cpp -o BANSUNG
./BANSUNG
```

**Python 3:**
```bash
python BANSUNG.py
```

## Bộ test

Có 90 test, chia theo đúng tỉ lệ điểm từng subtask trong đề:

| Bài | Số test | Chia theo subtask |
|---|---|---|
| CHOXUAN | 10 | – |
| CANBANG | 20 | 14 / 4 / 2 |
| KHOANGCACH | 20 | 10 / 4 / 4 / 2 |
| XOADOAN | 20 | 8 / 4 / 4 / 4 |
| BANSUNG | 20 | 6 / 4 / 6 / 4 |

- Các test đầu của mỗi subtask là ví dụ trong đề và các trường hợp biên. Các test sau là test ngẫu nhiên, test lớn nhất nằm cuối.
- Đáp án được tính bằng lời giải trong `solutions/`.
- Các test nhỏ được đối chiếu thêm với lời giải duyệt trâu.

**Chấm bằng Themis:** chọn thư mục `tests/<TÊNBÀI>` làm thư mục đề, so sánh output bỏ qua khoảng trắng.

**Sinh lại bộ test** (seed cố định nên kết quả luôn giống nhau):
```bash
python gen_tests.py            # sinh tất cả các bài
python gen_tests.py BANSUNG    # chỉ sinh một bài
```
