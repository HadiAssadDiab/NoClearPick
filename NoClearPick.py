from sys import stdout;from getkey import getkey, keys


def draw(options: list[str] = ["Hello", "World"], indicator: str = "*", selected: int = 0):
    spaces = " " * len(indicator)
    stdout.write("\033[?25l")
    toprint = ""
    for i, n in enumerate(options):
        toprint += " {0} {1}\n".format(indicator if selected == i else spaces, n)
    stdout.write(toprint)

def noclearpick(options: list = ["Hello", "World"], title: str = "Pick an option (use arrow keys to select and enter to pick):", indicator: str = "*", default_index: int = 0):
    """
    Creates a curses based interactive selection list in the terminal without clearing the terminal

    Usage::
    noclearpick(["Hello", "World"], "Pick the best word (use arrow keys to select the best word):", "=>", default_index = 0)
    """
    
    if not isinstance(indicator, str):
        raise TypeError("Indicator must be a string")
    
    if default_index < 0:
        raise ValueError("Default index must be greater than or equal to 0")
    
    stdout.write("{0}\n".format(str(title)))
    draw(options = options, indicator = indicator, selected = default_index)
    selected = default_index
    while 1:
        try:
            key = getkey()
            if key == keys.UP:
                selected -= 1
                if selected < 0:
                    selected = len(options) - 1
                stdout.write("\x1b[2K\x1b[1A" * len(options))
                draw(options = options, indicator = indicator, selected = selected)
            elif key == keys.DOWN:
                selected += 1
                if selected == len(options):
                    selected = 0
                stdout.write("\x1b[2K\x1b[1A" * len(options))
                draw(options = options, indicator = indicator, selected = selected)
            elif key == keys.ENTER:
                stdout.write("\033[?25h")
                return options[selected], selected
        except Exception as e:
            print(e)

        
if __name__ == "__main__":
    print("Returned:", noclearpick(
        options = ['"Lorem Ipsum is simply dummy text."', '"of the printing and typesetting industry."', '''"Lorem Ipsum has been the industry's"''', '"standard dummy text ever since the 1500s,"'],
        title = "Pick the best quote (use arrow keys to select and enter to pick):",
        indicator = "=>",
        default_index = 0
        ))