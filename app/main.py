# This script was made by Grigorios Tsakalis.
# For further information and a fully detailed documentation please visit my repository at:
# https://github.com/GregJackalis/Share_Screen_Application/blob/main/Documentation.md


import subprocess
# from install_libraries import install_libraries


def run_app():
    subprocess.run(['python', 'app/gui_client.py'])


if __name__ == "__main__":
    # install_libraries()
    run_app()
