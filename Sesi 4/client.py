import socket

# Membuat socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menentukan alamat server dan port
server_ip = '127.0.0.1'
server_port = 12345

# Terhubung ke server
client_socket.connect((server_ip, server_port))
print("Terhubung ke server.")

# Mengirim pesan ke server
pesan = input("Ketik pesan untuk server: ")
client_socket.send(pesan.encode())

# Menerima balasan dari server
balasan = client_socket.recv(1024).decode()
print(f"Balasan dari server: {balasan}")

# Tutup koneksi
client_socket.close()
