# # Write your game here
# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon

# To make this work, you may have to type this into the terminal --> pip install curses
import curses

game_data = {
    'width': 15,
    'height': 15,
    'player': {"x": 4, "y": 4, "score": 0},
    'block_pos': {"x": 0, "y": 0},

    # ASCII icons
    'ball': "\U000026AA",
    'block': "\U0001F532",
    'paddle': "\U00002796 ",
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
            elif x ==game_data['ball'][game_data['ball']['x']] and y == game_data['ball']['y']:
                row += game_data['ball']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

<<<<<<< HEAD
curses.wrapper(draw_board)
=======
# curses.wrapper(draw_board)

>>>>>>> c6460a6 (ahhh)
