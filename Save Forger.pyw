from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfilename
from hashlib import md5


class SaveForger(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("Save Forger")
        self.menu = Menu(self)
        self.fileMenu = Menu(self.menu, tearoff=0)
        self.fileMenu.add_command(label="Open", command=self.open)
        self.fileMenu.add_command(label="Save", command=self.save)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        self.config(menu=self.menu)
        self.textEditor = Text(self)
        self.textEditor.grid(row=0, column=0, columnspan=2)
        Label(self, text="Type \"I agree to being a sussy baka if i am using this for cheating\"").grid(row=1, column=0)
        self.passwordBox = Entry(self)
        self.passwordBox.grid(row=1, column=1)
        with open("NewGame.json", "r") as file:
            self.textEditor.insert("1.0", file.read())
        self.mainloop()

    def open(self):
        file = askopenfile(filetypes=[
            ("Save file", ".json")
        ])
        self.textEditor.delete("1.0", "end")
        self.textEditor.insert("1.0", file.read())
        file.close()

    def save(self):
        if self.passwordBox.get() != "I agree to being a sussy baka if i am using this for cheating":
            self.destroy()
            return
        filename = asksaveasfilename(filetypes=[
            ("Save file", ".json")
        ])
        text = self.textEditor.get("1.0", "end")
        with open(filename, "w") as file:
            file.write(text)
        with open(filename[:-5]+".hash", "wb") as file:
            file.write(md5(bytes(text, 'utf-8')).digest())


app = SaveForger()
