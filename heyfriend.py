import tkinter as tk

def close_window(event):
    root.destroy()

def show_alert():
    alert_label.config(text="Hey friend!")

# Create the main window
root = tk.Tk()
root.title("Random Python")

# Create a label for the alert
alert_label = tk.Label(root, text="Hey friend!", font=("Helvetica", 16))
alert_label.pack(pady=20)

# Bind a key event to close the window
root.bind("<Key>", close_window)

# Set up a loop to continually show the alert
while True:
    root.update()
    show_alert()
