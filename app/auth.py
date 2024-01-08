from jose import jwt, JWTError
from datetime import datetime, timedelta
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

# Sensitive information (Secret Key, Algorithm, Expiration Time) stored in a .env file
# for enhanced security.
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
FORMAT = 'utf-8'


class Authentication:

    def __init__(self):
        pass

    # Once the Login Credentials are correct, an access token is generated for the user.
    # This token allows specific actions, such as connecting to the remote screen
    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    # This function is called from the Server-Behaviour when the "Connect to Desktop" button is pressed.
    # It checks whether the given token (the token the user has, if they have any) is valid. By valid,
    # it means that it is NOT None and it has the same format (secret key, algorithm, etc) as the one specified
    # in the .env file.
    def verify_access_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return True
        except JWTError:
            # Handle invalid token
            return False

    # This function is used to hash the passwords that are given for each pre-made users below.
    # This feature enhances the security of the application.
    def hash_password(self, password):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(FORMAT), salt)

        return hashed_password

    # This function is used when the Server is checking if the given password from the user
    # is the same as the hashed password stored in the "users" dictionary.
    # After this step is completed, an access token is made for the user to use.
    def check_password(self, entered_password, hashed_password):
        # Check if the entered password matches the stored hashed password
        return bcrypt.checkpw(entered_password.encode(FORMAT), hashed_password)


# Authentication Instance
auth_instance = Authentication()
users = {"gregory": auth_instance.hash_password("12345678"),
         "jackalis": auth_instance.hash_password("logmein"),
         "socket.programming": auth_instance.hash_password("15012024")}
