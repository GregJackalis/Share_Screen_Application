# Share Screen Application Documentation
#### Created by Grigorios Tsakalis

## Introduction
This is the official documentation for the Share_Screen_Application.
This project was made for the Assignment on the Networks & Security module and its aim is to simulate a "Screen-Mirroring" Application, through the usage of Socket Programming in Python. In addition, authorization and data encryption needed to be used to make the application as safe and strong as possible, thus a variety of libraries and encryptions were used.

## Purpose and Target Audience
Whether you're a computer science student or just a coding enthusiast, this project contains all the scripts that were made from scratch by me! For any further information or questions related to my work please don't hesitate to email me at: [grig.tsakalis@mc-class.gr](mailto:grig.tsakalis@mc-class.gr)

## Getting Started
The application includes nine Python Scripts, one .ui file, and other files (such as .env, requirements to be downloaded, and so on). The applicaiton started being made from the "Front-End" part which it was about setting up the GUI and the gui_client script. Then, it was time for Socket Programming to take place, and even though at first two different scripts (one for client and one for server) were made, I decided afterwards that I want to make as a Peer-to-Peer connection.<br>
Therefore, the peer.py script contains a class that can behave as a Client but also as Server, the only difference is that the Server is in charge for checking the credentials- using the the authentication.py script- and to also start sharing their screen once everything is set up. The client's behaviour attributes on the other hand, gives the user the ability to try and sign in as many times as they want and once the credentials are correct, to connect to the remote screen.

## Scripts and their Purpose
### my_gui.ui
This file was exported from the Qt Designer app that I used in order to build my own User Interface and even name my elements- so that I can use them later-on on my application. Once the making of the GUI was done, it was time to use it on my Python project.

### gui_client.py
This is the "main" script of my project, meaning that it needs to be run first. This script "connects"" the GUI that I've already made, with the Peer script that contains both Client and Server behaviours. What it does is that it gives functionality to the button on the Interface, then based on the button that is pressed (and if the user has chosen to be the user of course by entering 2 on the terminal) the interface imports and uses Client behaviour attributes- by making a Peer class instance- to send data to the server but also wait and handle a response.<br>
However, if the user enters 1 on the terminal when running this script, the user will enter Share Screen mode, a.k.a. the user will be the Server- by making a Peer class instance as well- and then the Server behaviour attributes will come in and await for a Client to Connect.

### peer.py
This is the second most important script of my project, and it's the one responsible for a secure and reliable conenction between Client and Server by using Socket Programming principles. The script includes two classes:
1) The first called **ClientThread** is used to create a thread between the Client and the Server so that the Client will always await a response from the Server (while also checking if there is still a connection and an ucoming message of course).

