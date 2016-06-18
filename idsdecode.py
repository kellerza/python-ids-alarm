"""First go at decoding the IDS 1632 alarm bus.

requires pyserial
"""
import serial
from colorama import Fore, Back, init

COM = 'COM9'


def printc(str, color=None):
    """Print a character, optional color."""
    if color:
        str = color + str + Fore.RESET
    print(str, end="", flush=True)


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
    printc('\n' + Back.RED + p_name)
    for typ in p_data:
        schr = ser.read()
        if typ == 'h':
            printc(' ' + c2hex(schr), Fore.GREEN)
        elif typ == 'H':
            printc(' ' + c2hex(schr), Fore.BLUE)
        elif typ == 'a':
            printc(c2ascii(schr) or c2hex(schr), Fore.YELLOW)
        else:
            printc(c2hex(schr), Fore.WHITE)
    printc(Back.RESET)


def main():
    init()
    ser = serial.Serial(COM, 19200)
    while True:
        schr = ser.read()
        char = c2ascii(schr)
        chx = c2hex(schr)
        if char == 'D':
            getparam(ser, 'D', 'Haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        elif char == 'B':
            getparam(ser, 'B', 'h')
        elif char == 'Z':
            getparam(ser, 'Z', 'h')
        elif char == 'W':
            getparam(ser, 'W', 'H')
        elif char and ('A' <= char and char <= 'Z' or
                     'a' <= char and char <= 'z'):
            printc('  ' + char, Fore.WHITE)
        else:
            printc(' ' + chx, Fore.YELLOW)

if __name__ == '__main__':
    main()