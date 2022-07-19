import tcod

KEY_COMMANDS = {
    tcod.event.KeySym.RETURN: 0,
    tcod.event.KeySym.q: 1,
    tcod.event.KeySym.w: 2,
    tcod.event.KeySym.e: 3,
    tcod.event.KeySym.r: 4,
    tcod.event.KeySym.t: 5,
    tcod.event.KeySym.y: 6,
    tcod.event.KeySym.u: 7,
    tcod.event.KeySym.i: 8,
    tcod.event.KeySym.o: 9,
    tcod.event.KeySym.p: 10,
    tcod.event.KeySym.a: 11,
    tcod.event.KeySym.s: 12,
    tcod.event.KeySym.d: 13,
    tcod.event.KeySym.f: 14,
    tcod.event.KeySym.g: 15,
    tcod.event.KeySym.h: 16,
    tcod.event.KeySym.j: 17,
    tcod.event.KeySym.k: 18,
    tcod.event.KeySym.l: 19,
    tcod.event.KeySym.z: 20,
    tcod.event.KeySym.x: 21,
    tcod.event.KeySym.c: 22,
    tcod.event.KeySym.v: 23,
    tcod.event.KeySym.b: 24,
    tcod.event.KeySym.n: 25,
    tcod.event.KeySym.m: 26
}

def handleInput(passed_event, console, CONSOLE) -> None:
    event = KEY_COMMANDS[passed_event]
    if (event == 0) :
        CONSOLE.newLine()
    elif (event == 1):
        # q
        CONSOLE.set(113)
    elif (event == 2):
        # w
        CONSOLE.set(119)
    elif (event == 3):
        # e
        CONSOLE.set(101)
    elif (event == 4):
        # r
        CONSOLE.set(114)
    elif (event == 5):
        # t
        CONSOLE.set(116)
    elif (event == 6):
        # y
        CONSOLE.set(121)
    elif (event == 7):
        # u
        CONSOLE.set(117)
    elif (event == 8):
        # i
        CONSOLE.set(105)
    elif (event == 9):
        # o
        CONSOLE.set(111)
    elif (event == 10):
        # p
        CONSOLE.set(112)
    elif (event == 11):
        # a
        CONSOLE.set(97)
    elif (event == 12):
        # s
        CONSOLE.set(115)
    elif (event == 13):
        # d
        CONSOLE.set(100)
    elif (event == 14):
        # f
        CONSOLE.set(102)
    elif (event == 15):
        # g
        CONSOLE.set(103)
    elif (event == 16):
        # h
        CONSOLE.set(104)
    elif (event == 17):
        # j
        CONSOLE.set(106)
    elif (event == 18):
        # k
        CONSOLE.set(107)
    elif (event == 19):
        # l
        CONSOLE.set(108)
    elif (event == 20):
        # z
        CONSOLE.set(122)
    elif (event == 21):
        # x
        CONSOLE.set(120)
    elif (event == 22):
        # c
        CONSOLE.set(99)
    elif (event == 23):
        # v
        CONSOLE.set(118)
    elif (event == 24):
        # b
        CONSOLE.set(98)
    elif (event == 25):
        # n
        CONSOLE.set(110)
    elif (event == 26):
        # m
        CONSOLE.set(109)