# This script was made by Grigorios Tsakalis.
# For further information and a fully detailed documentation please visit my repository at:
# https://github.com/GregJackalis/Share_Screen_Application/blob/main/Documentation.md


from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from peer import Peer as peer


class GUI_Client(QMainWindow):

    # class constructor
    def __init__(self):
        super(GUI_Client, self).__init__()
        self.client_instance = client_instance
        self.setup_ui()

    def setup_ui(self):
        uic.loadUi("app/my_gui.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.handle_login)
        self.connect_desktop_btn.clicked.connect(self.screen_share)
        self.actionClose.triggered.connect(self.close_connection)

    def handle_login(self):
        try:
            print("Login button clicked")
            client_instance.try_to_login(
                self.lineEdit.text(), self.lineEdit_2.text())
        except Exception as e:
            print(f"Error in handle_login: {e}")

    def screen_share(self):
        try:
            print("Connect to Desktop button pressed!")
            client_instance.check_action()
        except Exception as e:
            print(f"Error in screen_share: {e}")

    def close_connection(self):
        client_instance.close_connection()


action = input("""\n\n\n\nPress 1 to Share Screen\nPress 2 to see Shared Screen\n
               (REMEMBER: The app will work only in case there is a desktop/user sharing their screen)\n\nInput: """)
if action == '1':
    server_instance = peer(None)
    server_instance.listen()
elif action == '2':
    app = QApplication(sys.argv)
    client_instance = peer(None)
    gui_client_instance = GUI_Client()
    client_instance.gui_window = gui_client_instance

    client_instance.connect_to_server()
    messageBox = QMessageBox
    app.exec_()
else:
    print("Invalid input! Please run the program again and type \"1\" or \"2\" ")
    exit(0)
