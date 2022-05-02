class StartMenu:
    def __init__(self, stdsrc, curses):
        self.stdscr = stdsrc
        self.curses = curses

    def main(self):
        self._logo()
        self._start()

    def _logo(self):
        self.stdscr.addstr(5, 55, "~* Blind typing", self.curses.color_pair(1))
        self.stdscr.addstr(5, 69, "h", self.curses.color_pair(2))
        self.stdscr.addstr(5, 70, "|", self.curses.A_BLINK)
        self.stdscr.addstr(6, 69, "g")
        self.stdscr.addstr(6, 72, "trainer *~")

    def _start(self):
        self.stdscr.addstr(20, 55, "Press Enter to start")
        while True:
            key = self.stdscr.getkey()
            if key == "\n":
                self.stdscr.clear()
                self.stdscr.refresh()
                break
