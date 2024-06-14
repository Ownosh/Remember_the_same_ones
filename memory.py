from tkinter import *
from random import shuffle

column = 7  # столбцы
row = 4  # строки
btn = []  # список кнопок
img = []
files = ['yellow.png', 'gold.png',
         'green.png', 'emerald.png', 'cyan.png',
         'blue.png', 'pink.png', 'azure.png',
         'bronze.png', 'purple.png', 'scarlet.png',
         'steel.png', 'silver.png'] * 2
shuffle(files)
fix = True
m = 0


def play(n):  # функция обработчик нажатия на кнопку
    global m, fix
    # print(btn[n].cget('image'))
    if btn[n].cget('image') != 'pyimage1': return
    btn[n].config(image=img[n])
    if fix:
        fix = False
    elif files[n] == files[m]:
        fix = True
    else:
        btn[m].config(image=imgBL)
    m = n


tk = Tk()
imgBL = PhotoImage(file="blank.png")
for i in files:
    img += [PhotoImage(file=i)]

for i in range(row):
    f = Frame()
    f.pack(expand=YES, fill=BOTH)
    for j in range(column):
        btn += [Button(f, image=imgBL)]
        btn[-1].pack(expand=YES, fill=BOTH, side=LEFT)
        btn[-1].config(command=lambda n=i * column + j: play(n))

mainloop()