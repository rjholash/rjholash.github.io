@echo off
echo ===================================================
echo Publication Sync: BibTeX to CV.yml
echo ===================================================

:: Set script paths
set SCRIPT_DIR=%~dp0

:: Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python not found in PATH.
    echo Please install Python and try again.
    pause
    exit /b 1
)

:: Install required Python packages if not already installed
echo Installing required packages...
python -m pip install bibtexparser pyyaml

:: Run the sync script
python "%SCRIPT_DIR%bibtex_to_cv.py"

echo.
echo Sync process completed!
echo.

pause
