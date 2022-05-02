import curses


class Settings:
    def __init__(self, activated: bool, stdsrc):
        self.stdscr = stdsrc
        self.name: str
        self.activated: bool = activated
        if self.activated:
            self.activating()
        else:
            self.deactivating()

    def activating(self):
        curses.use_default_colors()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(True)

        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def deactivating(self):
        pass
