import tkinter
import random
from tkinter import PhotoImage
from tkinter import messagebox


def prepare_and_start():
    global player
    global ball
    global enemy

    canvas.delete("all")
    # генерация позиции игрока и его создание
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    player = canvas.create_image(
        (player_pos[0], player_pos[1]), image=player_pic, anchor='nw')
    master.bind("<KeyPress>", key_pressed)

    # генерация позиции мячика и его создание
    ball_pos = (random.randint(0, 650),
                random.randint(0, 650))
    ball = canvas.create_oval(ball_pos[0], ball_pos[1],
                              ball_pos[0] + 70, ball_pos[1] + 70)

    # генерация позиции врага и его создание
    enemy_pos = (random.randint(1, N_X - 1) * step,
                 random.randint(1, N_Y - 1) * step)
    enemy = canvas.create_image(
        (enemy_pos[0], enemy_pos[1]), image=enemy_pic, anchor='nw')


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

    # вывод координат по игроку и кругу
    # print('x1', canvas.bbox(player)[0], canvas.bbox(ball)[0])
    # print('y1', canvas.bbox(player)[1], canvas.bbox(ball)[1])
    # print('x2', canvas.bbox(player)[0] + 30, canvas.bbox(ball)[2])
    # print('y2', canvas.bbox(player)[1] + 50, canvas.bbox(ball)[3])

    # вывод координат по игроку и врагу
    print('x1', canvas.bbox(player)[0], canvas.bbox(enemy)[0])
    print('y1', canvas.bbox(player)[1], canvas.bbox(enemy)[1])
    print('x2', canvas.bbox(player)[2], canvas.bbox(enemy)[2])
    print('y2', canvas.bbox(player)[3], canvas.bbox(enemy)[3])

    # сравнение координат игрока и круга, если объекты соприкасаются - ты выиграл
    if ((canvas.bbox(player)[0] >= canvas.bbox(ball)[0] and canvas.bbox(player)[1] >= canvas.bbox(ball)[1]) and
    (canvas.bbox(player)[0] + 30 <= canvas.bbox(ball)[2] and canvas.bbox(player)[1] + 50 <= canvas.bbox(ball)[3])):
        messagebox.showinfo('Победа', 'Ты выиграл!')

    # сравнение координат игрока и врага, если объекты соприкасаются - ты проиграл
    elif (((canvas.bbox(player)[0] >= canvas.bbox(enemy)[0] and canvas.bbox(player)[1] + 20 >= canvas.bbox(enemy)[1]) and
    (canvas.bbox(player)[2] <= canvas.bbox(enemy)[2] + 30 and canvas.bbox(player)[3] - 20 <= canvas.bbox(enemy)[3])) or
        ((canvas.bbox(player)[0] >= canvas.bbox(enemy)[0] - 30 and canvas.bbox(player)[1] + 20 >= canvas.bbox(enemy)[1]) and
    (canvas.bbox(player)[2] <= canvas.bbox(enemy)[2] and canvas.bbox(player)[3] - 20 <= canvas.bbox(enemy)[3]))):
        messagebox.showinfo('Поражение', 'Ты проиграл!')


def key_pressed(event):
    if event.keysym == 'W' or event.keysym == 'Up':
        move_wrap(player, 0, -step)
    elif event.keysym == 'S' or event.keysym == 'Down':
        move_wrap(player, 0, step)
    elif event.keysym == 'A' or event.keysym == 'Left':
        move_wrap(player, -step, 0)
    elif event.keysym == 'D' or event.keysym == 'Right':
        move_wrap(player, step, 0)

    # генерация будущего хода врага и его ход
    step_enemy = random.choice([-step*5, step*5])
    choise_1 = random.choice([step_enemy, 0])
    choise_2 = 0
    if choise_1 == 0:
        choise_2 = step_enemy
    elif choise_1 != 0:
        choise_2 = 0

    move_wrap(enemy, choise_1, choise_2)


master = tkinter.Tk()
step = 16
N_X = 42
N_Y = 42
WIDTH = 700
HEIGHT = 700
a = False

canvas = tkinter.Canvas(master, bg='#FCAB08', width=WIDTH, height=HEIGHT)
player_pic = PhotoImage(file="player_pic.png")
enemy_pic = PhotoImage(file="enemy.png")

label = tkinter.Label(master, text="Найди выход!")
restart = tkinter.Button(master, text="Начать заново", command=prepare_and_start)
restart.pack()
label.pack()
canvas.pack()
prepare_and_start()

master.bind("<KeyPress>", key_pressed)
master.mainloop()
