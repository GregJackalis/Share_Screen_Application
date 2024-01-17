<!-- This script was made by Grigorios Tsakalis.
For further information and a fully detailed documentation, please visit my repository at:
https://github.com/GregJackalis/Share_Screen_Application/blob/main/Documentation.md -->

# Share Screen Application Documentation
#### Created by Grigorios Tsakalis

## Introduction
This is the official documentation for the Share_Screen_Application.
This project was made for the Assignment on the Networks & Security module and its aim is to simulate a "Screen-Mirroring" Application, through the usage of Socket Programming in Python. In addition, authorization and data encryption needed to be used to make the application as safe and strong as possible, thus a variety of libraries and encryptions were used.<br><br>

## Target Audience
Whether you're a computer science student or just a coding enthusiast, this project contains all the scripts that were made from scratch by me! For any further information or questions related to my work please don't hesitate to email me at: [grig.tsakalis@mc-class.gr](mailto:grig.tsakalis@mc-class.gr)<br><br>

## Getting Started
The application includes nine Python Scripts, one .ui file, and other files (such as .env, requirements to be downloaded, and so on). The application started being made from the "Front-End" part which it was about setting up the GUI and the gui_client script. Then, it was time for Socket Programming to take place, and even though at first two different scripts (one for client and one for server) were made, I decided afterwards that I want to make as a Peer-to-Peer connection.<br>
Therefore, the peer.py script contains a class that can behave as a Client but also as Server, the only difference is that the Server is in charge for checking the credentials- using the the authentication.py script- and to also start sharing their screen once everything is set up. The client's behaviour attributes on the other hand, gives the user the ability to try and sign in as many times as they want and once the credentials are correct, to connect to the remote screen.<br><br>

## Features
The application implements a variety of features and technologies, such as:
1) **Socket Programming**: The application uses a Peer-to-Peer model of socket programming. I achieved this by making a singular app peer.py that includes a Class "Peer", in which class a variety of attributes are used in order to make the class behave as a Client or Server.

2) **JTW Token**: This libary was used in order to make a Verfication Token and "lock" the possibility of a User (on the Client Side) to connect to the Server and spectate their screen. The token is made from three parts, and information for the data used for these parts is saved in a .env file:<br>
&nbsp;&nbsp; - The header that includes the type of algorithm and token. <br>
&nbsp;&nbsp; - The payload which includes the data that we want to encrypt and also connect with the token (this data could be a specific username with an authorized/verified password). <br>
&nbsp;&nbsp; - The signature which is made from the header, payload, and signature. <br>

3) **Hashing**: To decrease the possibility of an attacker breaching my application, I decided to use an combination of ways to encrypt data. In the auth.py script where the JWT Token libary is implemented along with a few functions, Hashing Encryption is also implemented and used. It is used to hash the saved passwords, so that even in case the attacker gets through, it won't be able to see the sensitive information. More information about it can be found on the auth.py script explanation later on.

4) **Vignere Cipher**: On top of hashing and using a JWT Token, I decided to also encrypt the data that is transmitted through the Client and the Server. The cipher is called along with its encryption and decryption functionalitis, while also in order for the cipher to be implemented, a secret key needs to be used. Again, just like with the JWT Token, the key  is stored in a .env file and the vignere_cipher.py script uses that key to do all the encryptions and decryptions.

4) **PyQt GUI**: Using the PyQt5 Library and the QtDesigner application, I made my own interface to help the Client's have a better and more simplified understanding of the app and its functionality. Through the interface, and properly naming my GUI elements, I gave functionality to the buttons and blank fields. The functionality of these elements is then connected with the Peer-to-Peer model.

5) **Log Files**: Log Files are made through the log_config.py script. Then, other scripts implement the log files feature in order to log information into 3 different .txt type files: one for the peer to peer connection, one for the client screen side, and one for the server screen side.

6) **Add-Ons**: <br>
- In order for the application to run, requirements need to be installed, and this is achieved by using the subprocess library to install the requirements needed.
- For the share screen process, two different scripts are used which both of them implement a simple Client-Server model to send image data and also show them on the screen.
- In order for each side to understand on which state the application is currently on, a state machine is used, while also specific numbers are sent with the data, to Client and Server. The state machine feature helps the two sides understand on which state (and which function to use) based on the number that they receive in their received data. <br><br>


