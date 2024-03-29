# This script was made by Grigorios Tsakalis.
# For further information and a fully detailed documentation please visit my repository at:
# https://github.com/GregJackalis/Share_Screen_Application/blob/main/Documentation.md


import subprocess
import importlib


def install_libraries():
    try:
        importlib.import_module('PyQt5')
        print(f"PyQt5 is already installed.")
    except ImportError:
        subprocess.run(['pip', 'install', 'PyQt5'], check=True)
        print(f"PyQt5 installed successfully!")

    try:
        importlib.import_module('python-dotenv')
        print(f"python-dotenv is already installed.")
    except ImportError:
        subprocess.run(['pip', 'install', 'python-dotenv'], check=True)
        print(f"python-dotenv installed successfully!")

    try:
        importlib.import_module('python-jose')
        print(f"python-jose is already installed.")
    except ImportError:
        subprocess.run(['pip', 'install', 'python-jose'], check=True)
        print(f"python-jose installed successfully!")

    try:
        importlib.import_module('opencv-python')
        print(f"opencv-python is already installed.")
    except ImportError:
        subprocess.run(['pip', 'install', 'opencv-python'], check=True)
        print(f"opencv-python installed successfully!")

    try:
        importlib.import_module('bcrypt')
        print(f"bcrypt is already installed.")
    except ImportError:
        subprocess.run(['pip', 'install', 'bcrypt'], check=True)
        print(f"bcrypt installed successfully!")

    try:
        importlib.import_module('pyautogui')
        print(f"pyautogui is already installed.")
    except ImportError:
        subprocess.run(['pip', 'install', 'pyautogui'], check=True)
        print(f"pyautogui installed successfully!")


install_libraries()
