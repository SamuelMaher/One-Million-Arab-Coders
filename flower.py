import turtle

def draw_flower():
    window= turtle.Screen()
    window.bgcolor("white")

   

    flower=turtle.Turtle()
    flower.shape("arrow")
    flower.color("red")
    flower.speed(10)
    j=0
    while(j<36):
        #flower.color("random")
        count=0
        while(count<3):
            flower.right(120)
            flower.forward(100)
            count+=1
        j+=1
        flower.right(10)

        
        
    window.exitonclick()

draw_flower()
