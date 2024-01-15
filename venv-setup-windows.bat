@echo off

REM The requirements are installed in the virtual environment created by this script
REM Once the app is closed, the venv is deleted.
REM For more info on how to use this file please visit my documentation.

REM Set the virtual environment directory
set VENV_DIR=Share_Screen_Venv

REM Get the directory where the batch script is located
set SCRIPT_DIR=%~dp0

REM Change to the script's directory
cd /d "%SCRIPT_DIR%"

REM Check the operating system
if "%OSTYPE%" == "msys" (
    REM Windows
    python -m venv "%VENV_DIR%"
    call "%VENV_DIR%\Scripts\activate"

    REM Inform the user that the virtual environment is activated
    echo Virtual environment activated. You are now in the virtual environment.

    REM Deactivate the virtual environment when the user exits
    deactivate
) else (
    echo Unsupported operating system
    exit /b 1
)
