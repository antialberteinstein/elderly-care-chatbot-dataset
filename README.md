# 🤖 Elderly Care QA Dataset Generator

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Advanced Dataset Generator for Elderly Care Chatbots**  
*Powered by Google Gemini API*

**Repository: `elderly-care-chatbot-dataset`**

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [🎯 Features](#-features) • [💡 Examples](#-examples)

</div>

---

## 🌟 Overview

The **Elderly Care QA Dataset Generator** is a sophisticated tool designed to create high-quality conversational datasets for training chatbots that specialize in elderly care. Using Google's Gemini AI, it generates natural, culturally-appropriate Vietnamese conversations between elderly users and care assistants.

### 🎯 Key Features

- **🤖 AI-Powered Generation**: Leverages Google Gemini for natural conversation creation
- **🏃‍♂️ Marathon Mode**: Continuous generation with automatic backups
- **📊 Multi-Format Support**: CSV, JSON, Excel export capabilities
- **🎲 12 Specialized Topics**: Comprehensive coverage of elderly care scenarios
- **🔧 Cross-Platform**: Windows, Linux, macOS support
- **📈 Advanced Analytics**: Dataset statistics and quality metrics
- **🧹 Smart Management**: Automatic file organization and cleanup

### 🎭 Conversation Topics

| Topic | Description | Examples |
|-------|-------------|----------|
| 🔔 **Daily Reminders** | Medication, appointments, meals | "I forgot to take my medicine" |
| 🏥 **Health Care** | Nutrition, symptoms, medical advice | "My blood pressure is high" |
| 🧠 **Mental Health** | Sleep, entertainment, emotional support | "I can't sleep well" |
| 💬 **Communication** | Conversation, storytelling, listening | "I feel lonely today" |
| 🍳 **Cooking & Shopping** | Recipes, food storage, shopping tips | "What should I cook today?" |
| 🏠 **Household Tasks** | Cleaning, organizing, home tips | "How to clean the house efficiently?" |
| 🎭 **Entertainment** | Movies, music, games, stories | "Recommend me a good movie" |
| 🕯️ **Spiritual & Traditional** | Ceremonies, festivals, folklore | "When is the ancestor worship day?" |
| 👨‍👩‍👧‍👦 **Family Relations** | Calling family, expressing love | "I miss my grandchildren" |
| 📱 **Technology** | Phone usage, scam prevention | "How to use video calling?" |
| 📢 **Notifications** | Schedule reminders, weather updates | "What's the weather today?" |
| ❓ **FAQ** | Common health and daily life questions | "What foods are good for diabetes?" |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+** installed on your system
- **Google Gemini API key** (free at [Google AI Studio](https://aistudio.google.com/app/apikey))
- **Internet connection** for API calls

### 🔧 Installation

#### Option 1: Windows (Batch Script)
```batch
# Clone or download the project
git clone https://github.com/your-repo/elderly-care-qa-generator.git
cd elderly-care-qa-generator

# Run the Windows launcher
run.bat
```

#### Option 2: Windows (PowerShell)
```powershell
# Navigate to project directory
cd elderly-care-qa-generator

# Run PowerShell launcher
.\run.ps1
```

#### Option 3: Unix/Linux/macOS
```bash
# Clone or download the project
git clone https://github.com/your-repo/elderly-care-qa-generator.git
cd elderly-care-qa-generator

# Make script executable and run
chmod +x run.sh
./run.sh
```

#### Option 4: Manual Installation
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Unix/Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your Google API key

# Run the manager
python qa_manager.py
```

### 🔑 API Key Setup

1. **Get your Google Gemini API key**:
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy the generated key

2. **Configure the key**:
   ```bash
   # Create .env file
   echo "GOOGLE_API_KEY=your_actual_api_key_here" > .env
   ```

---

## 🎮 Usage Guide

### Interactive Mode

Launch the interactive menu:
```bash
python qa_manager.py
```

The interactive menu provides:
- 🔍 **API Connection Check**
- 🎲 **Demo Generation** (Quick testing)
- 🎯 **Custom Generation** (Topic-specific)
- 🏃‍♂️ **Marathon Mode** (Continuous generation)
- 📊 **File Management** (Merge, analyze, clean)

### Command Line Interface

```bash
# Check API connection
python qa_manager.py --check

# Generate demo dataset
python qa_manager.py --demo

# Start marathon mode
python qa_manager.py --marathon

# Merge CSV files
python qa_manager.py --merge

# Analyze datasets
python qa_manager.py --analyze

# Clean output directories
python qa_manager.py --clean

# Show system information
python qa_manager.py --info
```

### Using Launcher Scripts

```bash
# Windows
run.bat --demo          # Generate demo
run.bat --marathon      # Start marathon mode

# Unix/Linux/macOS
./run.sh --demo         # Generate demo
./run.sh --marathon     # Start marathon mode

# PowerShell
.\run.ps1 -Demo         # Generate demo
.\run.ps1 -Marathon     # Start marathon mode
```

---

## 📊 Output Structure

The generator creates organized output directories:

```
elderly-care-qa-generator/
├── marathon_rounds_20250701_143022/    # Individual round files
│   ├── marathon_round_1_20250701_143045.csv
│   ├── marathon_round_2_20250701_144112.csv
│   └── ...
├── marathon_finals/                    # Consolidated datasets
│   ├── marathon_final_20250701_151234.csv
│   └── ...
├── demo_20250701_140530.csv           # Demo outputs
├── topic_1_daily_reminders_20250701.csv  # Topic-specific files
└── merged_dataset_20250701.csv        # Merged files
```

### 📄 CSV Format

Each dataset contains two columns:

| Column | Description | Example |
|--------|-------------|---------|
| `input` | User's question/statement | "Tôi bị đau đầu, có nên uống thuốc không?" |
| `output` | Chatbot's response | "Cô/Chú có thể uống paracetamol nếu đau đầu nhẹ..." |

---

## 🎯 Features Deep Dive

### 🏃‍♂️ Marathon Mode

Marathon Mode is the flagship feature for large-scale dataset generation:

- **Continuous Generation**: Runs indefinitely until stopped
- **Round-based Processing**: Each round generates 360 Q&A pairs (30 per topic)
- **Automatic Backups**: Saves progress after each round
- **Graceful Shutdown**: Ctrl+C stops safely after completing current round
- **Progress Tracking**: Real-time statistics and performance metrics

```python
# Example Marathon Session Output:
🏃‍♂️ MARATHON GENERATOR - CONTINUOUS DATA GENERATION
═══════════════════════════════════════════════════════════════
📋 Configuration: 30 pairs per topic | 12 topics = 360 pairs/round
⏹️  Press Ctrl+C to stop safely
🚀 Starting generation...

🔄 === ROUND 1 ===
📝 Topic 1: Daily Reminders...
   ✅ Generated 30 pairs in 15.2s | Total: 30
📝 Topic 2: Health Care...
   ✅ Generated 30 pairs in 18.7s | Total: 60
...
🎉 Round 1 completed!
📊 Generated 360 pairs in 5.2 minutes
💾 Saved: marathon_rounds_20250701_143022/marathon_round_1_20250701_143045.csv
📈 Total: 360 pairs
🏆 Average speed: 69.2 pairs/minute
```

### 📊 Advanced Analytics

The analytics feature provides comprehensive dataset insights:

```python
# Example Analytics Output:
📊 Analysis of: marathon_final_20250701_151234.csv
══════════════════════════════════════════════════════════════
📝 Total rows: 1,080
📋 Columns: ['input', 'output']

📏 INPUT Statistics:
   Average length: 67.3 characters
   Min length: 15 characters
   Max length: 184 characters

📏 OUTPUT Statistics:
   Average length: 156.8 characters
   Min length: 45 characters
   Max length: 298 characters

💾 File size: 0.89 MB
```

### 🔧 Smart File Management

- **Automatic Organization**: Files sorted into logical directories
- **Deduplication**: Removes duplicate Q&A pairs during merging
- **Batch Operations**: Process multiple files simultaneously
- **Pattern Matching**: Merge files by naming patterns
- **Safe Cleanup**: Confirmation prompts before deletion

---

## 💡 Examples

### Basic Usage Examples

#### Generate Demo Dataset
```python
from qa_manager import QAManager

manager = QAManager()
manager.demo_generation()
```

#### Custom Topic Generation
```python
# Generate 50 Q&A pairs about health care
generator = QAGenerator()
qa_pairs = generator.generate_qa_pairs("2", 50)  # Topic 2: Health Care
generator.save_to_csv(qa_pairs, "health_care_dataset.csv")
```

#### Merge Multiple Datasets
```python
# Merge all CSV files in current directory
manager = QAManager()
manager.merge_csv_files()
```

### Advanced Usage Examples

#### Marathon with Custom Configuration
```python
from marathon_generator import MarathonGenerator

marathon = MarathonGenerator()
marathon.run_marathon()
# Generates continuous datasets until stopped
```

#### Programmatic API Usage
```python
from generator_google import QAGenerator

# Initialize generator
generator = QAGenerator()

# Generate for all topics
all_qa_pairs = []
for topic_id in range(1, 13):
    pairs = generator.generate_qa_pairs(str(topic_id), 25)
    all_qa_pairs.extend(pairs)

# Save combined dataset
generator.save_to_csv(all_qa_pairs, "complete_dataset.csv")
print(f"Generated {len(all_qa_pairs)} total Q&A pairs")
```

### Sample Generated Data

```csv
input,output
"Tôi quên uống thuốc huyết áp rồi, giờ có nên uống không?","Cô/Chú đừng lo lắng quá nhé. Nếu mới quên trong vòng 2-3 tiếng thì vẫn có thể uống được. Tuy nhiên, nếu đã gần đến giờ uống thuốc tiếp theo thì cô/chú bỏ qua lần này và uống đúng giờ như bình thường. Quan trọng là không được uống 2 lần liều một lúc nhé. Lần sau cô/chú có thể đặt báo thức để nhớ uống thuốc đúng giờ."

"Hôm nay trời mưa, tôi không muốn ra ngoài tập thể dục","Dạ cô/chú không cần lo lắng, ngày mưa vẫn có thể tập thể dục tại nhà mà. Cô/chú có thể đi bộ nhẹ trong nhà khoảng 15-20 phút, hoặc làm các động tác giãn cơ đơn giản như xoay vai, cổ tay. Cô/chú cũng có thể ngồi trên ghế và làm bài tập chân tại chỗ. Điều quan trọng là duy trì vận động hàng ngày để sức khỏe được tốt nhất nhé!"
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Google Gemini API Configuration
GOOGLE_API_KEY=your_actual_api_key_here

# Optional: Generation Parameters
DEFAULT_BATCH_SIZE=30
DEFAULT_BACKUP_INTERVAL=500
MAX_RETRIES=3
REQUEST_DELAY=1.0
```

### Advanced Configuration

You can customize generation parameters by modifying the generator classes:

```python
# Custom generation parameters
class CustomQAGenerator(QAGenerator):
    def __init__(self):
        super().__init__()
        self.batch_size = 50  # Increase batch size
        self.delay = 0.5      # Reduce delay between requests
        self.max_retries = 5  # Increase retry attempts
```

---

## 📈 Performance & Scaling

### Performance Metrics

| Mode | Speed | Memory Usage | API Calls |
|------|--------|--------------|-----------|
| Demo | ~10 pairs/min | Low | Minimal |
| Custom | ~20-30 pairs/min | Medium | Moderate |
| Marathon | ~60-80 pairs/min | High | Intensive |

### Optimization Tips

1. **Batch Size**: Increase batch size for better throughput
2. **Delays**: Reduce delays if API rate limits allow
3. **Memory**: Use backup intervals to manage memory usage
4. **Network**: Stable internet connection improves reliability

### Scaling Considerations

- **API Limits**: Google Gemini has rate limits (check current quotas)
- **File Size**: Large CSV files may impact performance
- **Storage**: Marathon mode can generate GBs of data
- **Memory**: Long sessions may require periodic restarts

---

## 🛠️ Troubleshooting

### Common Issues

#### API Connection Problems
```bash
# Check API key
python qa_manager.py --check

# Verify .env file
cat .env

# Test internet connection
ping google.com
```

#### Python Environment Issues
```bash
# Check Python version
python --version

# Verify virtual environment
which python  # Unix/Linux/macOS
where python   # Windows

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### File Permission Issues
```bash
# Unix/Linux/macOS
chmod +x run.sh
chmod 755 *.py

# Windows (PowerShell as Administrator)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error Messages

| Error | Cause | Solution |
|-------|--------|----------|
| `ModuleNotFoundError: No module named 'google'` | Missing dependencies | Run `pip install -r requirements.txt` |
| `ValueError: API key not found` | Missing or invalid API key | Check `.env` file and API key |
| `ConnectionError` | Network issues | Check internet connection |
| `PermissionError` | File access issues | Check file permissions |

### Debug Mode

Enable debug mode for detailed logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Run your generation code
```

---

## 📚 API Reference

### QAGenerator Class

```python
class QAGenerator:
    def __init__(self):
        """Initialize the QA generator with Google Gemini API"""
    
    def generate_qa_pairs(self, topic_key: str, num_pairs: int = 10) -> List[Dict]:
        """Generate Q&A pairs for a specific topic"""
    
    def save_to_csv(self, qa_pairs: List[Dict], filename: str = None) -> str:
        """Save Q&A pairs to CSV file"""
    
    def test_connection(self) -> bool:
        """Test API connection"""
```

### MarathonGenerator Class

```python
class MarathonGenerator:
    def __init__(self):
        """Initialize marathon generator"""
    
    def run_marathon(self):
        """Start continuous generation process"""
    
    def signal_handler(self, signum, frame):
        """Handle Ctrl+C gracefully"""
```

### QAManager Class

```python
class QAManager:
    def run_interactive(self):
        """Run interactive menu interface"""
    
    def check_api(self) -> bool:
        """Check API connection status"""
    
    def demo_generation(self):
        """Generate demo dataset"""
    
    def merge_csv_files(self):
        """Merge multiple CSV files"""
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

```bash
# Fork the repository
git clone https://github.com/your-username/elderly-care-qa-generator.git
cd elderly-care-qa-generator

# Create development environment
python -m venv dev-env
source dev-env/bin/activate  # Unix/Linux/macOS
# or
dev-env\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

### Code Style

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Add docstrings to all functions
- Include unit tests for new features

### Pull Request Process

1. Create a feature branch: `git checkout -b feature/amazing-feature`
2. Make your changes and test thoroughly
3. Update documentation if needed
4. Submit a pull request with clear description

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Google Gemini AI** for providing the underlying AI capabilities
- **Vietnamese elderly care community** for inspiration and requirements
- **Open source contributors** who made this project possible

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/elderly-care-qa-generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/elderly-care-qa-generator/discussions)
- **Email**: support@your-domain.com

---

<div align="center">

**Made with ❤️ for the elderly care community**

*Helping bridge the gap between technology and compassionate care*

[![Star this repo](https://img.shields.io/github/stars/your-repo/elderly-care-qa-generator?style=social)](https://github.com/your-repo/elderly-care-qa-generator)
[![Fork this repo](https://img.shields.io/github/forks/your-repo/elderly-care-qa-generator?style=social)](https://github.com/your-repo/elderly-care-qa-generator/fork)

</div>
