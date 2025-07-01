"""
Marathon Generator - Sinh dữ liệu liên tục cho tất cả chủ đề
Chạy liên tục cho đến khi nhận lệnh dừng (Ctrl+C)
"""
import signal
import sys
import time
import os
from datetime import datetime
from generator_google import QAGenerator

class MarathonGenerator:
    def __init__(self):
        """Khởi tạo Marathon Generator"""
        self.generator = QAGenerator()
        self.running = True
        self.current_round = 1
        self.total_generated = 0
        self.all_qa_pairs = []
        
        # Tạo thư mục chứa kết quả
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.rounds_dir = f"marathon_rounds_{self.session_id}"
        self.final_dir = "marathon_finals"
        
        # Tạo thư mục nếu chưa có
        os.makedirs(self.rounds_dir, exist_ok=True)
        os.makedirs(self.final_dir, exist_ok=True)
        
        print(f"📁 Thư mục rounds: {self.rounds_dir}")
        print(f"📁 Thư mục finals: {self.final_dir}")
        
        # Thiết lập signal handler cho Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)
        
    def signal_handler(self, signum, frame):
        """Xử lý khi nhận tín hiệu dừng (Ctrl+C)"""
        print("\n\n🛑 Nhận tín hiệu dừng...")
        print("💭 Tạm biệt, hẹn gặp lại!")
        print("⏳ Đang hoàn tất lượt hiện tại...")
        self.running = False
        
    def run_marathon(self):
        """Chạy marathon sinh dữ liệu liên tục"""
        print("🏃‍♂️ MARATHON GENERATOR - SINH DỮ LIỆU LIÊN TỤC")
        print("=" * 60)
        print("📋 Cấu hình: Mỗi chủ đề 30 câu | 12 chủ đề = 360 câu/lượt")
        print("⏹️  Nhấn Ctrl+C để dừng an toàn")
        print("🚀 Bắt đầu sinh dữ liệu...\n")
        
        try:
            while self.running:
                print(f"🔄 === LƯỢT {self.current_round} === ")
                round_start_time = time.time()
                round_qa_pairs = []
                
                # Sinh từng chủ đề theo thứ tự (1-12)
                for topic_key in sorted(self.generator.topics.keys(), key=int):
                    if not self.running:
                        print("🔄 Dừng ở giữa lượt...")
                        break
                        
                    topic_name = self.generator.topics[topic_key]
                    print(f"📝 Chủ đề {topic_key}: {topic_name[:50]}...")
                    
                    # Sinh 30 câu cho chủ đề này
                    start_time = time.time()
                    qa_pairs = self.generator.generate_qa_pairs(topic_key, 30)
                    elapsed = time.time() - start_time
                    
                    if qa_pairs:
                        round_qa_pairs.extend(qa_pairs)
                        self.total_generated += len(qa_pairs)
                        print(f"   ✅ Sinh được {len(qa_pairs)} câu trong {elapsed:.1f}s | Tổng: {self.total_generated}")
                    else:
                        print(f"   ❌ Lỗi sinh chủ đề {topic_key}")
                    
                    # Nghỉ 2 giây giữa các chủ đề (nếu vẫn đang chạy)
                    if self.running and topic_key != "12":  # Không nghỉ sau chủ đề cuối
                        time.sleep(2)
                
                # Lưu dữ liệu sau mỗi lượt hoàn thành
                if round_qa_pairs:
                    self.all_qa_pairs.extend(round_qa_pairs)
                    
                    # Lưu file backup cho lượt này vào thư mục rounds
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"marathon_round_{self.current_round}_{timestamp}.csv"
                    filepath = os.path.join(self.rounds_dir, filename)
                    self.generator.save_to_csv(round_qa_pairs, filepath)
                    
                    round_time = time.time() - round_start_time
                    print(f"\n🎉 Hoàn thành lượt {self.current_round}!")
                    print(f"📊 Sinh được {len(round_qa_pairs)} câu trong {round_time/60:.1f} phút")
                    print(f"💾 Đã lưu: {filepath}")
                    print(f"📈 Tổng cộng: {self.total_generated} câu")
                    print(f"🏆 Tốc độ trung bình: {len(round_qa_pairs)/(round_time/60):.1f} câu/phút\n")
                
                self.current_round += 1
                
                # Nghỉ 5 giây trước lượt tiếp theo (nếu vẫn đang chạy)
                if self.running:
                    print("⏰ Nghỉ 5 giây trước lượt tiếp theo...")
                    for i in range(5, 0, -1):
                        if not self.running:
                            break
                        print(f"   {i}...", end=" ", flush=True)
                        time.sleep(1)
                    print("\n")
                    
        except Exception as e:
            print(f"\n❌ Lỗi không mong muốn: {e}")
        finally:
            self.save_final_results()
            
    def save_final_results(self):
        """Lưu kết quả tổng hợp cuối cùng"""
        print("\n📊 === TỔNG KẾT ===")
        
        if self.all_qa_pairs:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            final_filename = f"marathon_final_{timestamp}.csv"
            final_filepath = os.path.join(self.final_dir, final_filename)
            
            # Lưu file final
            self.generator.save_to_csv(self.all_qa_pairs, final_filepath)
            
            # Lấy đường dẫn tuyệt đối để hiển thị
            absolute_path = os.path.abspath(final_filepath)
            
            print(f"🎯 Hoàn thành: {self.current_round - 1} lượt")
            print(f"📝 Tổng số câu: {self.total_generated}")
            print(f"� Kích thước dataset: {len(self.all_qa_pairs)} dòng")
            print(f"� Thư mục rounds: {os.path.abspath(self.rounds_dir)}")
            print(f"🎯 FILE FINAL: {absolute_path}")
            print(f"⭐ Dataset đã sẵn sàng để training chatbot!")
            
            # Thông báo nổi bật về file final
            print("\n" + "=" * 60)
            print("🔥 FILE QUAN TRỌNG - DATASET HOÀN CHỈNH:")
            print(f"📂 {absolute_path}")
            print("=" * 60)
        else:
            print("📭 Không có dữ liệu để lưu.")
        
        print("\n🏁 Marathon Generator kết thúc!")

def main():
    """Hàm main chạy Marathon Generator"""
    try:
        print("🔥 KHỞI ĐỘNG MARATHON GENERATOR")
        print("📖 Đây là chế độ sinh dữ liệu liên tục")
        print("🎯 Mục tiêu: Tạo dataset lớn cho chatbot chăm sóc người cao tuổi")
        print("⚠️  Lưu ý: Nhấn Ctrl+C để dừng an toàn\n")
        
        # Khởi tạo và chạy
        marathon = MarathonGenerator()
        marathon.run_marathon()
        
    except KeyboardInterrupt:
        print("\n🛑 Chương trình đã được dừng bởi người dùng.")
    except Exception as e:
        print(f"\n❌ Lỗi không mong muốn: {e}")
    finally:
        print("👋 Cảm ơn bạn đã sử dụng Marathon Generator!")
        print("💾 Hãy kiểm tra các file CSV đã được tạo trong thư mục hiện tại.")

if __name__ == "__main__":
    main()
