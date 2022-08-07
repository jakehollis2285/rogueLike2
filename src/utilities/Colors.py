import tcod

class ANSIColors:
    black = '\033[30m{0}\033[00m'
    red = '\033[31m{0}\033[00m'
    green = '\033[32m{0}\033[00m'
    orange = '\033[33m{0}\033[00m'
    blue = '\033[34m{0}\033[00m'
    purple = '\033[35m{0}\033[00m'
    cyan = '\033[36m{0}\033[00m'
    lightgrey = '\033[37m{0}\033[00m'
    darkgrey = '\033[90m{0}\033[00m'
    lightred = '\033[91m{0}\033[00m'
    lightgreen = '\033[92m{0}\033[00m'
    yellow = '\033[93m{0}\033[00m'
    lightblue = '\033[94m{0}\033[00m'
    pink = '\033[95m{}\033[00m'
    lightcyan = '\033[96m{0}\033[00m'

def colored(r, g, b, text):
    ''' color formated tcod string '''
    return f"{tcod.COLCTRL_FORE_RGB:c}{r:c}{g:c}{b:c}{text}"