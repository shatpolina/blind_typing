import curses
import time
from curses import wrapper


def logo(stdscr):
    stdscr.addstr(5, 55, "~* Blind typing", curses.color_pair(1))
    stdscr.addstr(5, 69, "h", curses.color_pair(2))
    stdscr.addstr(5, 70, "|", curses.A_BLINK)
    stdscr.addstr(6, 69, "g")
    stdscr.addstr(6, 72, "trainer *~")


def start_menu(stdscr):
    logo(stdscr)
    stdscr.addstr(20, 55, "Press Enter to start")


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
    curses.use_default_colors()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)

    black_green = curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    black_red = curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    black_white = curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_menu(stdscr)

    while True:
        key = stdscr.getkey()
        print(key)
        if key == "\n":
            break

    stdscr.clear()
    stdscr.refresh()

    while True:
        stdscr.clear()
        stdscr.addstr(1, 1, "Press Enter to stop")
        text_runner(stdscr)
        stdscr.refresh()


wrapper(main)

