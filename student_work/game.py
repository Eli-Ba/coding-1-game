import curses
import time

# -- FIXED DATA --
game_data = {
    'width': 10,
    'height': 10,
    'player': {"x": 4, "y": 9}, # Started in center
    'block_pos': {"x": 0, "y": 0},
    # REMOVED random options, added constant velocity (dx, dy)
    'ball_pos': {"x": 4, "y": 4, "dx": 1, "dy": -1}, 
    # ASCII icons
    'ball': "\U000026AA",                
    'block': "\U0001F532 \U0001F532 \U0001F532 \U0001F532",
    'paddle': "\U00002796\U00002796",
    'empty': " "
}

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    stdscr.clear()
    
    # Draw blocks
    for y in range(2): # Simple block top row
        for x in range(game_data['width']):
            stdscr.addstr(y, x*2, game_data['block'], curses.color_pair(1))

    # Draw player
    px, py = game_data['player']['x'], game_data['player']['y']
    stdscr.addstr(py, px, game_data['paddle'], curses.color_pair(1))
    
    # Draw ball
    bx, by = game_data['ball_pos']['x'], game_data['ball_pos']['y']
    stdscr.addstr(by, bx, game_data['ball'], curses.color_pair(1))
    
    stdscr.refresh()

def move_player(key):
    x = game_data['player']['x']
    if key == "a" and x > 0:
        game_data['player']['x'] -= 1
    elif key == "d" and x < game_data['width'] - 2:
        game_data['player']['x'] += 1

def move_ball():
    ball = game_data['ball_pos']
    
    # Move ball by constant velocity
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']
    
    # Simple Wall Bounce Logic
    if ball['x'] <= 0 or ball['x'] >= game_data['width'] - 1:
        ball['dx'] *= -1
    if ball['y'] <= 0 or ball['y'] >= game_data['height'] - 1:
        ball['dy'] *= -1

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None
            
        if key == "q":
            break
            
        if key in ["a", "d"]:
            move_player(key)
            
        move_ball()
        draw_board(stdscr)
        time.sleep(0.1) # Controlled speed

# Run the game
curses.wrapper(main)
