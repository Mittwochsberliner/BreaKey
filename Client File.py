import socket
import random

HOST = input("Enter opponent's IP: ")
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

enemy_strength = int(client.recv(1024).decode())
print(f"Opponent's key strength: {enemy_strength}")

my_key_strength = random.random()
client.send(str(my_key_strength).encode())

if my_key_strength > enemy_strength:
    print("You win!")
    my_key_strength -= random.uniform(0, 0.1) 
else:
    print("You lose!")

client.close()
