from Tkinter import Tk
from markwhat.ui.main_window import MainWindow


def main():
    root = Tk()
    app = MainWindow(root)
    # root.geometry("300x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
