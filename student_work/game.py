# # Write your game here

# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon

# To make this work, you may have to type this into the terminal --> pip install curses
import curses
import time

game_data = {
    'width': 10,
    'height': 10,
    'player': {"x": 9, "y": 9,},
    'block_pos': {"x": 0, "y": 0},
    'ball_pos': {"x": 4, "y": 4},

    # ASCII icons
    'ball': "\U000026AA",
    'block': "\U0001F532\U0001F532\U0001F532\U0001F532\U0001F532\U0001F532\U0001F532\U0001F532\U0001F532",
    'paddle': "\U00002796\U00002796",
    'empty': "  "
}


def draw_board(stdscr):
    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['paddle']
            elif x == game_data['block_pos']['x'] and y == game_data['block_pos']['y']:
                row += game_data['block']
            elif x == game_data['ball_pos']['x'] and y == game_data['ball_pos']['y']:
                row += game_data['ball']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row)
    stdscr.refresh()

def move_player(key):
    x = game_data['player']['x']
    if key.lower() == "a" and x > 0:
        game_data['player']['x'] -= 1
    elif key.lower() == "d" and x < game_data['width'] - 1:
        game_data['player']['x'] += 1

def move_ball():
    ball = game_data['ball_pos']
    
    # Calculate next position
    new_x = ball['x'] + ball['dx']
    new_y = ball['y'] + ball['dy']

    # Wall Collision Logic
    # Bounce Left/Right
    if new_x < 0 or new_x >= game_data['width']:
        ball['dx'] *= -1
        new_x = ball['x'] + ball['dx']

    # Bounce Top/Bottom
    if new_y < 0 or new_y >= game_data['height']:
        ball['dy'] *= -1
        new_y = ball['y'] + ball['dy']

    # Update actual position
    ball['x'] = new_x
    ball['y'] = new_y

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key and key.lower() == "q":
            break
        
        if key:
            move_player(key)

        move_ball()
        draw_board(stdscr)
        time.sleep(0.1)

    curses.wrapper(main)