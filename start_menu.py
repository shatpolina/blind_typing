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
        learning_text = "Press Enter to start learning"
        training_text = "Press Backspace to start training"
        self.stdscr.addstr(20, 55, learning_text)
        self.stdscr.addstr(21, 55 + len(learning_text), training_text)
        while True:
            key = self.stdscr.getkey()
            if key == "\n":
                self.stdscr.clear()
                self.stdscr.refresh()
                break
            if key == " ":
                self.stdscr.clear()
                self.stdscr.refresh()
