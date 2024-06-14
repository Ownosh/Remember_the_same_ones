from tkinter import Tk, Canvas, Button

class MainMenu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Запомни одинаковые")
        self.root.geometry("900x500")

        self.canvas = Canvas(self.root, width=900, height=500, highlightthickness=0)
        self.canvas.pack()

        self.create_buttons()

        self.root.mainloop()

    def create_buttons(self):
        play_button = Button(self.root, text="Играть", fg="Black", font=('times new roman', 15), bg='#F4FBED',
                             width=18, height=1, command=self.start_game)
        self.canvas.create_window(560, 200, anchor='nw', window=play_button)

        rules_button = Button(self.root, text="Правила", fg="Black", font=('times new roman', 15), bg='#F4FBED',
                              width=18, height=1, command=self.show_rules)
        self.canvas.create_window(560, 260, anchor='nw', window=rules_button)

        exit_button = Button(self.root, text="Выход", fg="Black", font=('times new roman', 15), bg='#F4FBED',
                             width=18, height=1, command=self.exit_game)
        self.canvas.create_window(560, 320, anchor='nw', window=exit_button)

    def start_game(self):
        print("Начать игру")

    def show_rules(self):
        print("Показать правила")

    def exit_game(self):
        self.root.destroy()

# Запуск приложения
if __name__ == "__main__":
    MainMenu()