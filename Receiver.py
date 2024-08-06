import zmq
import random


class Reply:
    def __init__(self, socket):
        self.socket = socket

    def get_quote_num(self):
        number = random.randrange(7)
        number += 1
        return number

    def send_path(self):
        while True:
            answer = self.socket.recv_string()
            if answer == "Yes":
                pic = self.get_quote_num()
                final = f"MotivationalQuotePics/{pic}.jpg"
                self.socket.send_string(final)
            if answer == "No":
                no_message = "Have a great day!"
                socket.send_string(no_message)
                break

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5500")
reply = Reply(socket)
reply.send_path()