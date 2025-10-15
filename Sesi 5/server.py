import socket
import threading

# list untuk menyimpan semua koneksi client
clients = []

# fungsi untuk mengirim pesan ke semua client
def broadcast(pesan, koneksi):
    for c in clients:
        if c != koneksi:
            try:
                c.send(pesan)
            except:
                c.close()
                if c in clients:
                    clients.remove(c)

# fungsi untuk menangani setiap client
def handle_client(koneksi, alamat):
    print(f"[TERHUBUNG] {alamat} bergabung ke server.")
    while True:
        try:
            pesan = koneksi.recv(1024)
            if not pesan:
                break
            print(f"[PESAN DARI {alamat}] {pesan.decode('utf-8')}")
            broadcast(pesan, koneksi)
        except:
            break

    # jika koneksi terputus
    print(f"[PUTUS] {alamat} keluar dari server.")
    clients.remove(koneksi)
    koneksi.close()

# fungsi utama server
def mulai_server():
    host = '127.0.0.1'  # localhost
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"[MENUNGGU] Server berjalan di {host}:{port}")

    while True:
        koneksi, alamat = server.accept()
        clients.append(koneksi)
        thread = threading.Thread(target=handle_client, args=(koneksi, alamat))
        thread.start()

mulai_server()