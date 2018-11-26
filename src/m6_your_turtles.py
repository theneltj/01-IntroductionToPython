"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Tyler Thenell.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.tracer(2)
john = rg.SimpleTurtle("circle")
john.pen = rg.Pen("white",0)
john.forward(300)
john.left(90)
john.pen = rg.Pen('blue',3)
john.forward(200)
for k in range(54):
    john.right(10)
    john.forward(2)
john.forward(200)
john.backward(200)
john.forward(200)

tim = rg.SimpleTurtle("square")
tim.speed = 500
tim.pen = rg.Pen('red',3)
tim.left(90)
for i in range(615):
    tim.forward(i)
    tim.right(135)
    if i > 200:
        tim.pen = rg.Pen('dark orange', 3)
    if i > 400:
        tim.pen = rg.Pen('gold', 3)
    if i > 600:
        tim.pen = rg.Pen('black', 3)
window.close_on_mouse_click()