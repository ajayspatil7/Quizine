import tkinter as tk


class LoginInterface():
    # Create the main window
    root = tk.Tk()
    root.title("Login")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.wm_resizable(False, False)

    # Create the username label and textbox
    user_label = tk.Label(root, text="Username:")
    user_label.grid(row=0, column=0, padx=10, pady=10)
    user_entry = tk.Entry(root)
    user_entry.grid(row=0, column=1, padx=10, pady=10)

    # Create the password label and textbox
    pass_label = tk.Label(root, text="Password:")
    pass_label.grid(row=1, column=0, padx=5, pady=5)
    pass_entry = tk.Entry(root, show="*")
    pass_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create the login button
    # Modify the login button to call the login function

    login_button = tk.Button(root, text="Login", bg="white", fg="black", command=login)
    login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Run the main loop
    root.mainloop()



