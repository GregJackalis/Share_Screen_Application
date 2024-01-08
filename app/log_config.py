# This script was made by Grigorios Tsakalis.
# For further information and a fully detailed documentation please visit my repository at:
# https://github.com/GregJackalis/Share_Screen_Application/blob/main/Documentation.md


import logging


# The purpose of this script and function is to create a centralised log file where the
# peer, the client_screen, and the server_screen script can use to log any info
def configure_logging_peer():
    logging.basicConfig(filename='Log_File_Peer.txt', filemode='w',
                        level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def configure_logging_share_screen_server():
    # Using filemode='w' to overwrite the existing log file
    logging.basicConfig(filename='Log_File_Share_Screen_Server.txt', filemode='w',
                        level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def configure_logging_share_screen_client():
    # Using filemode='w' to overwrite the existing log file
    logging.basicConfig(filename='Log_File_Share_Screen_Client.txt', filemode='w',
                        level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
