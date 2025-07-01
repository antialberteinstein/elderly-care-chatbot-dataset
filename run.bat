@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

REM ===================================================================
REM  🤖 Elderly Care QA Dataset Manager - Windows Launcher
REM  Advanced tool for generating conversational datasets
REM ===================================================================

title QA Dataset Manager - Windows

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                 🤖 ELDERLY CARE QA MANAGER                   ║
echo ║                                                              ║
echo ║     Advanced Dataset Generator for Elderly Care Chatbots    ║
echo ║                    Powered by Google Gemini                 ║
echo ║                                                              ║
echo ║                      Windows Launcher                       ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist .venv (
    echo 🔄 Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Failed to activate virtual environment
    pause
    exit /b 1
)

REM Check and install dependencies
echo 🔍 Checking dependencies...
python -c "import google.generativeai, pandas, dotenv" >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Parse command line arguments
set "INTERACTIVE=1"
set "COMMAND="

if "%1"=="" goto :interactive
if "%1"=="--help" goto :help
if "%1"=="-h" goto :help
if "%1"=="--check" set "COMMAND=--check" & set "INTERACTIVE=0"
if "%1"=="--demo" set "COMMAND=--demo" & set "INTERACTIVE=0"
if "%1"=="--marathon" set "COMMAND=--marathon" & set "INTERACTIVE=0"
if "%1"=="--merge" set "COMMAND=--merge" & set "INTERACTIVE=0"
if "%1"=="--analyze" set "COMMAND=--analyze" & set "INTERACTIVE=0"
if "%1"=="--clean" set "COMMAND=--clean" & set "INTERACTIVE=0"
if "%1"=="--info" set "COMMAND=--info" & set "INTERACTIVE=0"

if "!INTERACTIVE!"=="1" goto :interactive
if not "!COMMAND!"=="" goto :run_command

:help
echo.
echo 🎯 USAGE:
echo   run.bat                    # Interactive menu mode
echo   run.bat --check           # Check Google API connection
echo   run.bat --demo            # Generate demo dataset
echo   run.bat --marathon        # Start marathon generation
echo   run.bat --merge           # Merge CSV files
echo   run.bat --analyze         # Analyze datasets
echo   run.bat --clean           # Clean output directories
echo   run.bat --info            # Show system information
echo   run.bat --help            # Show this help
echo.
goto :end

:interactive
echo ✅ Starting interactive mode...
python qa_manager.py
goto :end

:run_command
echo ✅ Running command: !COMMAND!
python qa_manager.py !COMMAND!
goto :end

:end
echo.
echo 👋 Thank you for using QA Dataset Manager!
pause