## Testing
I run my program through a couple of softwares to test its security and integrity, while also run some custom tests at home and at uni. Different scenarios where used on different types of computers, trying to find as many "holes" in my program as possible. After a lot of tests since the very beginning of this project up to this point, the application is fully runnable and as safe as possible. <br>
- **The information that is logged on my program is about the Serve side, and can be:**<br>
    2024-01-112024-01-11 12:15:10,985 - INFO - Connected to ('127.0.0.1', 50001)<br>
    2024-01-11 12:15:17,798 - INFO - [SERVER] Client with address ('127.0.0.1', 50001) has lost connection.<br>
    2024-01-11 12:15:17,798 - INFO - [SERVER] Server is not waiting for messages anymore
    0,911 - DEBUG - push QWidget centralwidget<br>
- **Also information about the Client is logged, and it's in this format:**<br>
    2024-01-11 12:45:40,124 - INFO - [CLIENT] Successfully connected to Server!<br>
    2024-01-11 12:45:44,086 - INFO - [CLIENT] Correct Credentials!<br>
    2024-01-11 12:45:45,314 - INFO - [CLIENT] User verification succedeed!<br>
- **And also information about the Sharing Screen Process is logged and it looks like this:**
    2024-01-11 12:45:50,273 - INFO - [CLIENT] Remote Screen is ready. Connecting...<br>
    2024-01-11 12:45:50,273 - INFO - Client run_live() called at 2024-01-11 12:45:50<br>
    2024-01-11 12:45:50,274 - INFO - [CLIENT] Connected to the Share Screen Peer<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OR**<br>
    2024-01-11 12:45:47,105 - INFO - [SERVER] Starting to share...
    2024-01-11 12:45:47,105 - INFO - [SERVER] Server run_live() called at 2024-01-11 12:45:47
    2024-01-11 12:45:47,106 - INFO - [SERVER] Image Server Peer is Listening...<br><br>



## How to Run
1) First of all, python version 3.11.5 needs to be installed on the computer (along with its built-in pip-library)

2) Once python is set up on the computer, you will need to create a **Virtual Environment**:
- If you're on **MacOS** then you should run the **venv-setup-mac.sh** file (NOTE: To double click and run the .sh file on MacOS, you will need to Right Click on the File, then press "Get Info" and then on the "Open with:" selection, you should choose the Terminal app)

- If you're on **Windows** then you should run first the **venv-setup-windows.bat** file. <br>
**BUT** because of issues with windows os, for the application to successfuly run without any errors, it is advisable to **NOT** use a virtual environemnt. Try installing the libraries locally and running the scripts locally as well.


4) Then the requirements of the application need to be installed before running the app. <br>
In order for the requirements and libraries to be installed run this command: python app/install_libraries.py <br>
(NOTE: I originally put the libraries installation on the main script so that the requirements will be installed automatically but because of windows taking a bit longer to install all the requirements for each time the application starts to run, I decided it would be faster if the install_libraries.py script was run first before the actual application) <br><br>


**Great! Now you're ready to run the application!** <br>
**Run the main.py script:** <br>
 - This can happen by running on the Virtual Environment "Share_Screen_Venv" (or locally after installing the libraries) the command:
        &nbsp;&nbsp;python app/main.py

### NOTE: Due to windows and mac differences and issues I came accross (for issues I found on windows):
- I had to make a new function that checks the operating system that the script is running on, so that the appropriate local address is used.
- In case the PyQt5 module cannot be found even though it has been downloaded successfully, instead of running the main.py script, try to run this command to start the application: python app/gui_client.py <br>

- In case the application works fine but on the share screen process it doesn't work due to modules not being found (or something else), as I mentioned before, please install the requirements locally by running the commands: <br>
python app/install_libraries.py <br>
and <br>
python app/main.py <br>
on the terminal of the application's folder (right click while in project's folder and choose the option "Open in Terminal")

- After finishing running the application you should run the script uninstall_libraries in order to clean up your pc from the libraries you just installed: python app/uninstall_libraries.py


