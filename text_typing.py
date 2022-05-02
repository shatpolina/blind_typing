from settings import SettingsColors


class TextRunner:
    def __init__(self, stdscr, text, mistakes: bool):
        self.end_typing = False
        self.mistakes = mistakes
        self.mistakes_dict = {}
        self.taps = 0
        self.stdscr = stdscr
        self.text = text
        self.color = SettingsColors(stdscr)

    def main(self):
        while not self.end_typing:
            # TODO: add timer
            self.stdscr.addstr(1, 1, "Press Crtl+C to stop")
            self._text_runner()
            self.stdscr.clear()

        self._get_statisctic()

        while True:
            input = self.stdscr.getkey()
            if input == "\n" or input == "^[":  # only Enter worked
                break

    def _text_runner(self):
        try:
            self.next = False
            for index, t in enumerate(self.text):
                self.stdscr.clear()
                self.next = False

                self.stdscr.addstr(20, 35, f"{self.text[:index]}", self.color.green_white)
                if self.mistakes:
                    for mistake_index, old_mistake in self.mistakes_dict.items():
                        self.stdscr.addstr(20, 35 + mistake_index, f"{old_mistake}", self.color.red_white)
                self.stdscr.addstr(21, 35 + index, f"{self.text[index:]}")
                self.stdscr.refresh()
                n = 0
                while not self.next:
                    t_input = self.stdscr.getkey()
                    if t_input == "^[":
                        self.stdscr.addstr(20, 35 + index, " ")
                        self.stdscr.refresh()

                    if t_input:
                        self.taps += 1

                    if t_input == t:
                        self.next = True

                    if t_input == "KEY_BACKSPACE":
                        self.stdscr.addstr(20, 35 + index, " ")
                        self.stdscr.refresh()
                        pass

                    if t_input != t and t_input != "KEY_BACKSPACE":
                        mistake = {index: t_input}
                        self.mistakes_dict.update(mistake)
                        self.stdscr.addstr(20, 35 + index, f"{t_input}", self.color.red_white)
                        self.stdscr.refresh()
                        if self.mistakes:
                            self.next = True
                    else:
                        self.stdscr.addstr(20, 35 + index, " ", self.color.red_black)
                        self.stdscr.refresh()
        finally:
            self.end_typing = True

    def _get_statisctic(self):
        n_valid = f"Количество попаданий: {self.taps - int(len(self.mistakes_dict))}"
        n_errors = f"Количество ошибок: {len(self.mistakes_dict)}"
        n_taps = f"Количество нажатий: {self.taps}"
        n_text_score = f"Напечатано текста: %"

        self.stdscr.addstr(20, 25, n_valid, self.color.green_white)
        self.stdscr.addstr(20, 25 + 1 + len(n_valid), n_errors, self.color.red_white)
        self.stdscr.addstr(21, 25 + 2 + len(n_valid) + len(n_errors), n_taps)
        self.stdscr.addstr(21, 25 + 3 + len(n_valid) + len(n_errors) + len(n_taps), n_text_score)
        self.stdscr.refresh()
