import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def edit_task():
    try:
        selected_index = listbox.curselection()[0]
        current_task = listbox.get(selected_index)
        new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=current_task)
        if new_task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create widgets
entry = tk.Entry(app, width=50)
listbox = tk.Listbox(app, width=50, height=10)
add_button = tk.Button(app, text="Add Task", width=20, command=add_task)
edit_button = tk.Button(app, text="Edit Task", width=20, command=edit_task)
delete_button = tk.Button(app, text="Delete Task", width=20, command=delete_task)

# Grid layout
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
add_button.grid(row=2, column=0, padx=10, pady=10)
edit_button.grid(row=2, column=1, padx=10, pady=10)
delete_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
