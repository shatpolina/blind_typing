import curses
import time
from curses import wrapper

from settings import Settings
from start_menu import StartMenu
from text_typing import TextRunner


def main(stdscr):
    Settings(True, stdscr)
    StartMenu(stdscr, curses).main()

    text = "The quick brown fox jumps over the lazy dog."
    # text = "Съешь ещё этих мягких французских булок, да выпей [же] чаю."
    TextRunner(stdscr, text).main()


wrapper(main)
