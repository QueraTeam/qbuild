class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def cprint(*args, sep=' ', end='\n', file=None, color=None):
    if color is not None:
        args = [color + str(i) + Color.END for i in args]
    print(*args, sep=sep, end=end, file=file)
