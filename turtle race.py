
# import colorgram
# colors=colorgram.extract("20_001.jpg",10)
# first_color=colors[1]
# first_color_rgb=first_color.rgb
# tiger=Turtle()
# tiger.color(first_color_rgb)
#
# screen=Screen()
# screen.exitonclick()
# screentim=Turtle()
# screen=Screen()

# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def move_left():
#     tim.left(10)
# def move_right():
#     tim.right(10)
# def clears():
#     tim.clear()
#     tim.home()
# screen.listen()
#
# screen.onkey(key="p",fun=move_forward)
# screen.onkey(key="w",fun=move_backward)
# screen.onkey(key="b",fun=move_left)
# screen.onkey(key="t",fun=move_right)
# screen.onkey(key="c",fun=clears)
# screen.exitonclick()
############### Turtle Race ##################
#





import random
from turtle import Turtle ,Screen
screen=Screen()
screen.setup(500,500)
user__bet=screen.textinput(title="Enter  the  color",prompt="Color")
list_of_turtle=[]
color_list=["red","blue","green","yellow","black","pink","orange"]
x=-200
y=-150
is_race=False
for i in range(0,7):
    tim = Turtle("turtle")
    list_of_turtle.append(tim)
    tim.color(color_list[i])
    tim.penup()
    tim.goto(x,y)

    y=y+40
if user__bet:
    is_race=True

while is_race:
    for t  in  list_of_turtle:
        if t.xcor() > 230:
            is_race=False
            pencolor= t.color()[0]
            if pencolor==user__bet:
                print(f"you win , the winner color is {t.color()[0]}")
            else:
                print(f"You lose , ths winner color is {t.color()[0]}")
        fd=random.randint(0,5)
        t.forward(fd)


screen.exitonclick()

######### shanke game ##############
# POSITION=[(0,0),(-20,0),(-40,0)]
# class Snake_move():
#     import random
#     from turtle import Turtle,Screen
#     import time
#     screen=Screen()
#     screen.setup(500,500)
#     screen.bgcolor("black")
#     screen.tracer(0)
#     list_snake=[]
#     y=0
#     x=0
#     for i in range(3):
#         snake=Turtle("square")
#         snake.color("white")
#         snake.penup()
#         snake.goto(POSITION[i])
#
#         list_snake.append(snake)
#     game_on=True
#     while game_on:
#         screen.update()
#         time.sleep(0.1)
#         for seg_num in range(len(list_snake)-1,0,-1):
#             new_x=list_snake[seg_num-1].xcor()
#             new_y=list_snake[seg_num-1].ycor()
#             list_snake[seg_num].goto(new_x,new_y)
#         list_snake[0].forward(20)
#         # for i in list_snake:
#         #     i.forward(20)
#
#     screen.exitonclick()
# movement=Snake_move()
#
#
#
#
#
#
#
#
#