- Once the gui_client.py script is running, a text will pop up asking the user to choose whether they want to: <br>

**"Share their Screen" (act as a Server)**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;or <br> 
**See Shared Screen (act as a Client)** <br><br>

- When the Graphical Interface pops up on the screen, the User will be asked to etner a username and a password. This data is pre-made and are the following:<br>
&nbsp;&nbsp;&nbsp; **Username**: gregory &nbsp;&nbsp; **Password**: 12345678 <br>
&nbsp;&nbsp;&nbsp; **Username**: jackalis &nbsp;&nbsp; **Password**: logmein <br>
&nbsp;&nbsp;&nbsp; **Username**: socket.programming &nbsp;&nbsp; **Password**: 15012024





## Scripts and their Purpose

### main.py
-----------------------------------------------------------------------------------------------------
This script was made to centalize the application's start up process and also call the script that's responsible for installing the requirements of the app. The way it works, is that it first uses the install_libraries() function from the install_libraries.py script, and then it implements a simple run_app() function to run the gui_client.py script, which will therefore trigger the starting process of the actual application.

### my_gui.ui
-----------------------------------------------------------------------------------------------------
This file was exported from the Qt Designer app that I used in order to build my own User Interface and even name my elements- so that I can use them later-on on my application. Once the making of the GUI was done, it was time to use it on my Python project.<br><br><br>


### gui_client.py
-----------------------------------------------------------------------------------------------------
This is the "main" script of my project, meaning that it needs to be run first. This script "connects"" the GUI that I've already made, with the Peer script that contains both Client and Server behaviours. What it does is that it gives functionality to the button on the Interface, then based on the button that is pressed (and if the user has chosen to be the user of course by entering 2 on the terminal) the interface imports and uses Client behaviour attributes- by making a Peer class instance- to send data to the server but also wait and handle a response.<br>
However, if the user enters 1 on the terminal when running this script, the user will enter Share Screen mode, a.k.a. the user will be the Server- by making a Peer class instance as well- and then the Server behaviour attributes will come in and await for a Client to Connect.<br><br><br>


### peer.py
-----------------------------------------------------------------------------------------------------
This is the second most important script of my project, and it's the one responsible for a secure and reliable connection between Client and Server using Socket Programming principles. The script includes a class with the name "Peer" is where all of this application's socket programming is included:

### Server behaviour attributes:
- __Listen function__: It's used to listen for Clients that are trying to connect to the Server's address and port, and also handle messages using a function made in the state_machine.py script. Then, once handle_message function has returned the correct response, it is time for the right function to be called too. <br><br>
- __Login function__: It's used to receive the credentials the Client sends to login. In this function, by using an if-statement and functions that are imported from the auth.py scripts, the credentials are thoroughly decrypted using the vignere cipher, then encrypted again to match the already hashed passwords that are saved in a .env file...and then finally a response is sent to the Client. <br><br>
- __Check_Token Funciotn__: This function that is also called through the "handle_message" function, is used to check if the token that the Client has is valid. If the user hasn't signed in successfully, then they have **None** as a token, which is not valid. Also in case of an attacker making a fake one by changing small details in the token's format, the token that will be made will be completely different than the correct one, so the app is well secured and safe. <br>The token feature was inspired from additional studies done beyond my university's scope. The application implements the JWT library which I used in my authentication.py script, which is responsible for my application's security (more details about the script can be found later on). <br><br>
- __Share Function__: It's used only in case the token passed from the Client is valid, and it's called from the **handle_message** function too. This function sends a response to the Client, notifying them that the Screen Sharing process is about to begin. After that message is sent, then the **subprocess** command is run and the **server_screen.py** script is run (more details about the server_screen.py script later on). <br><br>

