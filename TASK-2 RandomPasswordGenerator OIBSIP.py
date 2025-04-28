import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Error", "Password length must be a number.")
        return

    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    exclude_similar = exclude_var.get()

    if not (use_letters or use_numbers or use_symbols):
        messagebox.showerror("Error", "Select at least one character type.")
        return

    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if exclude_similar:
        for c in "O0l1I":
            characters = characters.replace(c, '')

    if not characters:
        messagebox.showerror("Error", "No characters left to generate password.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x320")

length_var = tk.StringVar(value="12")
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
exclude_var = tk.BooleanVar(value=False)

tk.Label(root, text="Password Length:", font=('Arial', 10)).pack(pady=5)
tk.Entry(root, textvariable=length_var, width=5, font=('Arial', 12)).pack()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Exclude Similar Characters (O, 0, l, 1, I)", variable=exclude_var).pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password, bg="lightblue").pack(pady=10)

password_entry = tk.Entry(root, width=40, font=('Arial', 12))
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="lightgreen").pack(pady=5)

root.mainloop()
