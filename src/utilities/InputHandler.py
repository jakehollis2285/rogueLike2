import tcod
import Globals as Globals

STRING_TO_TILESET = {
    " ": 0,
    "#": 35,
    "$": 36,
    "%": 37,
    ",": 44,
    ".": 46,
    "/": 47,
    "0": 48,
    "1": 49,
    "2": 50,
    "3": 51,
    "4": 52,
    "5": 53,
    "6": 54,
    "7": 55,
    "8": 56,
    "9": 57,
    ":": 58,
    "=": 61,
    "@": 64,
    "[": 91,
    "\\": 92,
    "]": 93,
    "_": 95,
    "a": 97,
    "b": 98,
    "c": 99,
    "d": 100,
    "e": 101,
    "f": 102,
    "g": 103,
    "h": 104,
    "i": 105,
    "j": 106,
    "k": 107,
    "l": 108,
    "m": 109,
    "n": 110,
    "o": 111,
    "p": 112,
    "q": 113,
    "r": 114,
    "s": 115,
    "t": 116,
    "u": 117,
    "v": 118,
    "w": 119,
    "x": 120,
    "y": 121,
    "z": 122,
    "{": 123,
    "|": 124,
    "}": 125,
    "╣": 185,
    "║": 186,
    "╗": 187,
    "╝": 188,
    "╚": 200,
    "╔": 201,
    "╩": 202,
    "╦": 203,
    "╠": 204,
    "═": 205
}

TILESET_TO_STRING = {
    0: " ",
    32: " ",
    35: "#",
    36: "$",
    37: "%",
    46: ".",
    47: "/",
    61: "=",
    64: "@",
    65: "A",
    66: "B",
    67: "C",
    68: "D",
    69: "E",
    70: "F",
    71: "G",
    72: "H",
    73: "I",
    74: "J",
    75: "K",
    76: "L",
    77: "M",
    78: "N",
    79: "O",
    80: "P",
    81: "Q",
    82: "R",
    83: "S",
    84: "T",
    85: "U",
    86: "V",
    87: "W",
    88: "X",
    89: "Y",
    90: "Z",
    91: "[",
    92: "\\",
    93: "]",
    95: "_",
    97: "a",
    98: "b",
    99: "c",
    100: "d",
    101: "e",
    102: "f",
    103: "g",
    104: "h",
    105: "i",
    106: "j",
    107: "k",
    108: "l",
    109: "m",
    110: "n",
    111: "o",
    112: "p",
    113: "q",
    114: "r",
    115: "s",
    116: "t",
    117: "u",
    118: "v",
    119: "w",
    120: "x",
    121: "y",
    122: "z",
    123: "[",
    124: "|",
    125: "]",
    206: "╬"
}

KEY_COMMANDS = {
    # special character mappings (custom use values > 256 to avoid conflict with tileset)
    tcod.event.KeySym.RETURN: 50000,
    tcod.event.KeySym.BACKSPACE: 50001,
    tcod.event.KeySym.UP: 50002,
    tcod.event.KeySym.RIGHT: 50003,
    tcod.event.KeySym.DOWN: 50004,
    tcod.event.KeySym.LEFT: 50005,
    tcod.event.KeySym.ESCAPE: 50009,
    # tileset mappings for ascii keyboard letters (Code Page 437)
    tcod.event.KeySym.SPACE: ord(" "),
    tcod.event.KeySym.a: ord("a"),
    tcod.event.KeySym.b: ord("b"),
    tcod.event.KeySym.c: ord("c"),
    tcod.event.KeySym.d: ord("d"),
    tcod.event.KeySym.e: ord("e"),
    tcod.event.KeySym.f: ord("f"),
    tcod.event.KeySym.g: ord("g"),
    tcod.event.KeySym.h: ord("h"),
    tcod.event.KeySym.i: ord("i"),
    tcod.event.KeySym.j: ord("j"),
    tcod.event.KeySym.k: ord("k"),
    tcod.event.KeySym.l: ord("l"),
    tcod.event.KeySym.m: ord("m"),
    tcod.event.KeySym.n: ord("n"),
    tcod.event.KeySym.o: ord("o"),
    tcod.event.KeySym.p: ord("p"),
    tcod.event.KeySym.q: ord("q"),
    tcod.event.KeySym.r: ord("r"),
    tcod.event.KeySym.s: ord("s"),
    tcod.event.KeySym.t: ord("t"),
    tcod.event.KeySym.u: ord("u"),
    tcod.event.KeySym.v: ord("v"),
    tcod.event.KeySym.w: ord("w"),
    tcod.event.KeySym.x: ord("x"),
    tcod.event.KeySym.y: ord("y"),
    tcod.event.KeySym.z: ord("z")
}

def handleKeyboardInput(passed_event, CONSOLE, console_active=True) -> int:
    '''
    # this function checks for valid character input and then sets the value in the Console
    # -1 -- exit
    # 0 -- no op
    # 1 -- up arrow
    # 2 -- right arrow
    # 3 -- down arrow
    # 4 -- left arrow
    '''
    op = 0
    if (passed_event.sym in KEY_COMMANDS): # check if keyboard input is handled
        event = KEY_COMMANDS[passed_event.sym]
        # capture capital letters using shift key input
        if (passed_event.mod and tcod.event.Modifier.SHIFT and (event >= 97 and event <= 122)):
            event -= 32
        if (event == 50000):
            if (console_active):
                CONSOLE.newLine()
            op = 50000
        elif (event == 50001):
            if (console_active):
                CONSOLE.backspace()
            op = 0
        elif (event == 50002):
            op = 1;
        elif (event == 50003):
            op = 2;
        elif (event == 50004):
            op = 3;
        elif (event == 50005):
            op = 4;
        elif (event == 50009):
            op = -1
        else:
            CONSOLE.set(event)
            op = 0

    # handle exit (on user input)
    if(op < 0):
        raise SystemExit()
    # player movement operators
    elif(op > 0 and op < 5):
        Globals.GRID.move(Globals.GRID.PLAYER, op)

    return op
