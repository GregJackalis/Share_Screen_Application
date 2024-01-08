# This script was made by Grigorios Tsakalis.
# For further information and a fully detailed documentation please visit my repository at:
# https://github.com/GregJackalis/Share_Screen_Application/blob/main/Documentation.md


import subprocess
import importlib


def install_libraries():
    try:
        with open('requirements.txt', 'r') as file:
            libraries = file.read().splitlines()

        for library in libraries:
            try:
                importlib.import_module(library)
                print(f"{library} is already installed.")
            except ImportError:
                subprocess.run(['pip', 'install', library], check=True)
                print(f"{library} installed successfully!")

        print("All libraries checked and installed or already present.")

    except Exception as e:
        print(f"Error during installation: {e}")

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
