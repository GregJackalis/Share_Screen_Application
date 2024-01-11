import subprocess
from install_libraries import install_libraries


def run_app():
    subprocess.run(['python', 'app/gui_client.py'])


if __name__ == "__main__":
    install_libraries()
    run_app()
