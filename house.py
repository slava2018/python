from  turtle import *

house = Turtle()

house.down()
house.screen.setup(900, 900)

for side in range(4):
    house.forward(200)
    house.left(90)

house.circle(30)


house.screen.exitonclick()
house.screen.mainloop()

