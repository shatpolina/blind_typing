import curses
from curses import wrapper

from settings import Settings
from start_menu import StartMenu


def main(stdscr):
    Settings(True, stdscr)
    StartMenu(stdscr, curses).main()


wrapper(main)
