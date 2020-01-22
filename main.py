import guide as g

def main_page():
    while True:
        g.show_inst()
        _input = input('input: ')
        if _input == '1':
            print('start a new game')
        elif _input == '2':
            print('load savedata')
        elif _input == '3':
            print('game settings')
        elif _input == '4':
            exit()
        else:
            print('error input: ',_input)

if __name__ == '__main__':
    main_page()
