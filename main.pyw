from tkinter import *
from tkinter import ttk
from os.path import exists
from os import listdir
from os import remove
import datetime
import json
import hashlib
# Don't look at the cheats unless you wanna be a sussy baka


def cheat_devil(self):
    self.cookies += 666
    self.update_cookie_count()
    self.CheatText.config(text="The devil grants you 666 cookies")


def cheat_4th(self):
    if datetime.date.month == 5:
        if datetime.date.day == 4:
            self.cookies *= 2
            self.update_cookie_count()
            self.CheatText.config(text="May the 4th be with you")
            return
    self.CheatText.config(text="Try again later ;)")
    self.cookies += 1
    self.update_cookie_count()


def cheat_rosebud(self):
    self.cookies += 100
    self.update_cookie_count()
    self.CheatText.config(text="ah so you like the sims eh?")


def cheat_begone(self):
    self.CheatText.config(text="You can't read this because you threw the cheat tab into oblivion")
    self.Tabs.forget(2)
    self.Tabs.add(self.CheatsGoneTab, text="Cheats")
    self.Tabs.select(2)


def cheat_show(self):
    self.CheatInput.config(show="")


class App(Tk):
    cookies = 0
    upgrades = [
        0,
        0
    ]
    cheatNames = [
        "666",
        "may the 4th be with you",
        "rosebud",
        "sv_cheats 0",
        "show"
    ]
    cheats = [
        cheat_devil,
        cheat_4th,
        cheat_rosebud,
        cheat_begone,
        cheat_show
    ]
    upgradeCosts = [
        5,
        10
    ]
    saveVer = 0
    saveData = None

    def __init__(self, savefile):
        super().__init__()
        self.wm_title("Py Clicker")
        self.Tabs = ttk.Notebook(self, width=400, height=300)
        self.ClickerTab = Frame(self.Tabs)
        self.UpgradesTab = Frame(self.Tabs)
        self.CheatsTab = Frame(self.Tabs)
        self.CheatsGoneTab = Frame(self.Tabs)
        self.SaveTab = Frame(self.Tabs)
        self.Tabs.add(self.ClickerTab, text="Clicker")
        self.Tabs.add(self.UpgradesTab, text="Upgrades")
        self.Tabs.add(self.CheatsTab, text="Cheats")
        self.Tabs.add(self.SaveTab, text="Save")
        self.Tabs.pack()
        # Click Tab
        self.CookiesCounter = Label(self.ClickerTab, text="0 cookies")
        self.CookiesCounter.grid(row=0, column=0, rowspan=1, columnspan=1)
        self.ClickButton = Button(self.ClickerTab, text="Click", command=self.click)
        self.ClickButton.grid(row=1, column=0, rowspan=1, columnspan=1)
        # Cheats Tab
        self.CheatInput = Entry(self.CheatsTab, show="*")
        self.CheatInput.grid(row=0, column=0)
        self.CheatInput.bind("<Return>", lambda e: self.cheat())
        self.CheatButton = Button(self.CheatsTab, text="Done", command=self.cheat)
        self.CheatButton.grid(row=0, column=1)
        self.CheatText = Label(self.CheatsTab, text="Enter a cheat then hit done or press enter")
        self.CheatText.grid(row=1, column=0, columnspan=2)
        # Cheats Gone Tab
        self.GoneFishing = Label(self.CheatsGoneTab, text="Gone Fishing")
        self.GoneFishing.pack()
        if exists(savefile):
            with open(savefile, "r") as file:
                data = json.load(file)
                self.saveData = data
                if data["saveVer"] == self.saveVer:
                    self.cookies = data["cookies"]
                    self.upgrades = data["upgrades"]
                    self.upgradeCosts = data["upgradeCosts"]
        # Save Tab
        self.SaveFile = Entry(self.SaveTab)
        if savefile[6:-5] != "NewGame":
            self.SaveFile.insert(0, savefile[6:-5])
        self.SaveFile.grid(row=0, column=0)
        self.SaveButton = Button(self.SaveTab, text="Save", command=self.save)
        self.SaveButton.grid(row=0, column=1)
        Label(self.SaveTab, text="-- Saves --").grid(row=1, column=0, columnspan=2)
        self.row = 2
        for file in listdir("saves"):
            if file.endswith(".json"):
                label = Label(self.SaveTab, text=file[:-5])
                label.grid(row=self.row, column=0, columnspan=2)
                self.row += 1
        # Upgrades Tab
        self.UpgradeCookiesCounter = Label(self.UpgradesTab, text="0 cookies")
        self.UpgradeCookiesCounter.grid(row=0, column=0)
        self.UpgradeClicker = Button(self.UpgradesTab,
                                     text='Buy Clicker ({:d} cookies) {:d}'.format(self.upgradeCosts[0],
                                                                                   self.upgrades[0]),
                                     command=self.upgrade_clicker_buy)
        self.UpgradeClicker.grid(row=1, column=0)
        self.UpgradeAmount = Button(self.UpgradesTab,
                                    text='Buy Better Equipment ({:d} cookies) {:d}'.format(self.upgradeCosts[1],
                                                                                      self.upgrades[1]),
                                    command=lambda: self.buy_upgrade(1, self.UpgradeAmount,
                                                                     "Buy Better Equipment "))
        self.UpgradeAmount.grid(row=2, column=0)
        for i in range(len(self.upgrades)):
            if i == 0:
                for j in range(self.upgrades[i]):
                    self.after(10000, self.do_click_upgrade_better)
        self.update_cookie_count()

    def click(self):
        self.cookies += self.upgrades[1] + 1
        self.update_cookie_count()

    def cheat(self):
        if self.CheatInput.get().lower() in self.cheatNames:
            self.cheats[self.cheatNames.index(self.CheatInput.get().lower())](self)
            self.CheatInput.delete(0, "end")
            return
        self.CheatInput.delete(0, "end")
        self.CheatText.config(text="Cheater cheater pumpkin eater")
        self.cookies -= 100
        self.update_cookie_count()

    def buy_upgrade(self, upgrade, button, button_format):
        if self.cookies >= self.upgradeCosts[upgrade]:
            self.cookies -= self.upgradeCosts[upgrade]
            self.update_cookie_count()
            self.upgrades[upgrade] += 1
            self.upgradeCosts[upgrade] += self.upgrades[upgrade] * 2
            button.config(text=button_format+'({:d} cookies) {:d}'.format(self.upgradeCosts[upgrade],
                                                                          self.upgrades[upgrade]))

    def update_cookie_count(self):
        self.CookiesCounter.config(text='{:d} cookies'.format(self.cookies))
        self.UpgradeCookiesCounter.config(text='{:d} cookies'.format(self.cookies))

    def do_click_upgrade_better(self):
        self.click()
        self.after(10000, self.do_click_upgrade_better)

    def upgrade_clicker_buy(self):
        self.buy_upgrade(0, self.UpgradeClicker, "Buy Clicker ")
        self.after(10000, self.do_click_upgrade_better)

    def save(self):
        if not exists("saves/"+self.SaveFile.get()+".json"):
            Label(self.SaveTab, text=self.SaveFile.get()).grid(row=self.row, column=0, columnspan=2)
        with open("saves/"+self.SaveFile.get()+".json", "w") as file:
            json.dump({
                "saveVer": self.saveVer,
                "cookies": self.cookies,
                "upgrades": self.upgrades,
                "upgradeCosts": self.upgradeCosts
            }, file, indent=4)
        with open("saves/"+self.SaveFile.get()+".hash", "wb") as hashfile:
            with open("saves/" + self.SaveFile.get() + ".json", "r") as file:
                fsdgsdghsd = hashlib.md5()
                fsdgsdghsd.update(bytes(file.read(), "utf-8"))
                hashfile.write(fsdgsdghsd.digest())


