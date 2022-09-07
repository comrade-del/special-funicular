import socket
import threading
import sqlite3

IP = socket.gethostbyname(socket.gethostname())
PORT = 2004
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "DISCONNECT"

conns = sqlite3.connect("politics.db", check_same_thread=False)
cur = conns.cursor()


def handle_client(conn, addr):
    print(f"[NEW] {addr}")
    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        which = conn.recv(SIZE).decode(FORMAT)
        if which == '':
            pass
        if which == 'FCT':
            which = 'Federal Capital Territory'
        msg1 = cur.execute('''SELECT Zones from states WHERE States=?''', (which,)).fetchone()[0]

        print(f"[{addr}] {msg}")
        print(type(msg1))
        mss = f"{msg1}"
        conn.send(mss.encode(FORMAT))
    conn.close()


def main():
    print("[Started] Yayy")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ADDR)
    s.listen()
    print(f"[Listening] {IP}:{PORT}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE]: {threading.active_count() - 1}")


if __name__ == "__main__":
    main()
