from graphics import *

def main():

    win = GraphWin('Basic Python Graphics', 1400, 1200) # give title and dimensions

    win.setBackground("black")

    print("lemons are nice")
    #win.yUp() # make right side up coordinates!

    ## new images
    head = Circle(Point(700,300), 250) # set center and radius
    head.setFill("white")
    head.draw(win)

    eye3a = Circle(Point(600, 200), 30)
    eye3a.setFill('lightblue')
    eye3a.draw(win)

    eye3b = Circle(Point(600, 200), 5)
    eye3b.setFill('black')
    eye3b.draw(win)

    eye4a = Circle(Point(800, 200), 30)
    eye4a.setFill('lightblue')
    eye4a.draw(win)

    eye4b = Circle(Point(800, 200), 5)
    eye4b.setFill('black')
    eye4b.draw(win)

    nose1 = Oval(Point(650,250), Point(750,350)) # set center and radius
    nose1.setFill("orange")
    nose1.draw(win)


    mouth2a = Oval(Point(600,400), Point(800,420)) # set center and radius
    mouth2a.setFill("red")
    mouth2a.draw(win)

    mouth2b = Oval(Point(600,410), Point(800,430)) # set center and radius
    mouth2b.setFill("red")
    mouth2b.draw(win)


    message = Text(Point(win.getWidth()/2, 700), 'Mirror Mirror on the Wall.')
    message.draw(win)
    message.setTextColor("white")
    message.setSize(36)
    win.getMouse()
    win.close()

main()
