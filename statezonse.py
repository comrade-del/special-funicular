import tkinter
import customtkinter
from tkinter import messagebox
import sqlite3
import socket

IP = socket.gethostbyname(socket.gethostname())  # replace with my IP
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

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x200")
app.title("State Zones")


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


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="State zone finder", justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="State")
entry_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Get zone", command=button_function)
button_1.pack(pady=12, padx=10)


app.mainloop()
