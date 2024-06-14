from tkinter import Tk, Canvas, Button, PhotoImage

class MainMenu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Запомни одинаковые")
        self.center_window(900, 500)

        self.canvas = Canvas(self.root, width=900, height=500, highlightthickness=0)
        self.canvas.pack()

        self.create_buttons()
        self.add_images()

        self.root.mainloop()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

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

    def add_images(self):
        self.img_obj3 = PhotoImage(file="img_rules_menu/dio.png")
        self.canvas.create_image(0, 0, anchor='nw', image=self.img_obj3)

    def start_game(self):
        print("Начать игру")

    def show_rules(self):
        print("Показать правила")

    def exit_game(self):
        self.root.destroy()

# Запуск приложения
if __name__ == "__main__":
    MainMenu()