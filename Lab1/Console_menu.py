import os


from Sorted_list import SortedList


def console_clear():
    os.system('cls')


def print_menu():
    print('MENU'.center(30))
    print('_' * 30)
    print(f'| {'1. Create first list':<26} |')
    print(f'| {'2. Create second list':<26} |')
    print(f'| {'3. Modify first list':<26} |')
    print(f'| {'4. Modify second list':<26} |')
    print(f'| {'5. Find the difference':<26} |')
    print(f'| {'6. Print menu':<26} |')
    print(f'| {'7. Exit':<26} |')
    print('_' * 30, end='\n\n')


def menu():
    list1, list2 = None, None
    exit_flag = False
    print_menu()
    while not exit_flag:
        choice = input('Your choice >>> ')
        match choice:
            case '1':
                list1 = SortedList()
                print('First list created\n')
            case '2':
                list2 = SortedList()
                print('Second list created\n')
            case '3':
                if list1:
                    console_clear()
                    list_menu(list1)
                else:
                    print('You have to create first list before modifying.\n')
            case '4':
                if list2:
                    console_clear()
                    list_menu(list2)
                else:
                    print('You have to create second list before modifying.\n')
            case '5':
                if list1 and list2:
                    list3 = list1 - list2
                    print('The difference of two lists is: ', end='')
                    list3.print()
                else:
                    print('You have to create both lists before finding the difference.\n')
            case '6':
                print_menu()
            case '7':
                exit_flag = True
            case _:
                print('Invalid input. Try again.\n')


def validation(value):
    try:
        int(value)
        return True
    except ValueError:
        print('Invalid input. Value must be an integer.\n')
        return False


def list_menu(lst):
    exit_flag = False
    print_list_menu()
    while not exit_flag:
        choice = input('Your choice >>> ')
        match choice:
            case '1':
                value = input('Enter value >>> ')
                if validation(value):
                    lst.add(int(value))
            case '2':
                index = input('Enter index >>> ')
                if validation(index):
                    lst.remove_by_index(int(index))
            case '3':
                value = input('Enter value >>> ')
                if validation(value):
                    lst.remove_by_value(int(value))
            case '4':
                lst.print()
            case '5':
                print_list_menu()
            case '6':
                exit_flag = True
                console_clear()
                print_menu()
            case _:
                print('Invalid input. Try again.\n')


def print_list_menu():
    print('SORTED LIST MENU'.center(30))
    print('_' * 30)
    print(f'| {'1. Add element':<26} |')
    print(f'| {'2. Remove element by index':<26} |')
    print(f'| {'3. Remove element by value':<26} |')
    print(f'| {'4. Print list':<26} |')
    print(f'| {'5. Print menu':<26} |')
    print(f'| {'6. Exit':<26} |')
    print('_' * 30, end='\n\n')


if __name__ == '__main__':
    menu()
