import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import hashlib
import os

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.text = tk.Text(self)
        self.text.pack(side="top", fill="both", expand=True)

        self.save_button = tk.Button(self, text="Save", command=self.save)
        self.save_button.pack(side="bottom")

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
           


class ExamApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", self.end_exam)
        self.bind("<F11>", self.toggle_fullscreen)

        # Store the password in a secure way, such as a hash
        import hashlib
        self.password_hash = hashlib.sha256("mypassword".encode()).hexdigest()

        # Create the exam UI here...
        tEditor = TextEditor()
        tEditor.mainloop()

    def toggle_fullscreen(self, event=None):
        self.attributes("-fullscreen", not self.attributes("-fullscreen"))

    def end_exam(self, event=None):
        # Prompt the user to enter their password
        input_password = tkinter.simpledialog.askstring("End Exam", "Enter password to end exam:", show="*")

        # Check if the password is correct
        if hashlib.sha256(input_password.encode()).hexdigest() == self.password_hash:
            # End the exam and close the application
            self.destroy()
        else:
            tk.messagebox.showerror("Error", "Incorrect password")

app = ExamApp()
app.mainloop()
