# This script was made by Grigorios Tsakalis.
# For further information and a fully detailed documentation please visit my repository at:
# https://github.com/GregJackalis/Share_Screen_Application/blob/main/Documentation.md


# client.py
import socket
import cv2
import pickle
import struct
import time
import logging
import platform
import subprocess
# Importing centralised Log File
from log_config import configure_logging_share_screen_client

# Configure logging
configure_logging_share_screen_client()


def get_host_address():
    # Check the operating system and set the host address accordingly
    if platform.system() == 'Windows':
        return '127.0.0.1'  # localhost for Windows
    else:
        return '0.0.0.0'  # bind to all available interfaces for Linux/macOS


def run_live():
    logging.info(
        f"Client run_live() called at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Create a socket to connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((get_host_address(), 50506))
    logging.info("[CLIENT] Connected to the Share Screen Peer")

    # trying to install cv2 library again due to issues faced with windows os
    subprocess.run(['pip', 'install', 'opencv-python'], check=True)
    import cv2
    # Receive screen frames from the server
    while True:
        try:
            data = b""
            payload_size = struct.calcsize("Q")
            while len(data) < payload_size:
                packet = client_socket.recv(4 * 1024)
                if not packet:
                    logging.info("[CLIENT] Server Peer closed the connection.")
                    break
                data += packet

            if not data:
                print("No data received. Exiting.")
                break

            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                packet = client_socket.recv(4 * 1024)
                if not packet:
                    logging.info("[CLIENT] Server Peer closed the connection.")
                    break
                data += packet

            if not data:
                print("Incomplete frame data received. Exiting.")
                break

            frame_data = data[:msg_size]
            data = data[msg_size:]

            # Deserialize the frame
            try:
                frame = pickle.loads(frame_data)
            except EOFError:
                logging.info(
                    "[CLIENT] EOFError: Connection closed unexpectedly.")
                break
            except Exception as e:
                logging.info(f"[CLIENT] Error unpickling frame: {e}")
                break

            # Display the frame
            cv2.imshow('Live', frame)

            if cv2.waitKey(1) == ord('q'):
                break

        except KeyboardInterrupt:
            logging.info(
                "[CLIENT] Client closed from the user's command (Ctrl + C)")
            print("[CLIENT] Client closed from the user's command (Ctrl + C)")
            break

    # Release resources
    client_socket.close()
    cv2.destroyAllWindows()


print("Waiting for Remote Screen to be activated...")
time.sleep(3.5)
logging.info("[CLIENT] Remote Screen is ready. Connecting...")
run_live()
