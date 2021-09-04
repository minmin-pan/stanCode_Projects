"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension_1 import BreakoutGraphics
import time

# constant
FRAME_RATE = 1000 / 120         # 120 frames per second
NUM_LIVES = 3			        # Number of attempts


def main():
    graphics = BreakoutGraphics()
    blood = NUM_LIVES       # have how many run
    # Add animation loop here!
    while True:
        if graphics.get_count() == graphics.total_brick():
            graphics.win_label()
            break
        elif blood == 0:
            graphics.lose_label()
            break
        if graphics.get_start():
            if blood > 0:
                # if ball drop lower than window bottom need reset ball, minus one blood, and button reset
                if graphics.get_ball().y > graphics.get_window().height:
                    blood -= 1
                    graphics.reset_start()
                    graphics.reset_ball()
                # detect ball have hit brick or not, if hit brick need to remove and ball need rebound
                obj = graphics.detect_object()
                if obj is not None:
                    if obj is not graphics.get_label() and obj is not graphics.get_time_label():
                        graphics.paddle_improve(obj)
                        graphics.set_dy()
                    graphics.remove_brick(obj)
                # if ball hit the wall(up, left, right) need to rebound
                graphics.get_ball().move(graphics.get_dx(), graphics.get_dy())
                if graphics.get_ball().x <= 0 \
                        or graphics.get_ball().x + graphics.get_ball().width >= graphics.get_window().width:
                    graphics.set_dx()
                if graphics.get_ball().y <= 0:
                    graphics.set_dy()
                t2 = time.time()
                total_time = t2 - graphics.get_start_time()
                graphics.time_update(total_time)
        else:
            graphics.time_reset()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
