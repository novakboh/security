import socket
import jsonpickle
from dataclasses import dataclass
from hashlib import sha256

@dataclass
class Authorisation:
    login: str
    password: str

IP = "127.0.0.1"
PORT = 4000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.send(input("What do you want to do? (r/a): ").encode())
login = input("Enter login: ")
password = input("Enter password: ")
hashpassword = sha256(password.encode()).hexdigest()
authorisation = Authorisation(login, hashpassword)
json_output = jsonpickle.encode(authorisation, indent=4)
client.send(json_output.encode())
print(client.recv(1024).decode())
client.close()