import socket
import random
import requests

SERVER_URL = "https://breakey.onrender.com"  

host_ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]

# Register as available
requests.post(f"{SERVER_URL}/register", json={"ip": host_ip})
print("Waiting for a match...")

PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host_ip, PORT))
server.listen(1)

conn, addr = server.accept()
print(f"Connected to {addr}")

my_key_strength = random.random()
conn.send(str(my_key_strength).encode())

enemy_strength = float(conn.recv(1024).decode())
print(f"Enemy key strength: {enemy_strength}")

if my_key_strength > enemy_strength:
    print("You win!")
    my_key_strength -= random.uniform(0, 0.1) 
else:
    print("You lose!")

conn.close()
server.close()
