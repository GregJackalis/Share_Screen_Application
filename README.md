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
This is the "main" script of my project, meaning that it needs to be run first. This script "connects"" the GUI that I've already made, with the Peer script that contains both Client and Server behaviours. What it does is that it gives functionality to the button on the Interface, then based on the button that is pressed (and if the user has chosen to be the user of course by entering 2 on the terminal) the interface imports and uses Client behaviour attributes to send data to the server but also wait and handle a response.<br>
However, if the user enters 1 on the terminal when running this script, the user will enter Share Screen mode, a.k.a. the user will be the Server and that's where the Server behaviour attributes will come in and await for a Client to Connect.

### peer.py
This is the second most important script of my project, and it's the one responsible for a secure and reliable conenction between Client and Server by using Socket Programming principles. The script includes two classes:
1) The first called "ClientThread" is used to create a thread between the Client and the Server so that the Client will always await a response from the Server (while also checking if there is still a connection and an ucoming message of course).

2) The second class with the name "Peer" is where all of this application's socket programming is included. <br>
    ### Starting from the Server behaviour attributes, there are:<br><br>
    - <u>Listen function</u>: it's used to listen for Clients that are trying to connect to the Server's address and port, and also handle messages using a function made in the state_machine.py script. Then, once handle_message function has returned the correct response, it is time for the right function to be called too. <br><br>
    - <u>Login function</u>: it's used to receive the credentials the Client sends to login. In this function, by using an if-statement and functions that are imported from the auth.py scripts, the credentials are thoroughly decrypted using the vignere cipher, then encrypted again to match the already hashed passwords that are saved in a .env file...and then finally a response is sent to the Client. <br><br>
    - <u>Check_Token Funciotn</u>: This function that is also called through the "handle_message" function, is used to check if the token that the Client has is valid. If the user hasn't signed in successfully, then they have **None** as a token, which is not valid. Also in case of an attacker making a fake one by changing small details in the token's format, the token that will be made will be completely different than the correct one, so the app is well secured and safe. <br>The token feature was inspired from additional studies done beyond my university's scope. The application implements the JWT library which I used in my authentication.py script, which is responsible for my application's security (more details about the script can be found later on). <br><br>
    - <u>Share Function</u>: It's used only in case the token passed from the Client is valid, and it's called from the **handle_message** function too. This function sends a response to the Client, notifying them that the Screen Sharing process is about to beging. After that message is sent, then the **subprocess** command is run and the **server_screen.py** script is run (more details about the server_screen.py script later on). <br><br>
