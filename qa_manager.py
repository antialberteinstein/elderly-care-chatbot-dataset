#!/usr/bin/env python3
"""
🤖 Elderly Care QA Dataset Manager
Advanced tool for generating conversational datasets for elderly care chatbots.
"""

import os
import sys
import argparse
import glob
import pandas as pd
from datetime import datetime
from pathlib import Path

# Import local modules
from generator_google import QAGenerator
from marathon_generator import MarathonGenerator
from check_google_api import check_google_api

class QAManager:
    def __init__(self):
        """Initialize QA Dataset Manager"""
        self.generator = None
        self.version = "1.0.0"
        
    def show_banner(self):
        """Display cool banner"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                 🤖 ELDERLY CARE QA MANAGER                   ║
║                                                              ║
║     Advanced Dataset Generator for Elderly Care Chatbots    ║
║                    Powered by Google Gemini                 ║
║                                                              ║
║                        Version 1.0.0                        ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)

    def show_menu(self):
        """Display interactive menu"""
        print("\n🎯 MAIN MENU")
        print("=" * 50)
        print("1. 🔍 Check Google API Connection")
        print("2. 🎲 Generate Demo Dataset (Quick Test)")
        print("3. 🎯 Generate Custom Dataset (By Topic)")
        print("4. 🏃‍♂️ Marathon Mode (Continuous Generation)")
        print("5. 📊 Merge CSV Files")
        print("6. 📈 Analyze Dataset Statistics")
        print("7. 🧹 Clean Output Directories")
        print("8. ℹ️  Show System Information")
        print("9. 🔧 Advanced Options")
        print("0. 🚪 Exit")
        print("=" * 50)

    def check_api(self):
        """Check Google API connection"""
        print("\n🔍 Checking Google Gemini API...")
        return check_google_api()

    def demo_generation(self):
        """Generate demo dataset"""
        print("\n🎲 DEMO GENERATION")
        print("-" * 30)
        
        try:
            if not self.generator:
                self.generator = QAGenerator()
            
            num_pairs = int(input("Enter number of Q&A pairs (default: 5): ") or "5")
            topic = input("Enter topic number (1-12, default: 1): ") or "1"
            
            if topic not in self.generator.topics:
                print("❌ Invalid topic number!")
                return
            
            print(f"\n🔄 Generating {num_pairs} Q&A pairs for topic {topic}...")
            qa_pairs = self.generator.generate_qa_pairs(topic, num_pairs)
            
            if qa_pairs:
                filename = f"demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                self.generator.save_to_csv(qa_pairs, filename)
                
                print(f"✅ Demo completed! Generated {len(qa_pairs)} pairs")
                print(f"📁 File saved: {os.path.abspath(filename)}")
                
                # Show preview
                if input("\nShow preview? (y/n): ").lower() == 'y':
                    self.show_preview(qa_pairs[:3])
            else:
                print("❌ Failed to generate demo data")
                
        except Exception as e:
            print(f"❌ Error: {e}")

    def custom_generation(self):
        """Generate custom dataset by topic"""
        print("\n🎯 CUSTOM GENERATION")
        print("-" * 30)
        
        try:
            if not self.generator:
                self.generator = QAGenerator()
            
            # Show available topics
            print("\n📋 Available Topics:")
            for key, topic in self.generator.topics.items():
                print(f"{key:2}. {topic}")
            
            topic = input("\nEnter topic number (1-12): ")
            if topic not in self.generator.topics:
                print("❌ Invalid topic number!")
                return
            
            num_pairs = int(input("Enter number of Q&A pairs (default: 50): ") or "50")
            
            print(f"\n🔄 Generating {num_pairs} Q&A pairs for topic {topic}...")
            qa_pairs = self.generator.generate_qa_pairs(topic, num_pairs)
            
            if qa_pairs:
                topic_name = self.generator.topics[topic].split('(')[0].strip()
                filename = f"topic_{topic}_{topic_name.replace(' ', '_').lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                self.generator.save_to_csv(qa_pairs, filename)
                
                print(f"✅ Generation completed! Generated {len(qa_pairs)} pairs")
                print(f"📁 File saved: {os.path.abspath(filename)}")
            else:
                print("❌ Failed to generate data")
                
        except Exception as e:
            print(f"❌ Error: {e}")

    def marathon_mode(self):
        """Start marathon generation"""
        print("\n🏃‍♂️ MARATHON MODE")
        print("-" * 30)
        print("This will generate data continuously until you stop it.")
        print("Press Ctrl+C to stop safely.")
        
        if input("\nStart marathon? (y/n): ").lower() != 'y':
            return
        
        try:
            marathon = MarathonGenerator()
            marathon.run_marathon()
        except Exception as e:
            print(f"❌ Error: {e}")

    def merge_csv_files(self):
        """Merge multiple CSV files"""
        print("\n📊 MERGE CSV FILES")
        print("-" * 30)
        
        # Find CSV files
        csv_files = glob.glob("*.csv") + glob.glob("**/*.csv", recursive=True)
        if not csv_files:
            print("❌ No CSV files found in current directory")
            return
        
        print("📁 Found CSV files:")
        for i, file in enumerate(csv_files, 1):
            size = os.path.getsize(file) / 1024  # KB
            print(f"{i:2}. {file} ({size:.1f} KB)")
        
        print("\nOptions:")
        print("1. Merge ALL files")
        print("2. Select specific files")
        print("3. Merge files by pattern")
        
        choice = input("Choose option (1-3): ")
        
        try:
            if choice == "1":
                self._merge_files(csv_files)
            elif choice == "2":
                indices = input("Enter file numbers (comma-separated): ").split(',')
                selected_files = [csv_files[int(i.strip())-1] for i in indices if i.strip().isdigit()]
                self._merge_files(selected_files)
            elif choice == "3":
                pattern = input("Enter pattern (e.g., marathon_*, topic_*): ")
                pattern_files = glob.glob(pattern)
                if pattern_files:
                    self._merge_files(pattern_files)
                else:
                    print("❌ No files match the pattern")
        except Exception as e:
            print(f"❌ Error merging files: {e}")

    def _merge_files(self, files):
        """Helper method to merge CSV files"""
        if not files:
            print("❌ No files to merge")
            return
        
        print(f"\n🔄 Merging {len(files)} files...")
        all_data = []
        
        for file in files:
            try:
                df = pd.read_csv(file)
                all_data.append(df)
                print(f"   ✅ {file}: {len(df)} rows")
            except Exception as e:
                print(f"   ❌ {file}: Error reading file")
        
        if all_data:
            merged_df = pd.concat(all_data, ignore_index=True)
            
            # Remove duplicates
            original_size = len(merged_df)
            merged_df = merged_df.drop_duplicates(subset=['input', 'output'])
            final_size = len(merged_df)
            
            # Save merged file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"merged_dataset_{timestamp}.csv"
            merged_df.to_csv(filename, index=False)
            
            print(f"\n✅ Merge completed!")
            print(f"📊 Original: {original_size} rows")
            print(f"📊 After deduplication: {final_size} rows")
            print(f"📁 Saved: {os.path.abspath(filename)}")

    def analyze_dataset(self):
        """Analyze dataset statistics"""
        print("\n📈 DATASET ANALYSIS")
        print("-" * 30)
        
        csv_files = glob.glob("*.csv") + glob.glob("**/*.csv", recursive=True)
        if not csv_files:
            print("❌ No CSV files found")
            return
        
        print("📁 Available files:")
        for i, file in enumerate(csv_files, 1):
            print(f"{i:2}. {file}")
        
        try:
            choice = int(input("Select file to analyze: ")) - 1
            if 0 <= choice < len(csv_files):
                self._analyze_file(csv_files[choice])
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Invalid input")

    def _analyze_file(self, filename):
        """Analyze a specific CSV file"""
        try:
            df = pd.read_csv(filename)
            
            print(f"\n📊 Analysis of: {filename}")
            print("=" * 50)
            print(f"📝 Total rows: {len(df)}")
            print(f"📋 Columns: {list(df.columns)}")
            
            if 'input' in df.columns and 'output' in df.columns:
                # Calculate statistics
                input_lengths = df['input'].str.len()
                output_lengths = df['output'].str.len()
                
                print(f"\n📏 INPUT Statistics:")
                print(f"   Average length: {input_lengths.mean():.1f} characters")
                print(f"   Min length: {input_lengths.min()} characters")
                print(f"   Max length: {input_lengths.max()} characters")
                
                print(f"\n📏 OUTPUT Statistics:")
                print(f"   Average length: {output_lengths.mean():.1f} characters")
                print(f"   Min length: {output_lengths.min()} characters")
                print(f"   Max length: {output_lengths.max()} characters")
                
                # Show sample data
                print(f"\n📝 Sample data:")
                for i, row in df.head(3).iterrows():
                    print(f"   {i+1}. INPUT: {row['input'][:50]}...")
                    print(f"      OUTPUT: {row['output'][:50]}...")
                    print()
            
            # File size
            size_mb = os.path.getsize(filename) / (1024 * 1024)
            print(f"💾 File size: {size_mb:.2f} MB")
            
        except Exception as e:
            print(f"❌ Error analyzing file: {e}")

    def clean_directories(self):
        """Clean output directories"""
        print("\n🧹 CLEAN DIRECTORIES")
        print("-" * 30)
        
        # Find directories and files to clean
        dirs_to_check = ['marathon_rounds_*', 'marathon_finals']
        files_to_check = ['*.csv', 'demo_*.csv', 'test_*.csv']
        
        items_found = []
        
        # Check directories
        for pattern in dirs_to_check:
            dirs = glob.glob(pattern)
            for d in dirs:
                if os.path.isdir(d):
                    file_count = len(glob.glob(os.path.join(d, "*.csv")))
                    items_found.append(('dir', d, file_count))
        
        # Check files
        for pattern in files_to_check:
            files = glob.glob(pattern)
            for f in files:
                if os.path.isfile(f):
                    size_kb = os.path.getsize(f) / 1024
                    items_found.append(('file', f, size_kb))
        
        if not items_found:
            print("✅ No items to clean")
            return
        
        print("🗂️ Items found:")
        for item_type, name, info in items_found:
            if item_type == 'dir':
                print(f"   📁 {name} ({info} files)")
            else:
                print(f"   📄 {name} ({info:.1f} KB)")
        
        if input("\nDelete these items? (y/n): ").lower() == 'y':
            self._clean_items(items_found)

    def _clean_items(self, items):
        """Helper method to clean items"""
        import shutil
        
        deleted_count = 0
        for item_type, name, _ in items:
            try:
                if item_type == 'dir':
                    shutil.rmtree(name)
                    print(f"   🗑️ Deleted directory: {name}")
                else:
                    os.remove(name)
                    print(f"   🗑️ Deleted file: {name}")
                deleted_count += 1
            except Exception as e:
                print(f"   ❌ Failed to delete {name}: {e}")
        
        print(f"\n✅ Cleaned {deleted_count} items")

    def show_system_info(self):
        """Show system information"""
        print("\nℹ️ SYSTEM INFORMATION")
        print("-" * 30)
        print(f"🐍 Python: {sys.version}")
        print(f"📂 Working directory: {os.getcwd()}")
        print(f"🔧 Manager version: {self.version}")
        
        # Check API status
        print("\n🔌 API Status:")
        try:
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv('GOOGLE_API_KEY')
            if api_key:
                print(f"   ✅ Google API Key: {api_key[:20]}...")
            else:
                print("   ❌ Google API Key: Not found")
        except:
            print("   ❌ API configuration error")
        
        # Check dependencies
        print("\n📦 Dependencies:")
        dependencies = ['google.generativeai', 'pandas', 'python-dotenv']
        for dep in dependencies:
            try:
                __import__(dep.replace('-', '_').replace('.', '_'))
                print(f"   ✅ {dep}")
            except ImportError:
                print(f"   ❌ {dep}: Not installed")

    def show_preview(self, qa_pairs):
        """Show preview of Q&A pairs"""
        print("\n👀 PREVIEW:")
        print("-" * 40)
        for i, qa in enumerate(qa_pairs, 1):
            print(f"{i}. INPUT: {qa['input']}")
            print(f"   OUTPUT: {qa['output'][:100]}...")
            print()

    def advanced_options(self):
        """Show advanced options menu"""
        print("\n🔧 ADVANCED OPTIONS")
        print("-" * 30)
        print("1. 🎛️  Configure Generation Parameters")
        print("2. 📊 Export Dataset to Different Formats")
        print("3. 🔄 Batch Process Multiple Topics")
        print("4. 🧪 Test Custom Prompts")
        print("5. 📋 Generate Topic-Based Reports")
        print("0. ⬅️  Back to Main Menu")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            self.configure_parameters()
        elif choice == "2":
            self.export_formats()
        elif choice == "3":
            self.batch_process()
        elif choice == "4":
            self.test_custom_prompts()
        elif choice == "5":
            self.generate_reports()

    def configure_parameters(self):
        """Configure generation parameters"""
        print("\n🎛️ GENERATION PARAMETERS")
        print("(This feature will be implemented in future versions)")

    def export_formats(self):
        """Export to different formats"""
        print("\n📊 EXPORT FORMATS")
        print("(JSON, JSONL, XML export will be implemented in future versions)")

    def batch_process(self):
        """Batch process multiple topics"""
        print("\n🔄 BATCH PROCESSING")
        print("(Batch processing will be implemented in future versions)")

    def test_custom_prompts(self):
        """Test custom prompts"""
        print("\n🧪 CUSTOM PROMPT TESTING")
        print("(Custom prompt testing will be implemented in future versions)")

    def generate_reports(self):
        """Generate topic-based reports"""
        print("\n📋 TOPIC REPORTS")
        print("(Report generation will be implemented in future versions)")

    def run_interactive(self):
        """Run interactive menu"""
        self.show_banner()
        
        while True:
            self.show_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                self.check_api()
            elif choice == '2':
                self.demo_generation()
            elif choice == '3':
                self.custom_generation()
            elif choice == '4':
                self.marathon_mode()
            elif choice == '5':
                self.merge_csv_files()
            elif choice == '6':
                self.analyze_dataset()
            elif choice == '7':
                self.clean_directories()
            elif choice == '8':
                self.show_system_info()
            elif choice == '9':
                self.advanced_options()
            elif choice == '0':
                print("\n👋 Thank you for using QA Manager!")
                break
            else:
                print("\n❌ Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

def main():
    """Main function with argument parsing"""
    parser = argparse.ArgumentParser(
        description="🤖 Elderly Care QA Dataset Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python qa_manager.py                    # Interactive mode
  python qa_manager.py --check           # Check API connection
  python qa_manager.py --demo            # Generate demo dataset
  python qa_manager.py --marathon        # Start marathon mode
  python qa_manager.py --merge           # Merge CSV files
  python qa_manager.py --analyze         # Analyze datasets
  python qa_manager.py --clean           # Clean directories
        """
    )
    
    parser.add_argument('--check', action='store_true', help='Check Google API connection')
    parser.add_argument('--demo', action='store_true', help='Generate demo dataset')
    parser.add_argument('--marathon', action='store_true', help='Start marathon mode')
    parser.add_argument('--merge', action='store_true', help='Merge CSV files')
    parser.add_argument('--analyze', action='store_true', help='Analyze dataset statistics')
    parser.add_argument('--clean', action='store_true', help='Clean output directories')
    parser.add_argument('--info', action='store_true', help='Show system information')
    parser.add_argument('--version', action='version', version='QA Manager 1.0.0')
    
    args = parser.parse_args()
    manager = QAManager()
    
    # If no arguments provided, run interactive mode
    if not any(vars(args).values()):
        manager.run_interactive()
        return
    
    # Handle command line arguments
    if args.check:
        manager.check_api()
    elif args.demo:
        manager.demo_generation()
    elif args.marathon:
        manager.marathon_mode()
    elif args.merge:
        manager.merge_csv_files()
    elif args.analyze:
        manager.analyze_dataset()
    elif args.clean:
        manager.clean_directories()
    elif args.info:
        manager.show_system_info()

if __name__ == "__main__":
    main()
