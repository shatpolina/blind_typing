import curses
from curses import wrapper

from settings import Settings
from start_menu import StartMenu
from text_typing import TextRunner


def main(stdscr):
    Settings(True, stdscr)
    StartMenu(stdscr, curses).main()

    text = "The quick brown fox jumps over the lazy dog."
    TextRunner(stdscr, text).main()


wrapper(main)
