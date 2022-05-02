import curses
import time
from curses import wrapper

from settings import Settings
from start_menu import StartMenu


def text_runner(stdscr):
    # text = "Съешь ещё этих мягких французских булок, да выпей [же] чаю."
    text = "The quick brown fox jumps over the lazy dog."
    next = False
    for index, t in enumerate(text):
        stdscr.clear()
        next = False
        stdscr.addstr(20, 35, f"{text[:index]}", curses.color_pair(1))
        stdscr.addstr(21, 35 + index, f"{text[index:]}")
        stdscr.refresh()
        while not next:
            t_input = stdscr.getkey()
            if t_input == t:
                next = True
            elif t_input != t and t_input != "KEY_BACKSPACE":
                    stdscr.addstr(20, 35 + index, f"{t_input}", curses.color_pair(2))
                    stdscr.refresh()
            elif t_input == "KEY_BACKSPACE":
                stdscr.addstr(20, 35 + index, " ", curses.color_pair(1))
                stdscr.refresh()
            elif t_input == "\n":
                stdscr.clear()
                stdscr.refresh()
                exit()
            else:
                pass


def main(stdscr):
    Settings(True, stdscr)

    black_green = curses.color_pair(1)
    black_red = curses.color_pair(2)
    black_white = curses.color_pair(3)

    StartMenu(stdscr, curses).main()

    while True:
        stdscr.clear()
        stdscr.addstr(1, 1, "Press Enter to stop")
        text_runner(stdscr)
        stdscr.refresh()


wrapper(main)

