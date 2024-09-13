import subprocess
import os
import sys
password_file = open('passwords.txt', "w")
password_file.close()

wifi_files = []

command = subprocess.run("netsh wlan export profile key=\"clear\"", capture_output=True).stdout
print(command)
path = os.getcwd()

for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename) 
for i in wifi_files:
    wifi_name = ""
    wifi_pass = ""
    with open(i, "r") as f:
        for line in f.readlines():
            if 'name'in line:
                stripped = line.strip()
                front = stripped[6:]
                back = front [:-7]
                wifi_name = back
            if 'keyMaterial' in line:
                stripped = line.strip()
                front = stripped[13:]
                back = front [:-14]
                wifi_pass = back
    with open("passwords.txt", "a") as file:
        print(f"ssid: {wifi_name} - Pass: {wifi_pass}\n")
        file.write(f"ssid: {wifi_name} - Pass: {wifi_pass}\n")
