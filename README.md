Here's an example of how you could create a graphical user interface (GUI) for the previous code using the tkinter library in Python:

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



This code creates a window with a button labeled "Generate Number". When the button is clicked, the generate_number function is called and a random number is generated and displayed in the label on the window. The tkinter library is used to create the GUI elements and manage the event loop.
