import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(name, length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = []
    for i in range(length):
        randomchar = random.choice(characters)
        password.append(randomchar)
    password="".join(password)
    return password

def generate_password_button():
    name = name_entry.get().strip()
    length = int(length_entry.get())
    
    if not name:
        messagebox.showerror("Error", "Please enter your name.")
        return
    
    if length < 5:
        messagebox.showerror("Error", "Password length should be at least 5 characters.")
        return

    password = generate_password(name, length)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def accept_password_button():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Warning","No password to accept.")

def refresh_password_button():
    generate_password_button()

# Create the main window
root = tk.Tk()
root.minsize(500,500)
root.title("Password Generator")

head_label=tk.Label(root, text="Password Generator", font=("arial",30), background="blue", foreground="white")
head_label.pack()
# Create labels and entries for name and password length
name_label = tk.Label(root, text="Enter your name:", font=("arial",20))
name_label.pack()
name_entry = tk.Entry(root, width=25, font=("helvetica",13,"bold"),foreground="green")
name_entry.pack(pady=9)

length_label = tk.Label(root, text="Enter password length:", font=("arial",20))
length_label.pack()
length_entry = tk.Entry(root, width=25, font=("helvetica",13,"bold"),foreground="green")
length_entry.pack(pady=7)

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create an entry to display the generated password
pswd_label= tk.Label(root, text="Generated Password:", font=("arial",15,))
pswd_label.pack()
password_entry = tk.Entry(root, width=25, font=("helvetica",13,"bold"),foreground="red")
password_entry.pack(pady=7)

# Create the buttons
generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password_button, font=("arial",15), bg="cyan")
generate_button.pack(side=tk.LEFT, pady=7)

accept_button = tk.Button(button_frame, text="Accept", command=accept_password_button, font=("arial",15), bg="light green")
accept_button.pack(side=tk.LEFT, padx=10, pady=7)

refresh_button = tk.Button(button_frame, text="Refresh", command=refresh_password_button, font=("arial",15),bg="yellow")
refresh_button.pack(side=tk.LEFT, pady=7)

root.mainloop()
