# # Write your game here

# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon

# To make this work, you may have to type this into the terminal --> pip install curses
import curses
import time
import random

game_data = {
    'width': 10,
    'height': 10,
    'player': {"x": 9, "y": 9,},
    'block_pos': {"x": 0, "y": 0},
    'ball_pos': {"x": 4, "y": 4},

    # ASCII icons
    'ball': "\U000026AA",
    'block': "\U0001F532",
    'paddle': "\U00002796\U00002796",
    'empty': "  "
}

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['paddle']
            # Block
            elif x == game_data['block_pos']['x'] and y == game_data['block_pos']['y']:
                row += game_data['block']
            # Ball
            elif x == game_data['ball_pos']['x'] and y == game_data['ball_pos']['y']:
                row += game_data['ball']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()

    if key == "a" and x > 0:
        new_x -= 1
    elif key == "d" and x < game_data['width'] - 1:
        new_x += 1
    else:
        return  # Invalid key or move off board

    # Update position and increment score
    game_data['player']['x'] = new_x
    game_data['player']['y'] = new_y


def move_ball():
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    random.shuffle(directions)
    ex, ey = game_data['ball_pos']['x'], game_data['ball_pos']['y']

    for dx, dy in directions:
        new_x = ex + dx
        new_y = ey + dy
        if 0 <= new_x < game_data['width'] and 0 <= new_y < game_data['height']:
                game_data['ball_pos']['x'] = new_x
                game_data['ball_pos']['y'] = new_y
                break

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break
            move_player(key)

            move_ball()

            draw_board(stdscr)
            time.sleep(0.2)

curses.wrapper(main)   