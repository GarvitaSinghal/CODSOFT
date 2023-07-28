import tkinter as tk
def on_click(button_value):
    current = display_var.get()
    if button_value == "=":
        try:
            result = eval(current)
            display_var.set(result)
        except:
            display_var.set("Error")
    elif button_value == "C":
        display_var.set("")
    else:
        display_var.set(current + button_value)

# Create the main application window and naming it as calculator
root = tk.Tk()
root.title("Calculator")

# StringVar to store the display value
display_var = tk.StringVar()

# Entry widget to display the result
display_entry = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=20, insertwidth=40, width=15, justify="right")
display_entry.grid(row=0, column=0, columnspan=4)

# Buttons for each digit and operation
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

# Function to create and bind buttons
row, col = 1, 0
for button in buttons:
    tk.Button(root, text=button, font=("Babapro font", 15), padx=20, pady=10, command=lambda val=button: on_click(val)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the Tkinter event loop
root.mainloop()
