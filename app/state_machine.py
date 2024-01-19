# This script was made by Grigorios Tsakalis.
# For further information and a fully detailed documentation please visit my repository at:
# https://github.com/GregJackalis/Share_Screen_Application/blob/main/Documentation.md

# This is a simple state machine script used to "cover" a few
# lines of code in the peer script.
# It's much easier to handle each state in this function in a separate script than having
# each different case (based on the client-server side and the state the application is on)
# on the peer script.
from log_config import configure_logging_state_machine
import logging


def handle_message(msg):
    configure_logging_state_machine()
    if '555' in msg:
        logging.info(
            "Application is on Login State. Client has sent their credentials to the Server to check them")
        return 'login'

    if '7' in msg:
        logging.info(
            "Application is on the Check Token State. User has pressed the \"Connect to Server\" button and has sent their access token to the Server to check it if it's valid")
        return 'check_token'

    if '6' in msg:
        logging.info(
            "The application is in the state where the share screen process is starting. The user sents a message to the server saying to it to start sharing its screen")
        return 'share'

    if '3' in msg:
        logging.info(
            "Application is on the Token Verification State. The server sends a response back to the Client about the validation of the client's access token")
        return 'handle_verification_response'

    if '1' or '4' in msg:
        logging.info(
            "Application is on the Login Response State. The server sends information back to the client, whether the user's credentials were valid or not")
        return 'handle_login_response'
