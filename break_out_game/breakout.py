"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    # Add the animation loop here!
    graphics = BreakoutGraphics()
    dx = graphics.get_dx_velocity()
    dy = graphics.get_dy_velocity()
    radius = graphics.get_ball_radius()
    num = NUM_LIVES
    paddle_offset = 50
    bricks_height = 15
    bricks_num = 100

    while True:
        # to start the game
        if graphics.is_start and num >= 0:
            graphics.ball.move(dx, dy)
        # if ball falls down the window and put the ball to the original position
        if graphics.ball.y + graphics.ball.height >= graphics.window_height:
            dy = -dy
            graphics.ball.move(dx, dy)
            num -= 1
            graphics.reset_start()
            graphics.ball.x = (graphics.window_width - graphics.paddle_width) / 2
            graphics.ball.y = (graphics.window_height - bricks_height)/2
        # if ball falls down the window and bounce back
        if graphics.ball.x <= 0 or graphics.ball.width + graphics.ball.x >= graphics.window_width:
            dx = -dx
            graphics.ball.move(dx, dy)
        # the collision for four conditions
        upper_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        upper_right = graphics.window.get_object_at(graphics.ball.x + 2 * radius, graphics.ball.y)
        lower_right = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * radius)
        lower_left = graphics.window.get_object_at(graphics.ball.x + 2 * radius,graphics.ball.y + 2 * radius)
        if upper_left is not None:
            # ball collsion to paddle
            if upper_left is graphics.paddle:
                dy = -dy
                graphics.ball.move(dx, dy)
                # to avoid ball into paddle
                graphics.ball.y = graphics.window_height - (graphics.paddle.height + paddle_offset + radius)
            # ball collsion to bricks
            else:
                dy = -dy
                graphics.ball.move(dx, dy)
                graphics.window.remove(upper_left)
                bricks_num -= 1
        elif upper_right is not None:
            # ball collsion to paddle
            if upper_right is graphics.paddle:
                dy = -dy
                graphics.ball.move(dx, dy)
                graphics.ball.y = graphics.window_height - (graphics.paddle.height + paddle_offset + radius)

            # ball collsion to bricks
            else:
                dy = -dy
                graphics.ball.move(dx, dy)
                graphics.window.remove(upper_right)
                bricks_num -= 1

        elif lower_right is not None:

            # ball collsion to paddle
            if lower_right is graphics.paddle:
                dy = -dy
                graphics.ball.move(dx, dy)
                graphics.ball.y = graphics.window_height - (graphics.paddle.height + paddle_offset + radius)

            # ball collsion to bricks
            else:
                dy = -dy
                graphics.ball.move(dx, dy)
                graphics.window.remove(lower_right)
                bricks_num -= 1

        elif lower_left is not None:
            # ball collsion to paddle
            if lower_left is graphics.paddle:
                dy = -dy
                graphics.ball.move(dx, dy)
                graphics.ball.y = graphics.window_height - (graphics.paddle.height + paddle_offset + radius)
                # ball collsion to bricks
            else:
                dy = -dy
                graphics.ball.move(dx, dy)
                graphics.window.remove(lower_left)
                bricks_num -= 1

        # the game finish condition
        if bricks_num == 0 or num == 0:
            break
        # to avoid animation too fast
        pause(FRAME_RATE)



                # list = [upper_left, upper_right, lower_right, lower_left]
                # for i in list:
                #     if list is not None and list is not graphics.paddle:
                #         dy = -dy
                #         graphics.ball.move(dx, dy)
                #         graphics.window.remove(list)
                #         bricks_num -= 1
                #
                #     elif list is not None and list is not graphics.bricks:
                #         dy = -dy
                #         graphics.ball.move(dx, dy)










if __name__ == '__main__':
    main()
