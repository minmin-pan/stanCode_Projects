"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
import random
import time

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousemoved

# constant
BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.

# global variable
score = 0  # count score
count = 0  # count remove how many brick


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self._window = GWindow(width=window_width, height=window_height, title=title)

        # Start menu
        self._menu = GRect(self._window.width/4, self._window.height/10)
        self._menu.filled = True
        self._start_label = GLabel("Start!")
        self._start_label.color = 'white'
        self._start_label.font = 'Courier-20'
        self._window.add(self._menu, (self._window.width - self._menu.width) / 2,
                         (self._window.height - self._menu.height) / 2 + self._start_label.height * 2)
        self._window.add(self._start_label, (self._window.width - self._start_label.width) / 2,
                         (self._window.height + self._start_label.height) / 2 + self._start_label.height * 2)

        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height)
        self._paddle.filled = True
        self._window.add(self._paddle, (self._window.width - self._paddle.width) / 2,
                         self._window.height - PADDLE_OFFSET)

        # Center a filled ball in the graphical window
        self._ball = GOval(ball_radius * 2, ball_radius * 2)
        self._ball.filled = True
        self._window.add(self._ball, (self._window.width - self._ball.width) / 2,
                         (self._window.height - self._ball.height) / 2)

        # Create score label
        self._label = GLabel(f'Score:{score}')
        self._label.font = 'Courier-20'
        self._window.add(self._label, 0, self._label.height + 10)

        # create start time variable
        self._t0 = 0
        minute = 0
        minute = '%02d' % minute
        second = 0
        second = '%02d' % second
        self._timer = GLabel(f'Time:{minute}:{second}')
        self._timer.font = 'Courier-20'
        self._window.add(self._timer, self._window.width - self._timer.width, self._timer.height + 10)

        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Initialize our mouse listeners
        self._is_start = 0  # is a button to know start or not
        onmouseclicked(self.start)
        onmousemoved(self.__paddle_move)

        # brick setting
        # self._bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT)
        y = BRICK_OFFSET
        for i in range(BRICK_ROWS):
            x = 0
            if 0 <= i <= 1:
                b_color = '0x6F00D2'
            elif 2 <= i <= 3:
                b_color = '0x921AFF'
            elif 4 <= i <= 5:
                b_color = '0xB15BFF'
            elif 6 <= i <= 7:
                b_color = '0xCA8EFF'
            elif 8 <= i <= 9:
                b_color = '0xDCB5FF'
            for j in range(BRICK_COLS):
                self._bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self._bricks.filled = True
                self._bricks.fill_color = b_color
                self._bricks.color = b_color
                self._window.add(self._bricks, x, y)
                x += (BRICK_WIDTH + BRICK_SPACING)
            y += (BRICK_HEIGHT + BRICK_SPACING)

        self._menu_button = 0   # start menu button
        self._time_start = 0    # time_start button




    def detect_object(self):
        # detect object function
        for i in range(0, 3, 2):
            for j in range(0, 3, 2):
                probe = self._window.get_object_at(self._ball.x + i * BALL_RADIUS, self._ball.y + j * BALL_RADIUS)
                if probe is not None:
                    return probe

    def remove_brick(self, obj):
        # remove brick function
        global score, count
        if obj is not self._paddle and obj is not self._label and obj is not self._timer:
            self._window.remove(obj)
            score += 1
            count += 1
            self._label.text = f'Score:{score}'

    def get_dx(self):
        # Getter
        return self.__dx

    def get_dy(self):
        # Getter
        return self.__dy

    def set_dx(self):
        # Setter
        self.__dx *= -1

    def set_dy(self):
        # Setter
        self.__dy *= -1

    def __paddle_move(self, mouse):
        # private function (user can not reset)
        # paddle move function by mouse
        if self._paddle.width / 2 <= mouse.x <= self._window.width - self._paddle.width / 2:
            self._paddle.x = mouse.x - self._paddle.width / 2
            self._paddle.y = self._window.height - PADDLE_OFFSET

    def start(self, mouse):
        # use to let mouse click open the game
        time_button = 0
        self._is_start = 1
        if not self._time_start:
            self._time_start = 1
            time_button = 1
        if self._time_start:
            if time_button:
                self._t0 = time.time()
            self._window.remove(self._menu)
            self._window.remove(self._start_label)

    def get_start(self):
        # Getter
        return self._is_start

    def reset_start(self):
        # Setter
        self._is_start = 0
        self._time_start = 0

    def get_ball(self):
        # Getter
        return self._ball

    def get_window(self):
        # Getter
        return self._window

    def reset_ball(self):
        # use to reset ball to start site
        self._window.add(self._ball, (self._window.width - self._ball.width) / 2,
                         (self._window.height - self._ball.height) / 2)

    def get_label(self):
        # Getter
        return self._label

    def get_start_time(self):
        # Getter
        return self._t0

    def get_time_label(self):
        # Getter
        return self._timer

    def time_update(self, total_time):
        # use to time update
        minute = total_time // 60
        minute = '%02d' % minute
        second = total_time % 60
        second = '%02d' % second
        self._timer.text = f'Time:{minute}:{second}'

    def time_reset(self):
        # use to time reset
        minute = 0
        minute = '%02d' % minute
        second = 0
        second = '%02d' % second
        self._timer.text = f'Time:{minute}:{second}'

    @staticmethod
    def get_count():
        # Getter
        global count
        return count

    @staticmethod
    def total_brick():
        # Getter (get total how many brick)
        return BRICK_ROWS*BRICK_COLS

    def win_label(self):
        # show win
        win_label = GLabel('Win!!')
        win_label.font = 'Courier-30'
        self._window.add(win_label, (self._window.width-win_label.width)/2, (self._window.height-win_label.height)/2)

    def lose_label(self):
        # show lose
        win_label = GLabel('Lose!!')
        win_label.font = 'Courier-30'
        self._window.add(win_label, (self._window.width-win_label.width)/2, (self._window.height-win_label.height)/2)

    def paddle_improve(self, obj):
        # use to let ball not sticky in paddle
        if obj is self._paddle:
            self._ball.y = self._window.height-(self._paddle.height+PADDLE_OFFSET+self._ball.height)

    # def main_game(self):
        # show paddle
    #    self._window.add(self._paddle, (self._window.width - self._paddle.width) / 2, self._window.height - PADDLE_OFFSET)

        # show ball
    #    self._window.add(self._ball, (self._window.width - self._ball.width) / 2, (self._window.height - self._ball.height) / 2)

    # def menu(self):
    #    self.menu = GRect(self)


