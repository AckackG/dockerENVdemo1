# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from os import environ
from time import sleep


def main():
    while True:
        # show all env k,v

        for k, v in environ.items():
            print(f'{k} = {v}\n')

        print('FOO: ', environ.get('FOO'))
        print('BAR: ', environ.get('BAR'))
        sleep(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
