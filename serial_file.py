"""Serial port to file.

requires pyserial
"""
import serial
COM = 'COM9'
FNAME = 'output/output.dat'


def main():
    ser = serial.Serial(COM, 19200)
    with open(FNAME, 'xb') as outf:
        while True:
            schr = ser.read()
            outf.write(schr)

if __name__ == '__main__':
    main()