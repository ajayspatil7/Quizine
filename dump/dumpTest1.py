import tkinter as tk


def show_username_and_password():
    """
    :return:
    wertyfghj56
    """
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}")
    print(f"Password: {password}")

root = tk.Tk()
root.geometry("450x500")
root.title("Login")

# Align the username and password labels and entries in the center

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack(side="top")
username_label.pack(anchor="center")

password_label = tk.Label(root, text="Password:")
password_label.pack(side="top")
password_label.anchor("center")

password_entry = tk.Entry(root, show="*")
password_entry.pack(side="top")
password_label.anchor("center")

show_button = tk.Button(root, text="Show", command=show_username_and_password)
show_button.pack(side="top")

root.wm_resizable(False, False)
root.mainloop()

