import tkinter as tk

def button1_click():
    print("yipee")

def button2_click():
    print("f u")

# Create the main window
window = tk.Tk()
window.title("Questionare Window")
text1 = tk.Label(window, text="Will you marry me?")
text1.pack(pady=10)

# Create buttons
button1 = tk.Button(window, text="Yes", command=button1_click)
button1.pack(pady=10)

button2 = tk.Button(window, text="No", command=button2_click)
button2.pack(pady=10)

# Start the main event loop
window.mainloop()