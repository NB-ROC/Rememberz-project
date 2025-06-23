# client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.175.227", 8080))  # <-- IP van de server-laptop

# Verzend jouw specifieke YouTube-link
youtube_link = "https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran"
client.sendall(youtube_link.encode())

print("YouTube-link verzonden!")
client.close()
