# ===================================================================
#  🤖 Elderly Care QA Dataset Manager - PowerShell Launcher
#  Advanced tool for generating conversational datasets
# ===================================================================

param(
    [string]$Command = "",
    [switch]$Help,
    [switch]$Check,
    [switch]$Demo,
    [switch]$Marathon,
    [switch]$Merge,
    [switch]$Analyze,
    [switch]$Clean,
    [switch]$Info
)

# Set console encoding to UTF-8
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Colors
$Red = "Red"
$Green = "Green"
$Yellow = "Yellow"
$Cyan = "Cyan"
$Magenta = "Magenta"

# Banner
Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                 🤖 ELDERLY CARE QA MANAGER                   ║" -ForegroundColor Cyan
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "║     Advanced Dataset Generator for Elderly Care Chatbots    ║" -ForegroundColor Cyan
Write-Host "║                    Powered by Google Gemini                 ║" -ForegroundColor Cyan
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "║                    PowerShell Launcher                      ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Function to show help
function Show-Help {
    Write-Host "🎯 USAGE:" -ForegroundColor Yellow
    Write-Host "  .\run.ps1                    # Interactive menu mode"
    Write-Host "  .\run.ps1 -Check            # Check Google API connection"
    Write-Host "  .\run.ps1 -Demo             # Generate demo dataset"
    Write-Host "  .\run.ps1 -Marathon         # Start marathon generation"
    Write-Host "  .\run.ps1 -Merge            # Merge CSV files"
    Write-Host "  .\run.ps1 -Analyze          # Analyze datasets"
    Write-Host "  .\run.ps1 -Clean            # Clean output directories"
    Write-Host "  .\run.ps1 -Info             # Show system information"
    Write-Host "  .\run.ps1 -Help             # Show this help"
    Write-Host ""
    exit 0
}

# Function to check Python
function Test-Python {
    try {
        $pythonVersion = python --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
            return $true
        } else {
            throw "Python not found"
        }
    } catch {
        Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
        Write-Host "Please install Python 3.7+ from https://python.org" -ForegroundColor Yellow
        exit 1
    }
}

# Function to setup virtual environment
function Initialize-VirtualEnvironment {
    if (-not (Test-Path ".venv")) {
        Write-Host "🔄 Creating virtual environment..." -ForegroundColor Yellow
        python -m venv .venv
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ Failed to create virtual environment" -ForegroundColor Red
            exit 1
        }
    }
    
    Write-Host "🔌 Activating virtual environment..." -ForegroundColor Yellow
    
    if (Test-Path ".venv\Scripts\Activate.ps1") {
        & .venv\Scripts\Activate.ps1
    } else {
        Write-Host "❌ Failed to find activation script" -ForegroundColor Red
        exit 1
    }
}

# Function to check and install dependencies
function Install-Dependencies {
    Write-Host "🔍 Checking dependencies..." -ForegroundColor Yellow
    
    $checkDeps = python -c "import google.generativeai, pandas, dotenv" 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
        pip install -r requirements.txt
        
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
            exit 1
        }
    } else {
        Write-Host "✅ All dependencies are installed" -ForegroundColor Green
    }
}

# Function to run the manager
function Invoke-Manager {
    param([string]$ManagerCommand)
    
    if ([string]::IsNullOrEmpty($ManagerCommand)) {
        Write-Host "✅ Starting interactive mode..." -ForegroundColor Green
        python qa_manager.py
    } else {
        Write-Host "✅ Running command: $ManagerCommand" -ForegroundColor Green
        python qa_manager.py $ManagerCommand
    }
}

# Main execution
try {
    # Parse arguments
    if ($Help) {
        Show-Help
    }
    
    $ManagerCommand = ""
    if ($Check) { $ManagerCommand = "--check" }
    elseif ($Demo) { $ManagerCommand = "--demo" }
    elseif ($Marathon) { $ManagerCommand = "--marathon" }
    elseif ($Merge) { $ManagerCommand = "--merge" }
    elseif ($Analyze) { $ManagerCommand = "--analyze" }
    elseif ($Clean) { $ManagerCommand = "--clean" }
    elseif ($Info) { $ManagerCommand = "--info" }
    elseif (-not [string]::IsNullOrEmpty($Command)) { $ManagerCommand = $Command }
    
    # Setup environment
    Test-Python
    Initialize-VirtualEnvironment
    Install-Dependencies
    
    # Run the manager
    Invoke-Manager $ManagerCommand
    
    Write-Host ""
    Write-Host "👋 Thank you for using QA Dataset Manager!" -ForegroundColor Cyan
    
} catch {
    Write-Host "❌ An error occurred: $_" -ForegroundColor Red
    exit 1
}
