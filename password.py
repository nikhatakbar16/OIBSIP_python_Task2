from tkinter import *
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        password_var.set(password)
    except ValueError:
        password_var.set("Enter a valid number!")


window = Tk()
window.title("Random Password Generator")
window.geometry("420x240")
window.config(background="black")


icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)


password_var = StringVar()

Label(window, text="Password Length:", bg="black", fg="white", font=("Arial", 12)).pack(pady=10)
length_entry = Entry(window, font=("Arial", 12), justify='center')
length_entry.pack()

Button(window, text="Generate Password", command=generate_password, font=("Arial", 12), bg="gray", fg="white").pack(pady=15)

Entry(window, textvariable=password_var, font=("Arial", 12), width=30, justify='center').pack(pady=10)


window.mainloop()