class SaveFileButtons(Tk):
    def __init__(self, master=None, file="NewGame.json", command=None, delcommand=None):
        self.selectButton = Button(master, text=file[:-5], command=self.select)
        self.deleteButton = Button(master, text="Delete", command=self.delselect)
        self.command = command
        self.delcommand = delcommand
        self.file = file

    def select(self):
        if self.command is not None:
            self.command(self)

    def delselect(self):
        if self.delcommand is not None:
            self.delcommand(self)


app = None


class SaveFilePicker(Tk):
    buttons = []

    def __init__(self):
        super().__init__()
        self.minsize(200, 0)
        Button(self, text="New Game", command=self.start_new_game).grid(row=0, column=0)
        filesa = listdir("saves")
        files = []
        for file in filesa:
            if not file.endswith(".json"):
                continue
            with open("saves/" + file, "r") as filedata:
                fsdgsdghsd = hashlib.md5()
                fsdgsdghsd.update(bytes(filedata.read(), "utf-8"))
                if not exists("saves/" + file[:-5] + ".hash"):
                    continue
                with open("saves/" + file[:-5] + ".hash", "rb") as hashfile:
                    inputhash = hashfile.read()
                    if fsdgsdghsd.digest() == inputhash:
                        files.append(file)
                    else:
                        print("file failed hash check")
        for i in range(len(files)):
            self.buttons.append(SaveFileButtons(self, files[i], self.start, self.del_command))
            self.buttons[-1].selectButton.grid(row=i+1, column=0)
            self.buttons[-1].deleteButton.grid(row=i+1, column=1)
        self.mainloop()

    def start(self, button):
        global app
        app = App("saves/"+button.file)
        self.destroy()
        app.mainloop()

    def start_new_game(self):
        global app
        app = App("NewGame.json")
        self.destroy()
        app.mainloop()

    def del_command(self, button):
        button.selectButton.grid_forget()
        button.deleteButton.grid_forget()
        remove("saves/"+button.file)
        remove("saves/"+button.file[:-5]+".hash")


savePicker = SaveFilePicker()
