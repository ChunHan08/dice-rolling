import dice
import turtle 

def reroll():
  turtle.clear()
  turtle.tracer(0, 0)

  dice.Die(0, 0, 100, 10, "cyan", "white")

  dice.Die(0, 150, 100, 10, "cyan", "white")

  dice.Die(0, -150, 100, 10, "cyan", "white")
  turtle.update()
  
reroll()
turtle.onkey(reroll, "space")

turtle.listen()
turtle.mainloop()