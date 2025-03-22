import socket
import random
import requests
import time

SERVER_URL = "https://breakey.onrender.com"  

while True:
    response = requests.get(f"{SERVER_URL}/find_match").json()
    match_ip = response.get("match")
    if match_ip:
        print(f"Found opponent at {match_ip}")
        break
    print("Waiting for an opponent...")
    time.sleep(2)

PORT = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((match_ip, PORT))

enemy_strength = float(client.recv(1024).decode())
print(f"Opponent's key strength: {enemy_strength}")

my_key_strength = random.random()
client.send(str(my_key_strength).encode())

if my_key_strength > enemy_strength:
    print("You win!")
    my_key_strength -= random.uniform(0, 0.1) 
else:
    print("You lose!")

client.close()
