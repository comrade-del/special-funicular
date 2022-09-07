import tkinter
from tkinter import messagebox
import sqlite3
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 2004
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "DISCONNECT"

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(ADDR)
print(f"[Connected] at {IP}:{PORT}")

conn = sqlite3.connect("politics.db")
if conn:
    print("Connected Successfully")
else:
    print("Connection Not Established")
cur = conn.cursor()

app = tkinter.Tk()
app.geometry("300x200")
app.title("States.py")


def button_function():
    mgg = entry_1.get()
    msg = "search"
    while True:
        if mgg == '':
            messagebox.showwarning(title="Error", message="Type in a state.")
            break
        c.send(msg.encode(FORMAT))
        c.send(str(mgg).encode(FORMAT))
        out = c.recv(SIZE).decode(FORMAT)
        messagebox.showinfo('State Info', f'{mgg} is in the {out}')
        break


y_padding = 6

frame_1 = tkinter.Frame(master=app, width=500, height=300, bg="blue")
frame_1.pack(padx=60, pady=20, fill="both", expand=True)

label_1 = tkinter.Label(master=frame_1, text="State zone finder", bg="lightgray")
label_1.pack(pady=y_padding, padx=10)

entry_1 = tkinter.Entry(master=frame_1, highlightbackground="green", width=100)
entry_1.pack(pady=y_padding, padx=10)

button_1 = tkinter.Button(master=frame_1, command=button_function, text="Get zone", highlightbackground="red")
button_1.pack(pady=y_padding, padx=10)


app.mainloop()
