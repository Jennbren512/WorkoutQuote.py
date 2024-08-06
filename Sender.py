import time
import zmq

context = zmq.Context()

print("Connecting to server...")
time.sleep(1)
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5500")

def request_quote():
    while True:
        answer = input("Would you like to feel motivated? Enter Yes or No: ")
        if answer == "Yes":
            print(f'Sending request for workout quote')
            time.sleep(1)
            socket.send_string(answer)
            final = socket.recv_string()
            print(f"Receiving response: '{final}'")
        elif answer == "No":
            socket.send_string(answer)
            final = socket.recv_string()
            print(f"{final}")
            break
        else:
            print("Input not accepted. Try again.")

if __name__ == "__main__":
    request_quote()