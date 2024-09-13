# not fully working ;((
import socket
from threading import *
from colorama import *

init(autoreset=True)

ip = ""
ipFromFile = ""
try:
    f = open("addr","r")
    ipFromFile = f.read(16)
    f.close()
except FileNotFoundError:
    f = open("addr","w")
    ipFromFile = input(f"{Fore.YELLOW} - [IP Address]: ")
    f.write(ipFromFile)
    f.close()

ip = ipFromFile
print(f"[IP]: {ip}")

username = input(f"{Fore.YELLOW} - [Username]: ")

def TryToConnect():
    try:
        print(f"{Fore.LIGHTMAGENTA_EX}Trying to connect...")
        sock.connect((ip,4444))
        # sock.send(username.encode())
    except Exception as e:
        print(f"{Fore.RED}[Error] {e}")
        TryToConnect()
    Thread(target=Recive).start()
    Thread(target=Send).start()

def Recive():
    while True:
        recv = sock.recv(1024).decode()
        # recvaddr = recv[recv.find('(')+2:recv.find(',')-1]
        # recvport =  recv[recv.find(',')+2:recv.find(')')]
        print(recv)

def Send():
    while True:
        msg = input()
        if msg == "exit":
            sock.close()
            exit()
        sock.send(f"{username} > {msg}".encode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TryToConnect()
