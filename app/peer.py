# This script was made by Grigorios Tsakalis.
# For further information and a fully detailed documentation please visit my repository at:
# https://github.com/GregJackalis/Share_Screen_Application/blob/main/Documentation.md


from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox
from vignere_cipher import cryptography
import socket
import subprocess
from state_machine import handle_message
from auth import auth_instance, users
import logging
# Importing centralised Log File
from log_config import configure_logging_peer
from client_thread import ClientThread

# Configure logging
configure_logging_peer()

# These are the constant variables needed to:
# a) Encode and decode message
# b) A header for general messages, so that when receiving messages
#    there is a specific "cap" on the bytes of the message.
FORMAT = 'utf-8'
HEADER = 1024

# -------------------------------------------------------------------------------------------------------------------------


class Peer:
    def __init__(self, gui_window):
        self.client_token = None
        self.gui_window = gui_window

        # IP Address and Ports used by both Client-like and Server-like behaviours
        self.host = '0.0.0.0'
        self.port = 50501

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------

    # SERVER BEHAVIOUR
    def listen(self):
        self.socket.bind((self.host, self.port))

        # Accepts only 1 Client because the Server can Share their Screen to only one Client
        self.socket.listen(1)
        logging.info("Server is open and listening...")

        self.server_connection_socket, address = self.socket.accept()
        logging.info(f"Connected to {address}")

        while True:
            try:
                message = self.server_connection_socket.recv(
                    HEADER).decode(FORMAT).strip()

                if not message:
                    logging.info(
                        f"[SERVER] Client with address {address} has lost connection.")
                    self.server_connection_socket.close()
                    break

                info_list = message.split(',')
                print("Received info list:", info_list)

                if len(info_list) == 3:
                    server_action = handle_message(info_list)

                    # calling the function that is returned from the state machine function
                    getattr(self, server_action)(info_list[0], info_list[1])
                else:
                    print("Invalid info list length:", len(info_list))
            except OSError as e:
                if e.errno == 9:
                    logging.info(
                        f"[SERVER] Client with address {address} has lost connection.")
                    self.server_connection_socket.close()
                self.listen()
        logging.info("[SERVER] Server is not waiting for messages anymore")

    # Function used to check login credentials passed from the user and through the client socket
    # The "if-statement" first checks whether the given username is inside the "users" list.
    # Then, it first decrypts the password using the vignere cipher, and then using the check_password function
    # it checks whether the password given is in the pre-made "users" list
    def login(self, username_input, password_input):
        if username_input in users and auth_instance.check_password(cryptography.decrypt(password_input), users[username_input]):
            result = self.server_connection_socket.send(
                f'{auth_instance.create_access_token({username_input: password_input})},1'.encode(FORMAT))
            # logging.info(f"[SERVER] sendall result: {result}")

        else:
            result = self.server_connection_socket.send(
                'ERROR,4'.encode(FORMAT))
            # logging.info(f"[SERVER] sendall result: {result}")

    # Function used to check if the user's token is valid

    def check_token(self, sample, token):
        result = self.server_connection_socket.send(
            f'{auth_instance.verify_access_token(token)},3'.encode(FORMAT))
        # logging.info(f"[SERVER] sendall result: {result}")

    # Function used to start the Share Screen Process

    def share(self, sample1, sample2):
        result = self.server_connection_socket.send("image".encode('utf-8'))
        # logging.info(f"[SERVER] sendall result: {result}")
        subprocess.run(['python', 'app/server_screen.py'])

# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------

    # CLIENT BEHAVIOUR
    def connect_to_server(self):
        self.socket.settimeout(10)  # Set a timeout of 10 seconds
        try:
            self.socket.connect((self.host, self.port))
            logging.info("[CLIENT] Successfully connected to Server!")

            self.thread = ClientThread(self.socket)
            self.thread.data_received.connect(self.process_received_data)

            if not self.thread.isRunning():
                self.thread.start()

        except socket.error as e:
            logging.info(f"Error: {e}")
        finally:
            # Reset the timeout to None (blocking)
            self.socket.settimeout(None)

    def process_received_data(self, message):
        parts = message.split(',')
        if len(parts) == 2:
            client_action = handle_message(parts)

            # calling the function that is returned from the state machine function
            getattr(self, client_action)(parts[0])
        elif message == "image":
            subprocess.run(['python', 'app/client_screen.py'])
            end = str(input())
            if end == 'q':
                self.close_connection()

    # Function used to handle the response from the server when it comes
    # to login and credentials the user input
    def handle_login_response(self, token):
        if token == 'ERROR':
            logging.info("[CLIENT] Incorrect Credentials!")
            self.make_box("Incorrect Credentials!")
        else:
            logging.info("[CLIENT] Correct Credentials!")
            self.client_token = token
            self.make_box("Succesfully Logged in!")

    # Function to handle the response from the server when it comes
    # to pressing the button to connect to the Shared Screen
    def handle_verification_response(self, response):
        if response == 'True':
            logging.info("[CLIENT] User verification succedeed!")
            self.make_box("Authentication Verified!")
            self.send_share_msg()
        else:
            logging.info("[CLIENT] User verification failed!")
            self.make_box("User Verification Failed!")

    # Function used from the Client GUI for Login
    def try_to_login(self, username, password):
        try:
            result = self.socket.sendall(
                f'{username},{cryptography.encrypt(password)},555'.encode(FORMAT))
            # logging.info(f"[CLIENT] sendall result: {result}")
        except Exception as e:
            logging.info(
                f"[CLIENT] Error sending message to server on Try to Login function: {e}")

    # Function used from the Client GUI for Connecting to Shared Screen
    def check_action(self):
        try:
            result = self.socket.sendall(
                f"checktoken,{self.client_token},7".encode(FORMAT))
            # logging.info(f"[CLIENT] sendall result: {result}")
        except Exception as e:
            logging.info(
                f"[CLIENT] Error sending message to server on Check Action function: {e}")

    # Function used to "ignite" the Share Screen Process
    def send_share_msg(self):
        try:
            result = self.socket.send('screen,share,6'.encode(FORMAT))
            # logging.info(f"[CLIENT] send result: {result}")

        except Exception as e:
            logging.info(
                f"[CLIENT] Error sending message to server on Send Share Msg function: {e}")

    # Function used to close the application and the socket connection with the Server
    def close_connection(self):
        self.socket.close()
        QCoreApplication.quit()

    # Function used to make message boxes of the responses the Server sends
    # to the client
    def make_box(self, msg):
        messageBox = QMessageBox()
        messageBox.setText(msg)
        messageBox.exec_()
