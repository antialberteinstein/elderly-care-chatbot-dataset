"""
Tool tự động sinh câu hỏi và câu trả lời cho chăm sóc người cao tuổi
Sử dụng Google Gemini API
"""
import os
import csv
import time
import random
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Tải cấu hình từ file .env
load_dotenv()

class QAGenerator:
    def __init__(self):
        """Khởi tạo QA Generator với Google Gemini API"""
        self.api_key = os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("❌ Không tìm thấy GOOGLE_API_KEY trong file .env")
        
        # Cấu hình Google Gemini
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        print("✅ Đã kết nối thành công với Google Gemini API")
        
        # Danh sách chủ đề
        self.topics = {
            "1": "Nhắc nhở hằng ngày (uống thuốc, lịch tái khám, giờ ăn, uống nước, tập thể dục)",
            "2": "Chăm sóc sức khỏe (dinh dưỡng, triệu chứng bệnh, lời khuyên y tế, thuốc, vật lý trị liệu)",
            "3": "Sức khỏe tinh thần (cải thiện giấc ngủ, giải trí, tâm sự, hoạt động phấn chấn)",
            "4": "Giao tiếp & hỗ trợ cảm xúc (trò chuyện, kể chuyện, lắng nghe, tương tác thân thiện)",
            "5": "Đi chợ, nấu ăn, bếp núc (thực đơn, mẹo nấu ăn, bảo quản thực phẩm, mua hàng)",
            "6": "Việc nhà (dọn dẹp, sắp xếp đồ đạc, mẹo vặt gia đình)",
            "7": "Giải trí (phim, cải lương, sách, trò chơi, truyện cười)",
            "8": "Tâm linh – truyền thống (lễ nghi, cúng giỗ, Tết, chuyện dân gian, ca dao)",
            "9": "Quan hệ gia đình (gọi điện con cháu, lời yêu thương, dạy con cháu)",
            "10": "Công nghệ (điện thoại, Zalo, video call, tin lừa đảo, chatbot)",
            "11": "Thông báo tự động (nhắc lịch, chào buổi sáng/tối, thời tiết)",
            "12": "Câu hỏi thường gặp (ăn uống, sức khỏe, đau nhức)"
        }

    def generate_qa_pairs(self, topic_key, num_pairs=10):
        """Sinh câu hỏi và câu trả lời cho một chủ đề"""
        topic = self.topics.get(topic_key, "Chăm sóc người cao tuổi tổng quát")
        
        prompt = f"""
Bạn là một trợ lý AI tạo dataset để huấn luyện chatbot chăm sóc người cao tuổi. Hãy tạo {num_pairs} cặp dữ liệu về chủ đề: {topic}

Yêu cầu:
- INPUT: Là những câu nói, câu hỏi, thắc mắc, phàn nàn của NGƯỜI CAO TUỔI VIỆT NAM
- OUTPUT: Là câu trả lời của CHATBOT - thân thiện, hữu ích, chi tiết
- Người cao tuổi sẽ nói về các vấn đề của họ, chatbot cần trả lời phù hợp
- Sử dụng ngôn ngữ Việt Nam, thân thiện, gần gụi
- INPUT phải thật tự nhiên như người già thực sự nói

Ví dụ về chủ đề {topic}:
- INPUT có thể là: "Tôi quên uống thuốc mất rồi", "Đau đầu quá", "Không biết nấu gì hôm nay"
- OUTPUT: Chatbot sẽ tư vấn, an ủi, đưa ra lời khuyên cụ thể

Định dạng output:
INPUT: [câu nói/hỏi của người cao tuổi]
OUTPUT: [câu trả lời của chatbot]
---
INPUT: [câu nói/hỏi tiếp theo của người cao tuổi]
OUTPUT: [câu trả lời của chatbot]
---
(tiếp tục...)
"""

        try:
            print(f"🔄 Đang sinh {num_pairs} cặp Q&A cho chủ đề: {topic}")
            response = self.model.generate_content(prompt)
            return self.parse_qa_response(response.text)
        except Exception as e:
            print(f"❌ Lỗi khi sinh Q&A: {e}")
            return []

    def parse_qa_response(self, response_text):
        """Phân tích response và trích xuất các cặp Q&A"""
        qa_pairs = []
        blocks = response_text.split('---')
        
        for block in blocks:
            lines = block.strip().split('\n')
            input_text = ""
            output_text = ""
            
            for line in lines:
                line = line.strip()
                if line.startswith('INPUT:'):
                    input_text = line[6:].strip()
                elif line.startswith('OUTPUT:'):
                    output_text = line[7:].strip()
                elif output_text and line:  # Tiếp tục output nếu có nhiều dòng
                    output_text += " " + line
            
            if input_text and output_text:
                qa_pairs.append({
                    'input': input_text,
                    'output': output_text
                })
        
        return qa_pairs

    def save_to_csv(self, qa_pairs, filename=None):
        """Lưu dữ liệu vào file CSV"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"qa_data_{timestamp}.csv"
        
        file_exists = os.path.exists(filename)
        
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['input', 'output']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Chỉ ghi header nếu file mới
            if not file_exists:
                writer.writeheader()
            
            for qa in qa_pairs:
                writer.writerow(qa)
        
        print(f"💾 Đã lưu {len(qa_pairs)} cặp Q&A vào {filename}")
        return filename

    def generate_dataset(self, total_pairs=1000, backup_interval=500):
        """Sinh dataset lớn với backup định kỳ"""
        print(f"🚀 Bắt đầu sinh dataset {total_pairs} cặp Q&A")
        print(f"📁 Sao lưu sau mỗi {backup_interval} cặp")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        main_filename = f"elderly_care_qa_{timestamp}.csv"
        
        total_generated = 0
        all_qa_pairs = []
        
        while total_generated < total_pairs:
            # Chọn chủ đề ngẫu nhiên
            topic_key = random.choice(list(self.topics.keys()))
            batch_size = min(10, total_pairs - total_generated)
            
            # Sinh Q&A cho chủ đề này
            qa_pairs = self.generate_qa_pairs(topic_key, batch_size)
            
            if qa_pairs:
                all_qa_pairs.extend(qa_pairs)
                total_generated += len(qa_pairs)
                
                print(f"✅ Đã sinh {total_generated}/{total_pairs} cặp Q&A")
                
                # Backup định kỳ
                if len(all_qa_pairs) >= backup_interval:
                    backup_filename = f"backup_{len(all_qa_pairs)}_{timestamp}.csv"
                    self.save_to_csv(all_qa_pairs, backup_filename)
                    all_qa_pairs = []  # Reset để tiết kiệm memory
                
                # Nghỉ ngắn để tránh rate limit
                time.sleep(1)
            else:
                print("⚠️ Không sinh được Q&A, thử lại...")
                time.sleep(2)
        
        # Lưu phần còn lại
        if all_qa_pairs:
            self.save_to_csv(all_qa_pairs, main_filename)
        
        print(f"🎉 Hoàn thành! Đã sinh tổng cộng {total_generated} cặp Q&A")

    def test_connection(self):
        """Test kết nối API"""
        try:
            response = self.model.generate_content("Chào bạn!")
            print(f"✅ Test thành công: {response.text[:50]}...")
            return True
        except Exception as e:
            print(f"❌ Test thất bại: {e}")
            return False

def main():
    """Hàm main để chạy tool"""
    try:
        # Khởi tạo generator
        generator = QAGenerator()
        
        # Test kết nối
        if not generator.test_connection():
            return
        
        print("\n" + "="*60)
        print("🤖 TOOL SINH CÂU HỎI - TRẢ LỜI CHĂM SÓC NGƯỜI CAO TUỔI")
        print("="*60)
        
        # Hiển thị menu chủ đề
        print("\n📋 Các chủ đề có sẵn:")
        for key, topic in generator.topics.items():
            print(f"{key:2}. {topic}")
        
        print("\n🎯 Lựa chọn:")
        print("A. Sinh dataset lớn (1000+ cặp Q&A)")
        print("B. Sinh theo chủ đề cụ thể")
        print("C. Test sinh vài cặp Q&A")
        
        choice = input("\nNhập lựa chọn (A/B/C): ").upper()
        
        if choice == 'A':
            num_pairs = int(input("Nhập số cặp Q&A muốn sinh (mặc định 1000): ") or "1000")
            generator.generate_dataset(num_pairs)
            
        elif choice == 'B':
            topic_key = input("Nhập số chủ đề (1-12): ")
            if topic_key in generator.topics:
                num_pairs = int(input("Nhập số cặp Q&A (mặc định 20): ") or "20")
                qa_pairs = generator.generate_qa_pairs(topic_key, num_pairs)
                if qa_pairs:
                    generator.save_to_csv(qa_pairs)
            else:
                print("❌ Chủ đề không hợp lệ!")
                
        elif choice == 'C':
            # Test với 3 cặp Q&A
            qa_pairs = generator.generate_qa_pairs("1", 3)
            if qa_pairs:
                print("\n📝 Kết quả test:")
                for i, qa in enumerate(qa_pairs, 1):
                    print(f"\n{i}. INPUT: {qa['input']}")
                    print(f"   OUTPUT: {qa['output']}")
                
                save = input("\nLưu kết quả test? (y/n): ").lower()
                if save == 'y':
                    generator.save_to_csv(qa_pairs, "test_output.csv")
        else:
            print("❌ Lựa chọn không hợp lệ!")
            
    except KeyboardInterrupt:
        print("\n\n⏹️ Đã dừng chương trình.")
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")

if __name__ == "__main__":
    main()
