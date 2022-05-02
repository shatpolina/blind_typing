import curses


class SettingsColors:
    def __init__(self, stdsrc):
        self.green_white = curses.color_pair(1)
        self.red_white = curses.color_pair(2)
        self.white_black = curses.color_pair(3)
        self.black_red = curses.color_pair(4)
        self.red_black = curses.color_pair(5)


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
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)

    def deactivating(self):
        pass
