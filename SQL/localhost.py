import mysql.connector
from time import time

def cmd():
    user_input = input(" >")
    confirm = input("Confirm? (y/n) ")
    if confirm == "n":
        return False
    if user_input == "exit":
        return True
    s = time()
    c.execute(user_input)
    print(f">> {c.fetchone()} | Done in {round(time() - s,5)}s")
    return False

run = True

while run:
    start = time()
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root", # if7-%lZ*V
            password="", #82md90ao32n
            database="test"
        )

        if connection.is_connected():
            print("Connected to MySQL database")
            
            c = connection.cursor()
            
            c.execute("SELECT VERSION()")
            db_version = c.fetchone()
            print("MySQL Server Version:", db_version[0])
            while True:
                if cmd():
                    break

    except mysql.connector.Error as err:
        print("> Error:", err)

    if connection.is_connected():
        c.close()
        connection.close()
        print(f"MySQL connection closed. The session lasted {round(time() - start,3)} seconds.")
    reconnect = input("Reconnect? (y/n)")
    if reconnect == "n":
        run = False
