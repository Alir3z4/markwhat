from Tkconstants import BOTH, W, END
from Tkinter import Frame
from ttk import Style, Label
from markwhat.parsers import parse_markdown
from markwhat.ui.widgets.what_text import WhatText


class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.setupUI()

    def setupUI(self):
        self.master.title("Markwhat")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.markwhat_label = Label(self, text="Markwhat")
        self.markwhat_label.grid(sticky=W, row=0, column=0)

        self.markwhat_textarea = WhatText(self, background='white')
        self.markwhat_textarea.grid(row=1, column=0)
        self.markwhat_textarea.beenModified = self.on_markwhat_modfified

        self.markup_label = Label(self, text="Markup")
        self.markup_label.grid(sticky=W, row=0, column=1)

        self.markup_textarea = WhatText(self, background="white")
        self.markup_textarea.grid(row=1, column=1)

    def on_markwhat_modfified(self, event):
        text = self.markwhat_textarea.get('1.0', END)
        self.markup_textarea.delete('1.0', END)
        markup_text = parse_markdown(text)
        self.markup_textarea.insert('1.0', markup_text)


