from settings import SettingsColors


class TextRunner:
    def __init__(self, stdscr, text, mistakes: bool):
        self.end_typing = False
        self.mistakes = mistakes = False
        self.mistakes_list = []
        self.taps = 0
        self.stdscr = stdscr
        self.text = text
        self.color = SettingsColors(stdscr)

    def main(self):
        while True:
            if not self.end_typing:
                self.stdscr.addstr(1, 1, "Press Crtl+C to stop")
                mistakes = self._text_runner()
                self.stdscr.clear()
            if self.end_typing:
                self.stdscr.addstr(20, 35, f"Количество ошибок: {len(self.mistakes_list)}", self.color.red_white)
                self.stdscr.addstr(20, 57, f"Количество попаданий: {self.taps - int(len(self.mistakes_list))}", self.color.green_white)
                self.stdscr.addstr(21, 80, f"Символов напечатано: {self.taps}")
                self.stdscr.refresh()

    def _text_runner(self):
        try:
            self.next = False
            for index, t in enumerate(self.text):
                self.stdscr.clear()
                self.next = False
                self.stdscr.addstr(20, 35, f"{self.text[:index]}", self.color.green_white)
                self.stdscr.addstr(21, 35 + index, f"{self.text[index:]}")
                self.stdscr.refresh()
                while not self.next:
                    t_input = self.stdscr.getkey()
                    if t_input:
                        self.taps += 1

                    if t_input == "^[":
                        self.stdscr.addstr(20, 35 + index, " ")
                        self.stdscr.refresh()

                    if t_input == t:
                        self.next = True

                    if t_input != t and t_input != "KEY_BACKSPACE":
                        if self.mistakes:
                            mistake = {index: t}
                            self.mistakes_list.append(mistake)
                            self.stdscr.addstr(20, 35 + index, f"{t_input}", self.color.red_white)
                            self.stdscr.refresh()
                        else:
                            self.mistakes_list.append(index)
                            self.stdscr.addstr(20, 35 + index, f"{t_input}", self.color.red_white)
                            self.stdscr.refresh()
                            self.next = True

                    if t_input == "KEY_BACKSPACE":
                        self.stdscr.addstr(20, 35 + index, " ")
                        self.stdscr.refresh()
                    # не работает
                    else:
                        self.stdscr.addstr(20, 35 + index, " ", self.color.red_black)
                        self.stdscr.refresh()
        finally:
            self.end_typing = True
            return self.mistakes_list
