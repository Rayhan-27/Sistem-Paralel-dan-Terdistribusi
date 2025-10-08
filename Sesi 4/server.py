import socket

# Membuat socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menentukan alamat IP dan port
server_ip = '127.0.0.1'   # alamat lokal
server_port = 12345

# Bind alamat IP dan port ke socket
server_socket.bind((server_ip, server_port))

# Server mendengarkan koneksi masuk
server_socket.listen(1)
print(f"Server berjalan di {server_ip}:{server_port}, menunggu koneksi...")

# Menerima koneksi dari client
conn, addr = server_socket.accept()
print(f"Terhubung dengan client dari alamat: {addr}")

# Menerima pesan dari client
pesan = conn.recv(1024).decode()
print(f"Pesan dari client: {pesan}")

# Mengirim balasan ke client
balasan = "Pesan diterima oleh server."
conn.send(balasan.encode())

# Tutup koneksi
conn.close()
server_socket.close()
print("Server berhenti.")
