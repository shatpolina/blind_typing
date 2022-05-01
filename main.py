import curses
from curses import wrapper

def logo(stdscr):
    stdscr.addstr(5, 55, "~* Blind typing", curses.color_pair(1))
    stdscr.addstr(5, 69, "h", curses.color_pair(2))
    stdscr.addstr(5, 70, "|", curses.A_BLINK)
    stdscr.addstr(6, 69, "g")
    stdscr.addstr(6, 72, "trainer *~")


def text_runner(stdscr):
    text = "Съешь ещё этих мягких французских булок, да выпей [же] чаю."
    for index, t in enumerate(text):
        t_input = "ы"
        stdscr.addstr(20, 35, f"{text[:index]}", curses.color_pair(1))
        stdscr.addstr(21, int(35 + 23), f"{text[23:]}")
        if index == 23:
            stdscr.addstr(20, 35 + index, f"{t_input}", curses.color_pair(2))

            break


def main(stdscr):
    curses.use_default_colors()
    black_green = curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    black_red = curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    black_white = curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.clear()
    logo(stdscr)
    text_runner(stdscr)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)

