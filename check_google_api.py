"""
Kiểm tra kết nối Google Gemini API
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

def check_google_api():
    """Kiểm tra Google Gemini API"""
    print("🔍 Kiểm tra Google Gemini API...")
    
    # Tải config từ .env
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        print("❌ Không tìm thấy GOOGLE_API_KEY trong file .env")
        return False
    
    print(f"✅ Tìm thấy API key: {api_key[:20]}...")
    
    try:
        # Cấu hình và test API
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Test với câu hỏi đơn giản
        response = model.generate_content("Xin chào! Bạn có khỏe không?")
        
        print("✅ Kết nối Google Gemini API thành công!")
        print(f"📝 Phản hồi test: {response.text[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ Lỗi khi kết nối Google Gemini API: {e}")
        return False

def main():
    """Hàm main"""
    print("=" * 50)
    print("🔧 KIỂM TRA API - GOOGLE GEMINI")
    print("=" * 50)
    
    if check_google_api():
        print("\n🎉 Tất cả đã sẵn sàng! Bạn có thể sử dụng generator_google.py")
    else:
        print("\n❌ Vui lòng kiểm tra lại cấu hình API key trong file .env")

if __name__ == "__main__":
    main()
