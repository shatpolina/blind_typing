from settings import SettingsColors


class TextRunner:
    def __init__(self, stdscr, text):
        self.stdscr = stdscr
        self.text = text
        self.color = SettingsColors(stdscr)

    def main(self):
        while True:
            self.stdscr.clear()
            self.stdscr.addstr(1, 1, "Press Crtl+C to stop")
            self._text_runner()
            self.stdscr.refresh()

    def _text_runner(self):
        self.next = False
        for index, t in enumerate(self.text):
            self.stdscr.clear()
            self.next = False
            self.stdscr.addstr(20, 35, f"{self.text[:index]}", self.color.black_green)
            self.stdscr.addstr(21, 35 + index, f"{self.text[index:]}")
            self.stdscr.refresh()
            while not next:
                t_input = self.stdscr.getkey()
                if t_input == t:
                    self.next = True
                elif t_input != t and t_input != "KEY_BACKSPACE":
                    self.stdscr.addstr(20, 35 + index, f"{t_input}", self.color.black_red)
                    self.stdscr.refresh()
                elif t_input == "KEY_BACKSPACE":
                    self.stdscr.addstr(20, 35 + index, " ", self.color.black_green)
                    self.stdscr.refresh()
                elif t_input == "\n":
                    self.stdscr.clear()
                    self.stdscr.refresh()
                    exit()
                else:
                    pass
