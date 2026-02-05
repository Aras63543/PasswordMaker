import tkinter as tk
import random
import string

root = tk.Tk()
root.geometry("500x500")
root.title("Password Maker")

label = tk.Label(root, text="Password Maker")
label.pack()

# Create a label to display the generated password
password_label = tk.Label(root, text="")
password_label.pack()

def generate_password():
    length = 15  # Corrected spelling
    characters = string.punctuation + string.hexdigits

    password = ""
    for i in range(length):
        random_character = random.choice(characters)
        password += random_character

    # Update the password label with the generated password
    password_label.config(text=password)

button = tk.Button(root, text="Generate a password...", command=generate_password)
button.pack()

root.mainloop()
