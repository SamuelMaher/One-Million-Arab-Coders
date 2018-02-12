import turtle

def draw_shapes():
    window= turtle.Screen()
    window.bgcolor("red")

    #cir = turtle.Turtle()
    #cir.shape("arrow")
    #cir.color("green")
    #cir.speed(1)
    #cir.circle(100)

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(1)
    j=0
    while(j<36):
        count=0
        while (count <4): 
         brad.forward(100)
         brad.right(90)
         count+=1
        j+=1
        brad.right(10)

        

  #  tri=turtle.Turtle()
  #  tri.shape("turtle")
  #  tri.color("black")
   # tri.speed(1)

   # count=0
   # while(count<3):
   #     cir.right(120)
   #     cir.forward(100)
    #    count+=1

    window.exitonclick()

draw_shapes()
