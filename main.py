from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import hashlib
import os

#  Password is 0

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.text = tk.Text(self)
        self.text.pack(side="top", fill="both", expand=True)

        self.save_button = tk.Button(self, text="Save", command=self.save)
        self.save_button.pack(side="bottom")

    def save(self):

        text = self.text.get("1.0", "end-1c")  # Get the text from the text widget
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")  # Get the desktop path
        file_path = os.path.join(desktop, "text.txt")  # Create the file path
        # Write the text to the file
        with open(file_path, "w") as f:
            f.write(text)
           

class ExamApp(tk.Tk):

    def save(self):
        # Get the text from the text widget
        text = self.text.get("1.0", "end-1c")

        # Get the desktop path
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")

        # Create the file path
        file_path = os.path.join(desktop, "text.txt")

        # Write the text to the file
        with open(file_path, "w") as f:
            f.write(text)

    def __init__(self):
        super().__init__()

        self.attributes("-fullscreen", True)
        self.bind("<Escape>", self.end_exam)
        self.bind("<F11>", self.toggle_fullscreen)
        self.text = tk.Text(self)
        self.text.pack(side="top", fill="both", expand=True)
        self.save_button = tk.Button(self, text="Save", command=self.save)
        self.save_button.pack(side="bottom")
        self.save_button.config(font=("Arial", 14, "bold"))
        self.save_button.config(height=2, width=10)
        self.save_button.place(x=1300, y=35)
        self.config(bg="blue")


        # Store the password in a secure way, such as a hash
        import hashlib
        self.password_hash = hashlib.sha256("0".encode()).hexdigest()

        # Create the exam UI here...
        """UI and othre functionalities go here"""

    def toggle_fullscreen(self, event=None):
        self.attributes("-fullscreen", not self.attributes("-fullscreen"))

    def end_exam(self, event=None):

        screen_width = self.winfo_screenwidth()
        screen_height = screen_width = self.winfo_screenheight()
        x = screen_width // 2
        y = screen_height // 2

        input_password = tkinter.simpledialog.askstring("End Exam", "Enter password to end exam:", show="*")

        # Check if the password is correct
        if hashlib.sha256(input_password.encode()).hexdigest() == self.password_hash:
            # End the exam and close the application
            self.destroy()
        else:
            tk.messagebox.showerror("Error", "Incorrect password")

app = ExamApp()
app.mainloop()
