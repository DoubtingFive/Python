import socket
from threading import *
from colorama import *
import time

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
print(f"{Fore.YELLOW}[IP]: {ip}")

username = input(f"{Fore.YELLOW} - [Username]: ")

def TryToConnect():
    global sock
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"{Fore.YELLOW}Trying to connect...")
        sock.connect((ip,4444))
        sock.send(username.encode())
        recv = sock.recv(8196)
        print(recv.decode())
    except Exception as e:
        print(f"{Fore.RED}[Error TryToConnect()] {Fore.LIGHTRED_EX}{e}")
        time.sleep(2)
        TryToConnect()
    Thread(target=Recive).start()
    Send()

def Recive():
    global sock
    while True:
        try:
            recv = sock.recv(512)
            print(recv.decode())
        except Exception as e:
            print(f"{Fore.RED}[Error Recive()] {Fore.LIGHTRED_EX}{e}")
            TryToConnect()

def Send():
    global sock
    while True:
        try:
            msg = input()
            sock.send(f"{username} > {msg}".encode())
            if msg == "exit":
                sock.close()
                exit()
        except Exception as e:
            print(f"{Fore.RED}[Error Send()] {Fore.LIGHTRED_EX}{e}")
            TryToConnect()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TryToConnect()
