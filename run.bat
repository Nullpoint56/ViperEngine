@echo off
setlocal enabledelayedexpansion

echo [INFO] Starting script...
echo.

:: Step 1: Locate global Python
echo [INFO] Checking if Python is available in PATH...
where python >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Python not found in PATH. Please install Python or add it to your system PATH.
    exit /b 1
)
set PYTHON=python
echo [OK] Python found:
where python
echo.

:: Step 2: Create virtual environment if missing
if not exist ".venv" (
    echo [INFO] .venv folder not found. Creating virtual environment...
    %PYTHON% -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment. Ensure Python's venv module is available.
        exit /b 1
    )
    echo [OK] Virtual environment created successfully.
) else (
    echo [INFO] Existing virtual environment found.
)
echo.

:: Step 3: Activate virtual environment
echo [INFO] Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment.
    exit /b 1
)

:: Confirm Python path after activation
echo [INFO] Active Python interpreter:
where python
python --version
echo.

:: Step 4: Install dependencies
if exist "requirements.txt" (
    echo [INFO] Installing dependencies from requirements.txt...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Failed to install dependencies from requirements.txt.
        exit /b 1
    )
    echo [OK] Dependencies installed successfully.
) else (
    echo [WARNING] No requirements.txt found. Skipping dependency installation.
)
echo.

:: Step 5: Run main.py
if exist "main.py" (
    echo [INFO] Running main.py using virtual environment Python...
    %PYTHON% main.py
    if errorlevel 1 (
        echo [ERROR] main.py exited with an error.
        exit /b 1
    )
    echo [OK] main.py completed successfully.
) else (
    echo [ERROR] main.py not found in this folder.
    exit /b 1
)

echo.
echo [INFO] Script finished.
endlocal
pause

