import curses

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    height, width = 10, 20  # Map dimensions

    # Initial player position
    player_x, player_y = 1, 1

    # Create a simple static map
    game_map = [
        "####################",
        "#.................G#",
        "#........###########",
        "#........#.........#",
        "#........#.........#",
        "#........#.........#",
        "#........###########",
        "#..................#",
        "#..................#",
        "####################"
    ]

    key = None

    # Main game loop
    while key != ord('q'):  # Press 'q' to quit
        stdscr.clear()

        # Draw the map
        for y, row in enumerate(game_map):
            stdscr.addstr(y, 0, row)

        # Draw the player
        stdscr.addch(player_y, player_x, '@')

        # Get user input
        key = stdscr.getch()

        # Handle player movement
        new_x, new_y = player_x, player_y
        if key == curses.KEY_UP:
            new_y -= 1
        elif key == curses.KEY_DOWN:
            new_y += 1
        elif key == curses.KEY_LEFT:
            new_x -= 1
        elif key == curses.KEY_RIGHT:
            new_x += 1

        # Prevent moving into walls or out of bounds
        if game_map[new_y][new_x] != '#':
            player_x, player_y = new_x, new_y

        # Check win condition
        if game_map[player_y][player_x] == 'G':
            stdscr.addstr(height // 2, width // 2 - 7, "You Win! Press 'q' to quit.")
            stdscr.refresh()
            key = stdscr.getch()  # Wait for player to quit

    stdscr.clear()
    stdscr.addstr(0, 0, "Thanks for playing!")
    stdscr.refresh()
    stdscr.getch()

# Start the game
curses.wrapper(main)
