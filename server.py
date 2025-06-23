import socket

# Maak een socket aan
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind aan IP en poort
server.bind(("0.0.0.0", 8080))  # Luistert op alle netwerkinterfaces
server.listen(1)

print("🔌 Server gestart. Wachten op een verbinding...")

# Accepteer een verbinding
conn, addr = server.accept()
print(f"✅ Verbonden met {addr}")

# Ontvang de data (max 1024 bytes)
data = conn.recv(1024).decode()
print(f"📥 Ontvangen YouTube-link: {data}")

# Sluit de verbinding
conn.close()
server.close()
print("🔒 Verbinding gesloten.")