2) The second class with the name "Peer" is where all of this application's socket programming is included. <br>
    ### Server behaviour attributes:
    - __Listen function__: It's used to listen for Clients that are trying to connect to the Server's address and port, and also handle messages using a function made in the state_machine.py script. Then, once handle_message function has returned the correct response, it is time for the right function to be called too. <br><br>
    - __Login function__: It's used to receive the credentials the Client sends to login. In this function, by using an if-statement and functions that are imported from the auth.py scripts, the credentials are thoroughly decrypted using the vignere cipher, then encrypted again to match the already hashed passwords that are saved in a .env file...and then finally a response is sent to the Client. <br><br>
    - __Check_Token Funciotn__: This function that is also called through the "handle_message" function, is used to check if the token that the Client has is valid. If the user hasn't signed in successfully, then they have **None** as a token, which is not valid. Also in case of an attacker making a fake one by changing small details in the token's format, the token that will be made will be completely different than the correct one, so the app is well secured and safe. <br>The token feature was inspired from additional studies done beyond my university's scope. The application implements the JWT library which I used in my authentication.py script, which is responsible for my application's security (more details about the script can be found later on). <br><br>
    - __Share Function__: It's used only in case the token passed from the Client is valid, and it's called from the **handle_message** function too. This function sends a response to the Client, notifying them that the Screen Sharing process is about to beging. After that message is sent, then the **subprocess** command is run and the **server_screen.py** script is run (more details about the server_screen.py script later on). <br><br>

    ### Client behaviour attributes:
    - __Connect_to_Server function__: It's used to connect to the server and it's the very first function called when on the gui_client.py script's terminal the number 2 is entered. I chose to make it like this so that as soon as the Graphical Interface is loaded to the Client's screen, the client side has already connected to the server. It is also better in terms of not breaking the application, in case a server is not found for the client to connect to (because try...except blocks are used in this function). <br>
    In addition, in this function is where the ClientThread class is used to start a thread between the client and the server. <br><br>
    - __Process_Received_Data function__: This function is used in combination with the thread, and it's basically the response handler of the client's side. This function also uses the handle_message function from the "state_machine" script, which returnes the name of the function that needs to be used to handle the server's response correctly. Also, in the very last stage when the server is starting the Share Screen Process, a specific value is sent which when the client receives it, the Client also starts the Share Screen process from their side (the subprocess command is used in this case as well, in order to start the Share Screen Process). <br><br>
    - __Handle_Login_Response function__: This function is used to handle the server's login respone. The reason a function was made for such specific scenario is so that depending on the server's response, the correct information will be logged into a file and also get printed as a message box on the Client's Screen. <br><br>
    - __Handle_Verification_Response function__: This function is essential, since it triggers the Share Screen Process. It's implementation logic is the same as the handle_login_response, with the only difference that once the token is valid and a True response is returned, the function "send_share_msg" is called (more information about the send_share_msg function can be found later on). <br><br>
    - __Try_to_Login function__: This function is used directly from the Graphical Interface on the gui_client.py script. This function is the one responsible for taking the login credentials that the user has entered, and sending them to the Server for further validation. <br><br>
    - __Check_Action function__: This function is used just like the function mentioned above. The gui_client.py script imports and uses this function to send the User's token (None in case the user doesn't have a token) to the Server for futher validation. Then from that point, if the token is valid, the handle_verification_response function is used to trigger the Share Screen Process. <br><br>
    - __Send_Share_msg function__: This function as mentioned aboved, is only callable through the handle_verification_response function. This function is responsible for notifying the Server that the Client has received the "Valid Token" function, the user is notified of that (through a message box that popped up), and the Server needs to start its side ofr the Share Screen Process- meaning that the subprocess command needs to be run. <br><br>
    - __Close_Connection function__: This funtion is used fromt the close buttons used in the Graphical Interface, so that the socket connection and the application is closed and handled gracefully without breaking the app or the Server-Side <br><br>
    - __Make_Box function__: This funtion is used to save a few lines of code when it comes to make a pop-up message box on the User Interface. It takes a message as a parameter, and then by using elements from the PyQt5 library, a message box is made and showed with that message. <br><br>


### vignere_cipher.py
-----------------------------------------------------------------------------------------------------
This script implements the vignere cipher algorithm, which my application uses when sending data from the Client side to the Server and back. At first, I settled in with the JWT library and the hashing method but I realised that there was a small "window" for breachers, and that was transimitting sensitive data through both sides. Thus, whenever sensitive information is sent, such as a token or login credentials, the data is encrypted and then decrypted with a secret key. Keep in mind, the secret key along with other essentail security-related information, are saved in a .env file. 

### auth.py
This script is the "core" of my application's security. It includes the JWT token along with its functions. 
- First of all, the Secret Key, Algorithm, and everything else related to the making of the token, are saved in a **.env file** and are accessed only by using the dotenv library, making it extra secure since no file names are used.<br>
- Secondly, the **create_access_token** function which is only used when the given credentials are correct, is responsible for the making of the token. This happens, by combining the given data in a dictionary, a secret key, and an algorithm (Keep in mind, the token in general is made out of thrree parts, for more information on JWT, go to the [JWT Documentation](https://jwt.io/introduction)) <br>
- In addition, the **verify_access_token** function is used to check whether the Client's token is valid or not. Again, this function implements methods from the JWT library.
- The **hash_password** function is used to hash any value given to it. The .gensalt() command generates a random salt, meaning a random value used as additional input to the value given, that needs to be hashed. After that, the .hashpw() method is used to hash the given value.
- The **check_password** function is used by the Server when receiving credentials from the Client, and what it does is that it implements the .checkpw() method from the bcrypt library. What this method does is that it hashes the given value the same way as the pre-hashed and saved values, and then it checks if the hashed values are the same. Then, based on the result True or False is returned. For more information on the bcrypt library, go to the [bcrypt Documentation](https://www.npmjs.com/package/bcrypt).<br>
- The auth.py script also includes the authentication class's instance, along with the dictionary of the pre-made users of the application. Of course this is a very wrong practise in real-world scenarios, but for educational purposes I decided that it'd suit better to have such list in the auth.py script.