### Client behaviour attributes:
- __Connect_to_Server function__: It's used to connect to the server and it's the very first function called when on the gui_client.py script's terminal the number 2 is entered. I chose to make it like this so that as soon as the Graphical Interface is loaded to the Client's screen, the client side has already connected to the server. It is also better in terms of not breaking the application, in case a server is not found for the client to connect to (because try...except blocks are used in this function). <br>
In addition, in this function is where the ClientThread class is used to start a thread between the client and the server. <br><br>
- __Process_Received_Data function__: This function is used in combination with the thread, and it's basically the response handler of the client's side. This function also uses the handle_message function from the "state_machine" script, which returnes the name of the function that needs to be used to handle the server's response correctly. Also, in the very last stage when the server is starting the Share Screen Process, a specific value is sent which when the client receives it, the Client also starts the Share Screen process from their side (the subprocess command is used in this case as well, in order to start the Share Screen Process). <br><br>
- __Handle_Login_Response function__: This function is used to handle the server's login respone. The reason a function was made for such specific scenario is so that depending on the server's response, the correct information will be logged into a file and also get printed as a message box on the Client's Screen. <br><br>
- __Handle_Verification_Response function__: This function is essential, since it triggers the Share Screen Process. It's implementation logic is the same as the handle_login_response, with the only difference that once the token is valid and a True response is returned, the function "send_share_msg" is called (more information about the send_share_msg function can be found later on). <br><br>
- __Try_to_Login function__: This function is used directly from the Graphical Interface on the gui_client.py script. This function is the one responsible for taking the login credentials that the user has entered, and sending them to the Server for further validation. <br><br>
- __Check_Action function__: This function is used just like the function mentioned above. The gui_client.py script imports and uses this function to send the User's token (None in case the user doesn't have a token) to the Server for futher validation. Then from that point, if the token is valid, the handle_verification_response function is used to trigger the Share Screen Process. <br><br>
- __Send_Share_msg function__: This function as mentioned aboved, is only callable through the handle_verification_response function. This function is responsible for notifying the Server that the Client has received the "Valid Token" function, the user is notified of that (through a message box that popped up), and the Server needs to start its side for the Share Screen Process- meaning that the subprocess command needs to be run. <br><br>
- __Close_Connection function__: This funtion is used fromt the close buttons used in the Graphical Interface, so that the socket connection and the application is closed and handled gracefully without breaking the app or the Server-Side <br><br>
- __Make_Box function__: This funtion is used to save a few lines of code when it comes to make a pop-up message box on the User Interface. It takes a message as a parameter, and then using elements from the PyQt5 library, a message box is made and showed with that message. <br><br><br>



### client_thread.py
-----------------------------------------------------------------------------------------------------
This script is used to create a Class that handles the threading part between the Client and the Server so that the Client will always await a response from the Server, while also checking if there is still a connection. The reason this script was made, was to distribute the application's functionality into more parts, making it more readable and organized.


### vignere_cipher.py
-----------------------------------------------------------------------------------------------------
This script implements the vignere cipher algorithm, which my application uses when sending data from the Client side to the Server and back. At first, I settled in with the JWT library and the hashing method but I realised that there was a small "window" for breachers, and that was transmitting sensitive data through both sides. Thus, whenever sensitive information is sent, such as a token or login credentials, the data is encrypted and then decrypted with a secret key. Keep in mind, the secret key along with other essentail security-related information, are saved in a .env file. <br><br><br>


