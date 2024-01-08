import socket
import cv2
import numpy as np
import pyautogui
import pickle
import struct
import time
import logging
# Importing centralised Log File
from log_config import configure_logging_share_screen_server

# Configure logging
configure_logging_share_screen_server()


def run_live():
    logging.info(
        f"[SERVER] Server run_live() called at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Specify resolution
    resolution = (1920, 1080)

    # Create a socket to listen for connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 50506))
    server_socket.listen(5)

    logging.info("[SERVER] Image Server Peer is Listening...")

    # Accept a connection
    client_socket, addr = server_socket.accept()
    logging.info(f"[SERVER] Accepted connection from {addr}")

    while True:
        # Take screenshot using PyAutoGUI
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert it from BGR(Blue, Green, Red) to RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize the frame to a consistent size
        frame = cv2.resize(frame, resolution)

        # Get the size of the frame
        frame_size = struct.pack("Q", len(pickle.dumps(frame)))

        # Send the size and the frame to the client
        client_socket.sendall(frame_size + pickle.dumps(frame))

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # Release resources
    client_socket.close()
    server_socket.close()
    cv2.destroyAllWindows()


logging.info("[SERVER] Starting to share...")
run_live()
