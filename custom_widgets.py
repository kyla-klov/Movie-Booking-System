import tkinter as tk

#widgets for main program
class MainButton(tk.Button):
    def __init__(self, root, *args, **kwargs):
        tk.Button.__init__(self, root, *args, **kwargs)
        self.root = root
        self["font"] = "Helvetica", 15
        self["fg"] = "orange"
        self["bg"] = "#46464a"
        self["activeforeground"] = "orange"
        self["activebackground"] = "#2c2c2e"
        self["cursor"] = "hand2"

class WhiteLabel(tk.Label):
    def __init__(self, root, *args, **kwargs):
        tk.Label.__init__(self, root, *args, **kwargs)
        self.root = root
        self["font"] = "Ariel", 11
        self["fg"] = "white"
        self["bg"] = "#46464a"

class OrangeButton(tk.Button):
    def __init__(self, root, *args, **kwargs):
        tk.Button.__init__(self, root, *args, **kwargs)
        self.root = root
        self["fg"] = "white"
        self["bg"] = "orange"
        self["activeforeground"] = "white"
        self["activebackground"] = "#8a6603"

class GreyEntry(tk.Entry):
    def __init__(self, root, *args, **kwargs):
        tk.Entry.__init__(self, root, *args, **kwargs)
        self.root = root
        self["font"] = "Ariel", 10
        self["width"] = 30
        self["fg"] = "white"
        self["bg"] = "#46464a"

class PriceRadiobutton(tk.Radiobutton):
    def __init__(self, root, *args, **kwargs):
        tk.Radiobutton.__init__(self, root, *args, **kwargs)
        self.root = root
        self["font"] = "Ariel", 11
        self["fg"] = "black"
        self["bg"] = "orange"
        self["activeforeground"] = "black"
        self["activebackground"] = "orange"
