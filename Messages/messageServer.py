import socket
import threading as th
import colorama

colorama.init(autoreset=True)

def AcceptConnection():
    while True:
        connection, address = sock.accept()
        th.Thread(target=Connect,args=[connection,address]).start()

def Connect(c, a):
    u = c.recv(16).decode()
    newConnectionMessage = f"{colorama.Fore.LIGHTYELLOW_EX} >>> Get connection from {a[0]} as {u}."
    print(newConnectionMessage)
    newConnectionMessage = newConnectionMessage.encode()
    c.send(chat.encode())
    for x in conn_list:
        x.send(newConnectionMessage)
    conn_list.append(c)
    th.Thread(target=HandleConnection, args=[c,a,u]).start()

def HandleConnection(c,a,u):
    global chat
    while True:
        try:
            recv = c.recv(512)
            recvDecode = recv.decode()
            chat += recvDecode+"\n"
            print(recvDecode)
            for x in conn_list:
                if x == c: continue
                x.send(recv)
        except Exception as e:
            if c in conn_list:
                conn_list.remove(c)
            print(f"{colorama.Fore.LIGHTRED_EX} Error from {a[0]}: {e}{colorama.Fore.RESET}")
            lostConnectionMessage = f"{colorama.Fore.RED} <<< Lost connection from {a} as {u}.{colorama.Fore.RESET}".encode()
            for x in conn_list:
                x.send(lostConnectionMessage)
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_list = []
chat = "chat:\n"

sock.bind(("0.0.0.0",4444))
sock.listen(5)

print("Waiting for connections...")
AcceptConnection()
