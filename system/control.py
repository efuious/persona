import os

def press():
    _input = input('press a button')
    return 0

def clrscr():
    os.system('cls')

if __name__ == '__main__':
    clrscr()
    press()