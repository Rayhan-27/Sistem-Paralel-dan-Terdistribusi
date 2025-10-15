import socket
import threading

def terima_pesan():
    while True:
        try:
            pesan = client.recv(1024).decode('utf-8')
            print(pesan)
        except:
            print("[KESALAHAN] Koneksi ke server terputus.")
            client.close()
            break

def kirim_pesan():
    while True:
        pesan = input("")
        try:
            client.send(pesan.encode('utf-8'))
        except:
            print("[KESALAHAN] Gagal mengirim pesan.")
            client.close()
            break

# koneksi ke server
server_ip = '127.0.0.1'
server_port = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((server_ip, server_port))
    print("[TERHUBUNG] Anda berhasil terhubung ke server.")
except:
    print("[GAGAL] Tidak bisa terhubung ke server.")
    exit()

# jalankan dua thread: untuk menerima & mengirim pesan
thread_terima = threading.Thread(target=terima_pesan)
thread_kirim = threading.Thread(target=kirim_pesan)

thread_terima.start()
thread_kirim.start()