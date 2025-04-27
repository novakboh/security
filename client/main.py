import socket
import jsonpickle
from dataclasses import dataclass
from hashlib import sha256
from tkinter import *

def authorise():
    if sendData(): 
        client.send("a".encode())
        resultLabel.config(text=client.recv(1024).decode())
    else:
        resultLabel.config(text="Wrong input")

def register():
    if sendData(): 
        client.send("r".encode())
        resultLabel.config(text=client.recv(1024).decode())
    else:
        resultLabel.config(text="Wrong input")

def checkPassword():
    password = passwordEntry1.get()
    if password != "" and password == passwordEntry2.get():
        return password
    return False

def sendData():
    login = loginEntry.get()
    password = checkPassword()
    if login != "" and password:
        hashpassword = sha256(password.encode()).hexdigest()
        authorisation = Authorisation(login, hashpassword)
        json_output = jsonpickle.encode(authorisation, indent=4)
        client.send(json_output.encode())
        return True
    return False
    
@dataclass
class Authorisation:
    login: str
    password: str

IP = "127.0.0.1"
PORT = 4000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
root = Tk()
root.geometry("250x100")
root.title("Authorisation")
Label(text="Login:").grid(row=0, column=0)
Label(text="Password:").grid(row=1, column=0)
Label(text="Repeat password:").grid(row=2, column=0)
loginEntry = Entry()
loginEntry.grid(row=0, column=1)
passwordEntry1 = Entry()
passwordEntry1.grid(row=1, column=1)
passwordEntry2 = Entry()
passwordEntry2.grid(row=2, column=1)
Button(text="Authorise", command=authorise).grid(row=3, column=0)
Button(text="Register", command=register).grid(row=3, column=1)
resultLabel = Label().grid(row=4, column=0, columnspan=2)
root.mainloop()
client.close()