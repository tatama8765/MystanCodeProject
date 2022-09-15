"""
File: 
Name:
楊庭瑄
-------------------------

TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
# Global Variable
# to construct a window
window = GWindow()
# to count the time
count = 0
# to create a circle
circle = GOval(SIZE,SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    # as mouseclick and it will draw a line
    onmouseclicked(drawline)


def drawline(mouse):
    """
    This program will start to draw a circle or line
    """
    # because the count number will be changed so we need to calculate times
    global count
    # in even time
    if count % 2 == 0:
        # will draw a circle on the window and it will be mouseclick as the center
        window.add(circle,x=mouse.x-SIZE/2,y=mouse.y-SIZE/2)
        # to add the count
        count += 1
    # in odd time
    else:
        # will remove circle on the window first
        window.remove(circle)
        # and generate the line initial position is the last time center an the second time mouseclick position
        line = GLine(circle.x+SIZE/2,circle.y+SIZE/2,mouse.x,mouse.y)
        # to add a line on window
        window.add(line)
        # to add the count
        count += 1

if __name__ == "__main__":
    main()
