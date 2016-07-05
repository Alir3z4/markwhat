from Tkconstants import BOTH, W, END, NSEW
from Tkinter import Frame, StringVar
from ttk import Style, Label, Button

from tkinterhtml import HtmlFrame

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
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.markwhat_label = Label(self, text="Markwhat")
        self.markwhat_label.grid(sticky=W, row=0, column=0)

        self.markwhat_textarea = WhatText(self, background='white')
        self.markwhat_textarea.grid(row=1, column=0, sticky=NSEW)
        self.markwhat_textarea.beenModified = self.on_markwhat_modfified

        self.markup_label = Label(self, text="Markup")
        self.markup_label.grid(sticky=W, row=0, column=1)

        self.markup_preview = HtmlFrame(self)
        self.markup_preview.grid(row=1, column=1, sticky=NSEW)

        self.preview_button_text = StringVar()
        self.preview_button = Button(
            self,
            textvariable=self.preview_button_text,
            command=self.on_preview_click,
        )
        self.preview_button_text.set('HTML')
        self.preview_button.grid(row=2, column=1, sticky=W)

    def on_markwhat_modfified(self, event):
        text = self.markwhat_textarea.get('1.0', END)
        markup_text = parse_markdown(text)

        if isinstance(self.markup_preview, HtmlFrame):
            self.markup_preview.set_content(markup_text)
        else:
            self.markup_preview.delete('1.0', END)
            self.markup_preview.insert('1.0', markup_text)

    def on_preview_click(self):
        if isinstance(self.markup_preview, HtmlFrame):
            self.markup_preview = WhatText(self, background="white")
            self.preview_button_text.set('HTML')
        else:
            self.markup_preview = HtmlFrame(self)
            self.preview_button_text.set('HTML Source')

        self.markup_preview.grid(row=1, column=1, sticky=NSEW)
        self.on_markwhat_modfified(None)
