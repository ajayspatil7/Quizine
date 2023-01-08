import tkinter as tk


class LoginWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Login")
        self.geometry("200x100")

        self.user_id_label = tk.Label(self, text="User ID:")
        self.user_id_label.pack(side="left")

        self.user_id_entry = tk.Entry(self)
        self.user_id_entry.pack(side="left")

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(side="left")

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(side="left")

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(side="left")

    def login(self):
        user_id = self.user_id_entry.get()
        password = self.password_entry.get()

        # Check if the user's credentials are correct
        if user_id == "abc" and password == "123":
            # Close the login window
            self.destroy()

            # Open the exam interface
            ExamWindow(self.master)


class ExamWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
