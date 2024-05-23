import tkinter
import random
from tkinter import PhotoImage


def prepare_and_start():
    global player

    canvas.delete("all")
    # генерация позиции игрока и его создание
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    player = canvas.create_image(
        (player_pos[0], player_pos[1]), image=player_pic, anchor='nw')
    master.bind("<KeyPress>", key_pressed)


def move_wrap(obj, move_x, move_y):
    xy = canvas.coords(obj)  # тут выход координат игрока списком (х, у)
    canvas.move(obj, move_x, move_y)
    print(xy)
    if xy[0] <= 0:
        canvas.move(obj, WIDTH, 0)
    if xy[0] >= WIDTH:
        canvas.move(obj, -WIDTH, 0)
    if xy[1] <= 0:
        canvas.move(obj, 0, HEIGHT)
    if xy[1] >= HEIGHT:
        canvas.move(obj, 0, -HEIGHT)
        

def key_pressed(event):
    if event.keysym == 'W' or event.keysym == 'Up':
        move_wrap(player, 0, -step)
    elif event.keysym == 'S' or event.keysym == 'Down':
        move_wrap(player, 0, step)
    elif event.keysym == 'A' or event.keysym == 'Left':
        move_wrap(player, -step, 0)
    elif event.keysym == 'D' or event.keysym == 'Right':
        move_wrap(player, step, 0)


master = tkinter.Tk()
step = 16
N_X = 42
N_Y = 42
WIDTH = 700
HEIGHT = 700
a = False

canvas = tkinter.Canvas(master, bg='#FCAB08', width=WIDTH, height=HEIGHT)
player_pic = PhotoImage(file="player_pic.png")

label = tkinter.Label(master, text="Найди выход!")
restart = tkinter.Button(master, text="Начать заново", command=prepare_and_start)
restart.pack()
label.pack()
canvas.pack()
prepare_and_start()

master.bind("<KeyPress>", key_pressed)
master.mainloop()
