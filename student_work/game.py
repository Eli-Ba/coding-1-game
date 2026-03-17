import curses
import time

# -- GAME DATA --
game_data = {
    'width': 10,
    'height': 10,
    'player': {"x": 4, "y": 9},
    'ball_pos': {"x": 4, "y": 4, "dx": 1, "dy": -1},
    'blocks': [(x, y) for y in range(2) for x in range(10)],
    'ball': "\U000026AA",
    'block': "\U0001F532",
    'paddle': "\U00002796\U00002796",
    'empty': " "
}

def draw_board(stdscr):
    stdscr.clear()
    
    # Draw blocks
    for (x, y) in game_data['blocks']:
        stdscr.addstr(y, x, game_data['block'])

    # Draw player
    px, py = game_data['player']['x'], game_data['player']['y']
    stdscr.addstr(py, px, game_data['paddle'])
    
    # Draw ball
    bx, by = game_data['ball_pos']['x'], game_data['ball_pos']['y']
    stdscr.addstr(by, bx, game_data['ball'])
    
    stdscr.refresh()

def move_player(key):
    x = game_data['player']['x']
    
    if key == "a" and x > 0:
        game_data['player']['x'] -= 1
    elif key == "d" and x < game_data['width'] - 2:
        game_data['player']['x'] += 1

def move_ball():
    ball = game_data['ball_pos']

    # --- tick counter for smooth diagonal ---
    if not hasattr(move_ball, "tick"):
        move_ball.tick = 0
    move_ball.tick += 1

    # Move horizontally every frame
    ball['x'] += ball['dx']

    # Move vertically every other frame (fixes aspect ratio)
    if move_ball.tick % 2 == 0:
        ball['y'] += ball['dy']

    # --- Wall collisions ---
    if ball['x'] <= 0 or ball['x'] >= game_data['width'] - 1:
        ball['dx'] *= -1
        ball['x'] += ball['dx']

    if ball['y'] <= 0:
        ball['dy'] *= -1
        ball['y'] += ball['dy']

    # --- Paddle collision ---
    px, py = game_data['player']['x'], game_data['player']['y']
    if ball['y'] == py - 1 and px <= ball['x'] <= px + 1:
        ball['dy'] *= -1
        ball['y'] += ball['dy']

    # --- Block collision ---
    hit_block = None
    for block in game_data['blocks']:
        if (ball['x'], ball['y']) == block:
            hit_block = block
            break

    if hit_block:
        game_data['blocks'].remove(hit_block)
        ball['dy'] *= -1
        ball['y'] += ball['dy']

    # --- Bottom collision ---
    if ball['y'] >= game_data['height'] - 1:
        ball['dy'] *= -1
        ball['y'] += ball['dy']

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    
    while True:
        try:
            key = stdscr.getkey()
        except curses.error:
            key = None
            
        if key == "q":
            break
            
        if key in ["a", "d"]:
            move_player(key)
            
        move_ball()
        draw_board(stdscr)
        time.sleep(0.1)
# Run the game
curses.wrapper(main)