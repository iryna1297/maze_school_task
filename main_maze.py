import turtle
import tkinter as tk


# Створюємо вікно
root = tk.Tk()
root.title("Maze Game")
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Створюємо об'єкт черепашки
player = turtle.RawTurtle(canvas)
player.shape('turtle')
player.color('blue')
player.penup()

# Малюємо лабіринт
def draw_maze():
    global walls
    walls = [(-250, 250, -250, -50), (-250, 150, -50, 150), (0, 150, 250, 150), (50, 100, 250, 100),
             (-250, 50, -50, 50), (-150, 50, -150, -50), (-150, -50, 0, -50), (0, 0, 100, 0),
             (50, -50, 50, -250), (250, -250, 250, 0), (100, -100, 250, -100), (0, -200, 250, -200),
             (-50, 50, -50, -250), (-250, -250, -250, -50), (-150, 150, -150, 50), (50, 150, 50, 100),
             (-150, -150, -100, -150), (-100, -150, -100, -100), (-50, -100, 0, -100), (0, -100, 0, -50),
             (150, -150, 100, -150), (100, -150, 100, -200), (-100, -200, -100, -150), (-100, -150, -50, -150),
             (-50, -200, 50, -200), (-50, -150, -50, -150), (50, -150, 50, -100), (50, -150, 100, -150),
             (100, -200, 100, -150), (50, -200, 50, -250), (0, -250, 50, -250), (-50, -250, -50, -200),
             (-100, -200, -50, -200)]

    goals = [(180, -180)]

    for wall in walls:
        x1, y1, x2, y2 = wall
        player.penup()
        player.goto(x1, y1)
        player.pendown()
        player.goto(x2, y2)

    for goal in goals:
        x, y = goal
        player.penup()
        player.goto(x, y)
        player.dot(35, "green")

    player.penup()
    player.goto(-180, 180)
    player.dot(35, "yellow")

draw_maze()

# Визначаємо функції переміщення
def go_up():
    player.setheading(90)
    if (player.xcor(), player.ycor() + 10) not in walls:
        player.forward(10)

def go_down():
    player.setheading(270)
    if (player.xcor(), player.ycor() - 10) not in walls:
        player.forward(10)

def go_left():
    player.setheading(180)
    if (player.xcor() - 10, player.ycor()) not in walls:
        player.forward(10)

def go_right():
    player.setheading(0)
    if (player.xcor() + 10, player.ycor()) not in walls:
        player.forward(10)


canvas.bind_all('<Up>', lambda event: go_up())
canvas.bind_all('<Down>', lambda event: go_down())
canvas.bind_all('<Left>', lambda event: go_left())
canvas.bind_all('<Right>', lambda event: go_right())



# Запускаємо гру
root.mainloop()

