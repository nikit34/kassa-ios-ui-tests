#!/usr/bin/python3
import os
import sys
from time import sleep
from pynput.keyboard import Key, Controller


if __name__ == '__main__':
    if len(sys.argv) == 2:
        os.system("osascript -e 'activate application \"Simulator.app\"'")
        sleep(2)

        keyboard = Controller()
        keyboard.press(Key.cmd)

        if sys.argv[1] == 'right':
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        elif sys.argv[1] == 'left':
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        else:
            raise ValueError('[ERROR] invalid argument')

        keyboard.release(Key.cmd)
    else:
        raise IndexError('[ERROR] only one argument')
