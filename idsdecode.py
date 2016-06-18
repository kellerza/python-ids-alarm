"""First go at decoding the IDS 1632 alarm bus.

requires pyserial
"""
import serial
from colorama import Fore, Back, Style, init
from collections import deque

COM = 'COM9'
HIGHLIGHT = deque([])


def hex_plus1(hex, ):
    hlb = (ord(hex[0]), ord(hex[1])+1)
    if hlb[1] > 15:
        hlb = (hlb[0]+1, 0)
    if hlb[0] > 15:
        hlb = (0, hlb[1])
    return chr(hlb[0]) + chr(hlb[1])

def seq(str):
    if str in HIGHLIGHT:
        return Fore.BLUE + str + Fore.RESET
    for hx0 in HIGHLIGHT:
        hx1 = hex_plus1(hx0)
        hx2 = hex_plus1(hx1)
        if str == hx1 or str == hx2:
            return Fore.CYAN + str + Fore.RESET
    return str

    
def printc(str, color=None, prepend=' '):
    """Print a character, optional color."""
    str = seq(str)
    if color:
        str = color + str + Fore.RESET
    print(prepend + str, end="", flush=True)


def c2hex(char):
    """Convert to HEX (2 bytes)."""
    return "{:02x}".format(ord(char))


def c2ascii(char):
    """Convert to ascii."""
    try:
        return char.decode('ascii')
    except UnicodeDecodeError:
        return None


def getparam(ser, p_name, p_data):
    """Decode a specific parameter from the serial port."""
    printc(Back.RED + p_name, prepend='\n')
    for typ in p_data:
        schr = ser.read()
        if typ == 'h':
            printc(c2hex(schr), Fore.GREEN)
        elif typ == 'H':
            if len(HIGHLIGHT):
                HIGHLIGHT.popleft()
            HIGHLIGHT.append(c2hex(schr))
            printc(c2hex(schr), Fore.BLUE)
        elif typ == 'a':
            printc(c2ascii(schr) or c2hex(schr), Fore.WHITE, prepend='')
        else:
            printc(c2hex(schr), Fore.WHITE)
    printc(Style.RESET_ALL, prepend='')


def main():
    init()
    ser = serial.Serial(COM, 19200)
    while True:
        schr = ser.read()
        char = c2ascii(schr)
        chx = c2hex(schr)
        if char == 'D':
            getparam(ser, 'D', 'Haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah')
            getparam(ser, '_', 'hhhhahhhhhHhhhhh')
        elif char == 'S':
            getparam(ser, 'S', 'Hhhhh')
            getparam(ser, '_', 'hhhhahhhhhHhhhhh')
        elif char == 'R':
            getparam(ser, 'R', 'hhhhh')
        elif char == 'C':
            getparam(ser, 'C', 'hhhhhhhhhh')
        elif char == 'B':
            getparam(ser, 'B', 'hhh')
        #elif char == 'Z':
        #    getparam(ser, 'Z', 'h')
        #elif char == 'W':
        #    getparam(ser, 'W', 'H')
        elif char and ('A' <= char and char <= 'Z' or
                     'a' <= char and char <= 'z'):
            printc(char, Fore.WHITE, prepend = '  ')
        else:
            printc(chx, Fore.YELLOW)

if __name__ == '__main__':
    main()