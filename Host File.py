import socket
import random

hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)


print(f"Waiting for a player to connect on {HOST}:{PORT}...")

conn, addr = server.accept()
print(f"Connected by {addr}")

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
