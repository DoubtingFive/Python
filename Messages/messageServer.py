import socket
import threading as th
import colorama

def AcceptConnection():
    while True:
        connection, address = sock.accept()
        th.Thread(target=Connect,args=[connection,address]).start()

def Connect(c, a):
    print(f"Get connection from {a[0]}.") # check port command
    c.send(chat.encode())
    for x in conn_list:
        x.send(f"{colorama.Fore.LIGHTYELLOW_EX} >>> New connection from: {a}".encode())
    conn_list.append(c)
    conn_name.append(a)
    th.Thread(target=HandleConnection, args=[c,a]).start()

def HandleConnection(c,a):
    while True:
        try:
            recv = c.recv(1024)
        except Exception as e:
            print(f" Error from {a[0]}: {e}")
            conn_list.remove(c)
            conn_name.remove(a)
        if recv == "exit":
            print("exit: "+a)
            conn_list.remove(c)
            conn_name.remove(a)
        print(recv.decode())
        chat += recv.decode()+"n\\"
        for x in conn_list:
            x.send(recv)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_list = []
conn_name = []
chat = ""

sock.bind(("0.0.0.0",4444))
sock.listen(5)

print("Waiting for connections...")
AcceptConnection()
