"""
File: 
Name:
楊庭瑄
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


# Global Variable
# create a window width is 800  and height is 500 and show the title on thw window
window = GWindow(800, 500, title='bouncing_ball.py')
# We want to generate a ball that width is size and the height is size and the position is at the start_x and start_y
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
# need to calculate click_times at set to 1
click_times = 1
# need to set a on-off that can know to start
knock = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # need to let ball colored black
    ball.filled = True
    ball.fill_color = 'black'
    # need to let ball to add on the window
    window.add(ball)
    # to ensure after click and start
    onmouseclicked(bounce)


def bounce(event):
    """
    this function need to show the after click and a series of motion
    """
    # to change global variable number
    global click_times,knock
    # to set vy initial velocity
    vy = 0
    # to let click the ball and start move
    if not knock and click_times <= 3:
        # To start it
        knock = True
        # add one time
        click_times += 1
        # the ball move condition
        while ball.x < window.width:
            # to bounce condition
            if (ball.y+SIZE) > window.height:
                # to avoid move around the ground
                if vy > 0:
                    # to avoid bounce height beyond the last time
                    vy *= -REDUCE
            # whether go down or bounce back the vy will add gravity
            vy = GRAVITY + vy
            # will move at velocity (Vx,vy)
            ball.move(VX, vy)
            # and the pause time to avoid too fast
            pause(DELAY)
        # ball.x > window width and return to the origin position
        ball.x = START_X
        ball.y = START_Y
        # turn off the knock
        knock = False



if __name__ == '__main__':
    main()