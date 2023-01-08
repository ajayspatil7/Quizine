from tkinter import ttk
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
        self.text.config(bg="lightgrey", fg="black", highlightbackground="lightgrey")

        self.save_button = tk.Button(self, text="Save", command=self.save)
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_exam)

    def submit_exam(self):
        tk.messagebox.showerror("If you submit you can't do any changes. The exam window will close immediately")
        confirmation = tkinter.simpledialog.askstring("Submission Confirmation", "Are you Sure want to Submit? (Y/N)")

    def clear(self):
        self.text.delete("1.0", "end")

    def save(self):
        text = self.text.get("1.0", "end-1c")  # Get the text from the text widget
        # desktop = os.path.join(os.path.expanduser("~"), "Desktop")  # Get the desktop path
        file_path = "/Users/ajay/PycharmProjects/Quizine/submissions/file.c"
        # Write the text to the file
        with open(file_path, "w") as f:
            f.write(text)
