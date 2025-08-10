import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import requests
import json

SERVER_URL = "http://localhost:5000/check-email/"


def check_email():
    email = entry.get()
    if not email:
        messagebox.showwarning("Input Error", "Please enter an email address.")
        return
    try:
        response = requests.get(SERVER_URL + email)
        response.raise_for_status()
        result = response.json()

        is_valid = "valid" if result.get("format") else "invalid"
        is_disposable = "a disposable" if result.get("disposable") else "not a disposable"
        has_dns = "has valid DNS records" if result.get("dns") else "does not have valid DNS records"
        domain = result.get("domain", "unknown domain")

        friendly_msg = (
            f"Results for: {email}\n"
            f"- Email format is {is_valid}.\n"
            f"- The domain is: {domain}\n"
            f"- The email is {is_disposable} address.\n"
            f"- The domain {has_dns}."
        )

        output.delete(1.0, tk.END)
        output.insert(tk.END, friendly_msg)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to check email:\n{e}")

root = tk.Tk()
root.title("Email Checker")

root.resizable(False, False)

load = Image.open("logo.png")
render = ImageTk.PhotoImage(load)
root.iconphoto(False, render)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Enter email address:")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5)

btn = tk.Button(frame, text="Check Email", command=check_email)
btn.grid(row=0, column=2, padx=5)

output = tk.Text(frame, width=50, height=10)
output.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()