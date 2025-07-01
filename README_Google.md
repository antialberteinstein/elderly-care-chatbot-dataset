# 🤖 Tool Sinh Câu Hỏi - Trả Lời Chăm Sóc Người Cao Tuổi

Tool tự động sinh câu hỏi và câu trả lời cho chăm sóc người cao tuổi sử dụng **Google Gemini API**.

## ⚡ Tính năng chính

- ✅ **Miễn phí** - Sử dụng Google Gemini API (miễn phí)
- 🎯 **12 chủ đề chuyên biệt** cho người cao tuổi
- 💾 **Tự động backup** sau mỗi 500 dòng dữ liệu
- 📊 **Xuất file CSV** với 2 cột: input và output
- 🔄 **Sinh dataset lớn** (1000+ cặp Q&A)

## 📋 Các chủ đề

1. **Nhắc nhở hằng ngày** - Uống thuốc, lịch tái khám, ăn uống
2. **Chăm sóc sức khỏe** - Dinh dưỡng, triệu chứng, thuốc men
3. **Sức khỏe tinh thần** - Giấc ngủ, giải trí, tâm sự
4. **Giao tiếp & cảm xúc** - Trò chuyện, kể chuyện, lắng nghe
5. **Nấu ăn & bếp núc** - Thực đơn, mẹo nấu ăn, bảo quản
6. **Việc nhà** - Dọn dẹp, sắp xếp, mẹo vặt
7. **Giải trí** - Phim, cải lương, trò chơi, truyện cười
8. **Tâm linh & truyền thống** - Lễ nghi, Tết, dân gian
9. **Quan hệ gia đình** - Con cháu, yêu thương, dạy con
10. **Công nghệ** - Điện thoại, Zalo, chống lừa đảo
11. **Thông báo tự động** - Nhắc lịch, chào hỏi, thời tiết
12. **FAQ** - Câu hỏi thường gặp về sức khỏe

## 🚀 Cài đặt & Sử dụng

### 1. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 2. Lấy Google Gemini API Key
1. Truy cập: https://aistudio.google.com/app/apikey
2. Đăng nhập Google account
3. Click "Create API Key"
4. Copy API key

### 3. Cấu hình API Key
Cập nhật file `.env`:
```env
# Cấu hình Google Gemini API
GOOGLE_API_KEY=your_actual_api_key_here
```

### 4. Kiểm tra kết nối
```bash
python check_google_api.py
```

### 5. Chạy demo
```bash
python demo_google.py
```

### 6. Chạy tool chính
```bash
python generator_google.py
```

## 📝 Cách sử dụng

### Sinh dataset lớn (tự động)
```python
from generator_google import QAGenerator

generator = QAGenerator()
generator.generate_dataset(total_pairs=1000, backup_interval=500)
```

### Sinh theo chủ đề cụ thể
```python
# Sinh 20 cặp Q&A cho chủ đề "Nhắc nhở hằng ngày"
qa_pairs = generator.generate_qa_pairs("1", 20)
generator.save_to_csv(qa_pairs, "topic1_qa.csv")
```

## 📊 Định dạng Output

File CSV có 2 cột:
- **input**: Câu hỏi hoặc phát biểu của người dùng
- **output**: Câu trả lời chi tiết của AI

Ví dụ:
```csv
input,output
"Tôi nên uống thuốc huyết áp lúc nào?","Cô/Chú nên uống thuốc huyết áp vào buổi sáng sau khi ăn sáng khoảng 30 phút. Điều này giúp thuốc phát huy tác dụng tốt nhất..."
"Làm sao để nhớ uống thuốc đều đặn?","Có một số cách để nhớ uống thuốc: 1) Đặt báo thức điện thoại, 2) Để thuốc ở nơi dễ thấy..."
```

## 📁 Cấu trúc file

- `generator_google.py` - Tool chính
- `check_google_api.py` - Kiểm tra API
- `demo_google.py` - Demo nhanh
- `.env` - Cấu hình API key
- `requirements.txt` - Thư viện cần thiết

## ⚠️ Lưu ý

- Tool **miễn phí** với Google Gemini API
- **Tự động backup** sau mỗi 500 cặp Q&A
- **Rate limit**: Nghỉ 1 giây giữa các request
- Dữ liệu sinh ra bằng **tiếng Việt**
- Phù hợp với **người cao tuổi Việt Nam**

## 🎯 Ví dụ Output

```
INPUT: Tôi bị đau đầu, có nên uống thuốc paracetamol không?
OUTPUT: Cô/Chú có thể uống paracetamol nếu đau đầu nhẹ, liều dùng 500mg mỗi lần, cách 6-8 tiếng uống một lần. Tuy nhiên, nếu đau đầu kéo dài hoặc có triệu chứng khác như buồn nôn, hoa mắt, Cô/Chú nên đến bệnh viện khám để bác sĩ tư vấn chính xác nhé.

INPUT: Làm sao để ngủ ngon hơn?
OUTPUT: Để có giấc ngủ ngon, Cô/Chú nên: 1) Đi ngủ và thức dậy đúng giờ, 2) Tránh uống cà phê sau 2h chiều, 3) Tắm nước ấm trước khi ngủ, 4) Đọc sách hoặc nghe nhạc nhẹ nhàng, 5) Đảm bảo phòng ngủ tối và mát mẻ. Tránh xem TV hoặc dùng điện thoại trước khi ngủ 1 tiếng nhé.
```

## 🔧 Troubleshooting

### Lỗi API Key
```
❌ Không tìm thấy GOOGLE_API_KEY trong file .env
```
**Giải pháp**: Kiểm tra file `.env` và API key

### Lỗi kết nối
```
❌ Lỗi khi kết nối Google Gemini API
```
**Giải pháp**: Kiểm tra internet và API key hợp lệ

## 📞 Hỗ trợ

Nếu gặp vấn đề, hãy:
1. Chạy `python check_google_api.py` để kiểm tra
2. Xem log lỗi chi tiết
3. Đảm bảo API key đúng

---
🎉 **Chúc bạn sử dụng tool thành công!**