### auth.py
-----------------------------------------------------------------------------------------------------
This script is the "core" of my application's security. It includes the JWT token along with its functions. 
- First of all, the Secret Key, Algorithm, and everything else related to the making of the token, are saved in a **.env file** and are accessed only by using the dotenv library, making it extra secure since no file names are used.<br>
- Secondly, the **create_access_token** function which is only used when the given credentials are correct, is responsible for the making of the token. This happens, by combining the given data in a dictionary, a secret key, and an algorithm (Keep in mind, the token in general is made out of thrree parts, for more information on JWT, go to the [JWT Documentation](https://jwt.io/introduction)) <br>
- In addition, the **verify_access_token** function is used to check whether the Client's token is valid or not. Again, this function implements methods from the JWT library.
- The **hash_password** function is used to hash any value given to it. The .gensalt() command generates a random salt, meaning a random value used as additional input to the value given, that needs to be hashed. After that, the .hashpw() method is used to hash the given value.
- The **check_password** function is used by the Server when receiving credentials from the Client, and what it does is that it implements the .checkpw() method from the bcrypt library. What this method does is that it hashes the given value the same way as the pre-hashed and saved values, and then it checks if the hashed values are the same. Then, based on the result True or False is returned. For more information on the bcrypt library, go to the [bcrypt Documentation](https://www.npmjs.com/package/bcrypt).<br>
- The auth.py script also includes the authentication class's instance, along with the dictionary of the pre-made users of the application. Of course this is a very wrong practise in real-world scenarios, but for educational purposes I decided that it'd suit better to have such list in the auth.py script.<br><br><br>


### state_machine.py
-----------------------------------------------------------------------------------------------------
This script contains a very simply function that handles messages for both server and client. It works in a way that based on the format and a number sent with each message, a specific state will also be returned. The state that is returned, is a string-type value that contains a function name. That string value can then be used straight away by using the getattr()() method, in which in the first parenthesis the string value is passed (along with the self keyword if its about a classes attribute), and in the second parenthesis the parameters that we want to pass to the function are written.<br><br><br>


### server_screen.py
-----------------------------------------------------------------------------------------------------
This script first of all uses a function from the log_config.py script which is responsible for logging information (more information about the log_config.py script later on). Then, using the run_live() function, it sets up a socket so that that original ones between the peers is not interupted, it sets up the resolution of the screen sharing, and then it finally enters the "while True" loop in which screenshots of the screen are continiously captured, coloured, resized and sent to the client. The loop also contains a condition, where if the q button is pressed, the screen sharing will be ended<br><br><br>


### client_screen.py
-----------------------------------------------------------------------------------------------------
This script is run from the subprocess command on the peer.py script (just like the server_screen.py script) and what it does is that it first waits 3.5 seconds for the server image socket to start running, and then connect (this time.sleep() command was used due to issues that were made because of the sockets running at the same time). The script also implements a method to log information, while also creates a new socket at the same address and port as the image-server.<br>
In the "while True" loop, the client awaits for incoming image data continiously, while also using try-except block to gracefully exit the loop in case an error occurs. Then, the size of the payload is determined, where "Q" represents an unsigned long long integer (8 bytes) After the payload size is determined from the all the data received, then it extracts the packet message size. In the second "while True" loop, it receives the actual frame data until it accumulates enough bytes and then the frame data are extracted. Lastly, by using the frame_loads method, it transforms the frame data into a Python object, and then the frame is finally showed using the OpenCV library.<br><br><br>


### log_config.py
-----------------------------------------------------------------------------------------------------
This script contains three different functions, each one responsible for logging information to different .txt files. The first function is about the Client and Server Peers, and every information related to that connection is logged to a "Log_File_Peer.txt" file, which gets overwritten everytime the program is run. The last two functions, are used in the Share Screen Process to log information independently for the Server-Image side and the Client-Image side. I explicitly chose to use two different functions and to create separate log files for each, because unlike in the Peer script, the data that are sent between the two side in the Share Screen Process are fast and a lot, resulting in one side overwriting information for the other side. <br><br><br>


### install_libraries.py
-----------------------------------------------------------------------------------------------------
This script is used to create a function that will take care the setup of the application on the machine that is running. In order for the application to run, the correct libraries on the correct versions need to be installed, and that's what this script does by using the requirements.txt file + a few other libraries that are explicitly installed, in order make the program run error-free.<br><br><br>

### uninstall_libraries.py
-----------------------------------------------------------------------------------------------------
This script is used explicitly from windows user in order to uninstall the libraries that were installed locally. This script was made due to issues I faced when testing my application on a windows machine. The usage of a virtual environment wasn't working so the best solution is to just install the libraries and run the scripts locally on the computer. Once the user is done with the application, they can use this script that will automatically clean up their machine from the application's library.<br><br><br>

### venv-setup-mac.sh && venv-setup-windows.bat
-----------------------------------------------------------------------------------------------------
These scripts are used to make a temporary Virtual Environment so that when the requirements and libraries of the application are installed, they won't get stored in the machine. Then on the venv that is made and is opened in the terminal, the "python app/main.py" command needs to be run to trigger the setting-up process of the applicaition. Once the terminal is closed where the Virtual Environment is running, the venv will be deactivated and deleted.