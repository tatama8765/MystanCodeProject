"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, __ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle_width = paddle_width
        self.paddle = GRect(width=self.paddle_width,height =paddle_height,x=(self.window_width-paddle_width)/2,y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(__ball_radius*2,__ball_radius*2,x=(self.window_width-BALL_RADIUS)/2,y=(self.window_height-BRICK_HEIGHT)/2)
        self.ball.filled = True
        self.ball.color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__ball_radius = BALL_RADIUS
        self.dx = random.randint(1, MAX_X_SPEED)
        self.dy = INITIAL_Y_SPEED
        self.__dx = self.dx
        self.__dy = self.dy
        if random.random() > 0.5:
            __dx = -self.__dx
        # Initialize our mouse listeners
        self.is_start = False

        onmousemoved(self.paddle_move)
        onmouseclicked(self.game_start)

        # to put the paddle on the window
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                color = ['lightblue', 'lightblue', 'plum', 'plum', 'pink', 'pink', 'palegreen', 'palegreen', 'burlywood', 'burlywood']
                self.bricks = GRect(BRICK_WIDTH,BRICK_HEIGHT,x=BRICK_WIDTH+i*(BRICK_WIDTH+BRICK_SPACING)-BRICK_WIDTH,y= BRICK_OFFSET+j*(BRICK_HEIGHT+BRICK_SPACING))
                self.bricks.fill_color = color[j]
                self.bricks.filled = True
                self.window.add(self.bricks)

    # to let the mouse can move to the paddle on the window
    def paddle_move(self,event):
        if self.paddle_width/2 <= event.x <= self.window_width-(self.paddle_width/2):
            self.paddle.x = (event.x-self.paddle.width/2)
            self.paddle.y = self.window_height - PADDLE_OFFSET

        #elif event.x >= self.window_width:
           #self.paddle.x = (event.x-self.paddle_width)/2
           # self.paddle.y = self.window_height - PADDLE_OFFSET
        #self.paddle.move(event.x + PADDLE_WIDTH / 2, PADDLE_OFFSET)

    # get (in order to get dx in user code)
    def get_dx_velocity(self):
        return self.__dx

    # get (in order to get dy in user code)
    def get_dy_velocity(self):
        return self.__dy

    # get (in order to get ball in user code)
    def ball(self):
        return self.ball

    # get (in order to game start in user code)
    def game_start(self,event):
         self.is_start = True

    # get (in order to get ball radius in user code)
    def get_ball_radius(self):
        return self.__ball_radius

    # get (in order to reset_start in user code)
    def reset_start(self):
        self.is_start = False




    # setter
