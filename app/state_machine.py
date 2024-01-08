# This script was made by Grigorios Tsakalis.
# For further information and a fully detailed documentation please visit my repository at:
# https://github.com/GregJackalis/Share_Screen_Application/blob/main/Documentation.md

# This is a simple state machine script used to "cover" a few
# lines of code in the peer script.
# It's much easier to handle each state in this function in a separate script than having
# each different case (based on the client-server side and the state the application is on)
# on the peer script.
def handle_message(msg):
    if '555' in msg:
        return 'login'

    if '7' in msg:
        return 'check_token'

    if '6' in msg:
        return 'share'

    if '3' in msg:
        return 'handle_verification_response'

    if '1' or '4' in msg:
        return 'handle_login_response'
