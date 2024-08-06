# WorkoutQuote.py
The repository for my partner's microservice I am creating
A microservice for a collegue's workout generator program. This service uses ZMQ to send a user input and returns an image of a motivational quote to the user.

Instructions for REQUEST:

  1. Import ZMQ

  2. Set up a correct socket and port:
     context = zmq.Context()
     socket = context.socket(zmq.REQ)
     socket.connect("tcp://127.0.0.1:5500")

  3. Send request via user input Yes or No to the server
     Yes will generate a random number assigned to an image found in the folder
     No will send a specified massage
     

Instructions for RECEIVE:
  1. Receive through same set up as request, with socket.recv_string()
     Service will return a path to img found in the folder


Example Call:
Would you like to feel motivated? Enter Yes or No
User: Yes
Receive:MotivationalQuotePics/1.jpg

Would you like to feel motivated? Enter Yes or No
User: No
Have a great day!


UML Sequence Diagram:

<img width="481" alt="Screen Shot 2024-08-05 at 7 21 59 PM" src="https://github.com/user-attachments/assets/ee7ddc29-bfca-435c-973d-7536d52ee0b1">




