@echo off

REM The requirements are installed on the virtual invornment that is made
REM through this scripts and once the app is closed, the venv is deleted.
REM For more info on how to use this file please visit my documentation.

REM Set the virtual environment directory
set VENV_DIR=Share_Screen_Venv

REM Check the operating system
if "%OSTYPE%" == "msys" (
    REM Windows
    python -m venv "%VENV_DIR%"
    call "%VENV_DIR%\Scripts\activate"

    REM Change to the directory where your Python script is located
    cd "C:\Users\grigoriostsakalis\Desktop\College 2023-2024\Networks & Security (Python)\For Assignment\Assignment 1\Share Screen Application (GitHub)"

    REM Inform the user that the virtual environment is activated
    echo Virtual environment activated. You are now in the virtual environment.

    REM Deactivate the virtual environment when the user exits
    deactivate
) else (
    echo Unsupported operating system
    exit /b 1
)
