from functools import update_wrapper
from tkinter.font import BOLD
from turtle import*
bgcolor('black')
color('red')
begin_fill()
pensize(5)
setposition(0,0)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
penup
setposition(0,200)
pendown()
write("LOVE FROM RITESH",Font=("Verdana",20, " bold"))
hideturtle()
done()