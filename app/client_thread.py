from PyQt5.QtCore import QThread, pyqtSignal
import logging

FORMAT = 'utf-8'
HEADER = 1024

# Class used to maintain a thread when it comes to the Client-Side receiving messages from the
# Server-Side


class ClientThread(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, conn_socket):
        self.connetion_socket = conn_socket
        super().__init__()

    def run(self):
        while True:

            # Client Socket is used to receive messages
            msg = self.connetion_socket.recv(HEADER)

            if not msg:
                break

            try:
                decoded_msg = msg.decode(FORMAT)

                self.data_received.emit(decoded_msg)
            except:
                # Emitting the message it means that the value inside the parenthesis,
                # which is type str, will be sent to the function "process_received_data"
                self.data_received.emit('image')

        logging.info("[CLIENT] Thread has stopped running")
