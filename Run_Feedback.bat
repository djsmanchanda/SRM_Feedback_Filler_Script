@echo off

rem Install pynput using pip
pip install pynput

rem Check if installation was successful (optional)
if %errorlevel% neq 0 (
    echo There was an error installing pynput.
    pause
    exit /b 1
)

rem Run feedback.py
python feedback.py

rem Pause at the end (optional)
pause
