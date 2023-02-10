import random
import tkinter as tk

def generate_number():
    number = "059"
    for i in range(7):
        number += str(random.randint(0, 9))
    label["text"] = number

root = tk.Tk()
root.title("Random Number Generator")

label = tk.Label(root, text="Click the button to generate a random number", font=("Helvetica", 16))
label.pack(pady=20)

button = tk.Button(root, text="Generate Number", font=("Helvetica", 16), command=generate_number)
button.pack(pady=20)

root.mainloop()
