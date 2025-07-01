"""
Demo đơn giản - Test Google Gemini API
"""
from generator_google import QAGenerator

"""
Demo Marathon - Sinh dữ liệu liên tục tất cả chủ đề
"""
import signal
import sys
import time
from datetime import datetime
from generator_google import QAGenerator

class MarathonGenerator:
    def __init__(self):
        self.generator = QAGenerator()
        self.running = True
        self.current_round = 1
        self.total_generated = 0
        self.all_qa_pairs = []
        
        # Thiết lập signal handler cho Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)
        
    def signal_handler(self, signum, frame):
        """Xử lý khi nhận Ctrl+C"""
        print("\n\n🛑 Nhận tín hiệu dừng...")
        print("💭 Tạm biệt, hẹn gặp lại!")
        print("⏳ Đang hoàn tất lượt hiện tại...")
        self.running = False
        
    def run_marathon(self):
        """Chạy marathon sinh dữ liệu"""
        print("�‍♂️ MARATHON GENERATOR - SINH DỮ LIỆU LIÊN TỤC")
        print("=" * 60)
        print("📋 Mỗi chủ đề: 30 câu | Tất cả 12 chủ đề = 360 câu/lượt")
        print("⏹️  Nhấn Ctrl+C để dừng an toàn")
        print("🚀 Bắt đầu sinh dữ liệu...\n")
        
        try:
            while self.running:
                print(f"🔄 === LƯỢT {self.current_round} === ")
                round_start_time = time.time()
                round_qa_pairs = []
                
                # Sinh từng chủ đề (1-12)
                for topic_key in self.generator.topics.keys():
                    if not self.running:
                        break
                        
                    topic_name = self.generator.topics[topic_key]
                    print(f"� Chủ đề {topic_key}: {topic_name[:50]}...")
                    
                    # Sinh 30 câu cho chủ đề này
                    qa_pairs = self.generator.generate_qa_pairs(topic_key, 30)
                    
                    if qa_pairs:
                        round_qa_pairs.extend(qa_pairs)
                        self.total_generated += len(qa_pairs)
                        print(f"   ✅ Sinh được {len(qa_pairs)} câu | Tổng: {self.total_generated}")
                    else:
                        print(f"   ❌ Lỗi sinh chủ đề {topic_key}")
                    
                    # Nghỉ 2 giây giữa các chủ đề
                    if self.running:
                        time.sleep(2)
                
                # Lưu dữ liệu sau mỗi lượt
                if round_qa_pairs:
                    self.all_qa_pairs.extend(round_qa_pairs)
                    
                    # Lưu file backup cho lượt này
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"marathon_round_{self.current_round}_{timestamp}.csv"
                    self.generator.save_to_csv(round_qa_pairs, filename)
                    
                    round_time = time.time() - round_start_time
                    print(f"\n🎉 Hoàn thành lượt {self.current_round}!")
                    print(f"� Sinh được {len(round_qa_pairs)} câu trong {round_time:.1f}s")
                    print(f"💾 Đã lưu: {filename}")
                    print(f"� Tổng cộng: {self.total_generated} câu\n")
                
                self.current_round += 1
                
                # Nghỉ 5 giây trước lượt tiếp theo
                if self.running:
                    print("⏰ Nghỉ 5 giây trước lượt tiếp theo...")
                    time.sleep(5)
                    
        except Exception as e:
            print(f"\n❌ Lỗi: {e}")
        finally:
            self.save_final_results()
            
    def save_final_results(self):
        """Lưu kết quả cuối cùng"""
        if self.all_qa_pairs:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            final_filename = f"marathon_final_{timestamp}.csv"
            self.generator.save_to_csv(self.all_qa_pairs, final_filename)
            
            print(f"\n📊 === KẾT QUẢ CUỐI CÙNG ===")
            print(f"🎯 Hoàn thành {self.current_round - 1} lượt")
            print(f"📝 Tổng cộng: {self.total_generated} cặp Q&A")
            print(f"💾 File tổng hợp: {final_filename}")
            print(f"⭐ Chúc mừng! Dataset đã sẵn sàng để training!")
        else:
            print("\n📭 Không có dữ liệu để lưu.")

def demo():
    """Demo marathon generator"""
    try:
        marathon = MarathonGenerator()
        marathon.run_marathon()
    except KeyboardInterrupt:
        print("\n🛑 Chương trình đã được dừng.")
    except Exception as e:
        print(f"\n❌ Lỗi không mong muốn: {e}")
    finally:
        print("\n👋 Cảm ơn bạn đã sử dụng Marathon Generator!")

if __name__ == "__main__":
    demo()
