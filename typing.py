import random
char_list = []

def menu_start():
    global char_list
    print("\033[1;34mwelcome\nchoose one of the options below:\n \033") ## print welcome message
    print("[1;36m\t0.numbers\n\t1.signs\n\t2.both of them\n\t3.custom list\n\t4.exit\n") ## print menu options
    a = int(input())

    if a == 0:
        char_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    elif a == 1:
        char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+','`', '~', '[', ']', '{', '}', '|', ':', ';', '<', '>', ',', '.', '/', '?', '"', '\\', "'"]
    elif a == 2: 
        char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+','`', '~', '[', ']', '{', '}', '|', ':', ';', '<', '>', ',', '.', '/', '?', '"', '\\', "'", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    elif a == 3:
        print("type finish, if you don't want add new char")
        char_list = []
        while(True):
            b = input()
            if b == "finish":
                break
            char_list.append(b)
            print(char_list)
        print('\n\nyou chose ', char_list)
        print("\nfor back to menu, type 'finish'\n", '\033[0;0m')
    elif a == 4:
        exit()

menu_start()
rand_char = random.choice(char_list)

while(True):
    print(rand_char)
    data = input()
    if data == 'finish':
        menu_start()
    elif data == rand_char:
        print('\033[5;32m\u2713 \033[0;0m')
    else:
        print('\033[5;91mX \033[0;0m')
        continue
    rand_char = random.choice(char_list)