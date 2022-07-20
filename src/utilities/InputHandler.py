import tcod

STRING_TO_TILESET = {
    " ": 0,
    "#": 35,
    "$": 36,
    "%": 37,
    ".": 46,
    "/": 47,
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
    "╬": 206,
    "door": 206
}

TILESET_TO_STRING = {
    0: " ",
    35: "#",
    36: "$",
    37: "%",
    46: ".",
    47: "/",
    61: "=",
    64: "@",
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
    tcod.event.KeySym.RETURN: 500,
    tcod.event.KeySym.BACKSPACE: 501,
    tcod.event.KeySym.UP: 502,
    tcod.event.KeySym.RIGHT: 503,
    tcod.event.KeySym.DOWN: 504,
    tcod.event.KeySym.LEFT: 505,
    tcod.event.KeySym.ESCAPE: 509,
    # tileset mappings for ascii keyboard letters (Code Page 437)
    tcod.event.KeySym.SPACE: STRING_TO_TILESET[" "],
    tcod.event.KeySym.a: STRING_TO_TILESET["a"],
    tcod.event.KeySym.b: STRING_TO_TILESET["b"],
    tcod.event.KeySym.c: STRING_TO_TILESET["c"],
    tcod.event.KeySym.d: STRING_TO_TILESET["d"],
    tcod.event.KeySym.e: STRING_TO_TILESET["e"],
    tcod.event.KeySym.f: STRING_TO_TILESET["f"],
    tcod.event.KeySym.g: STRING_TO_TILESET["g"],
    tcod.event.KeySym.h: STRING_TO_TILESET["h"],
    tcod.event.KeySym.i: STRING_TO_TILESET["i"],
    tcod.event.KeySym.j: STRING_TO_TILESET["j"],
    tcod.event.KeySym.k: STRING_TO_TILESET["k"],
    tcod.event.KeySym.l: STRING_TO_TILESET["l"],
    tcod.event.KeySym.m: STRING_TO_TILESET["m"],
    tcod.event.KeySym.n: STRING_TO_TILESET["n"],
    tcod.event.KeySym.o: STRING_TO_TILESET["o"],
    tcod.event.KeySym.p: STRING_TO_TILESET["p"],
    tcod.event.KeySym.q: STRING_TO_TILESET["q"],
    tcod.event.KeySym.r: STRING_TO_TILESET["r"],
    tcod.event.KeySym.s: STRING_TO_TILESET["s"],
    tcod.event.KeySym.t: STRING_TO_TILESET["t"],
    tcod.event.KeySym.u: STRING_TO_TILESET["u"],
    tcod.event.KeySym.v: STRING_TO_TILESET["v"],
    tcod.event.KeySym.w: STRING_TO_TILESET["w"],
    tcod.event.KeySym.x: STRING_TO_TILESET["x"],
    tcod.event.KeySym.y: STRING_TO_TILESET["y"],
    tcod.event.KeySym.z: STRING_TO_TILESET["z"]
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
    if (passed_event in KEY_COMMANDS): # check if keyboard input is handled
        event = KEY_COMMANDS[passed_event]
        if (event == 500):
            if (console_active):
                CONSOLE.newLine()
            return 500
        elif (event == 501):
            if (console_active):
                CONSOLE.backspace()
            return 0
        elif (event == 502):
            return 1;
        elif (event == 503):
            return 2;
        elif (event == 504):
            return 3;
        elif (event == 505):
            return 4;
        elif (event == 509):
            return -1
        else:
            CONSOLE.set(event)
            return 0
    else: # ignore invalid keyboard input
        return 0