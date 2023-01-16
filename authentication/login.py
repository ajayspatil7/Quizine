import tkinter as tk


class LoginInterface():
    # Create the main window
    root = tk.Tk()
    root.title("Login")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.wm_resizable(False, False)

    # Screen width and height
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)

    # Create the username label and textbox
    user_label = tk.Label(root, text="Username:")
    user_label.grid(row=0, column=0, padx=5, pady=2, sticky='e')
    user_entry = tk.Entry(root)
    user_entry.grid(row=0, column=1, padx=5, pady=2, sticky='w')

    # Create the password label and textbox
    pass_label = tk.Label(root, text="Password:")
    pass_label.grid(row=1, column=0, padx=5, pady=2, sticky='e')
    pass_entry = tk.Entry(root, show="*")
    pass_entry.grid(row=1, column=1, padx=5, pady=2, sticky='w')

    # Create the login button
    login_button = tk.Button(root, text="Login", bg="white", fg="black")
    login_button.grid(row=2, column=1, columnspan=5, padx=2, pady=2)

    # Run the main loop
    root.mainloop()





