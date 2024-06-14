from tkinter import Tk

class MainMenu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Запомни одинаковые")
        self.root.geometry("900x500")
        self.root.mainloop()


if __name__ == "__main__":
    MainMenu()
