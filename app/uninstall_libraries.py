import subprocess


def uninstall_libraries():
    libraries_to_uninstall = [
        'PyQt5',
        'python-dotenv',
        'python-jose',
        'opencv-python',
        'bcrypt',
        'pyautogui'
    ]

    for library in libraries_to_uninstall:
        try:
            subprocess.run(['pip', 'uninstall', '-y', library], check=True)
            print(f"{library} uninstalled successfully!")
        except subprocess.CalledProcessError:
            print(f"Error uninstalling {library}")


if __name__ == "__main__":
    uninstall_libraries()
