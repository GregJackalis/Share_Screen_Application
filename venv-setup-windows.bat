@echo off

set VENV_NAME=share_screen_venv

echo Creating virtual environment %VENV_NAME%...
python -m venv %VENV_NAME%

echo Activating virtual environment %VENV_NAME%...

if "%OS%"=="Windows_NT" (
    call %VENV_NAME%\Scripts\activate.bat
) else (
    source %VENV_NAME%/bin/activate
)

echo Virtual environment %VENV_NAME% is now active.

cmd /k
