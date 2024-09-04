from os import environ
from time import sleep

def main():
    while True:
    # show all env k,v
        print('-'*20)
        for k, v in environ.items():
            print(f'{k} = {v}\n')

        print('ENV_FILE_FOO: ', environ.get('ENV_FILE_FOO'))
        print('ENV_FILE_BAR: ', environ.get('ENV_FILE_BAR'))
        print('DOT_ENV_VARIABLE: ', environ.get('DOT_ENV_VARIABLE'))
        print('DOT_ENV_VARIABLE2: ', environ.get('DOT_ENV_VARIABLE2'))
        print('ENV_FROM_DOCKERFILE: ', environ.get('ENV_FROM_DOCKERFILE'))
        print('ENV_FROM_DOCKERFILE_2: ', environ.get('ENV_FROM_DOCKERFILE_2'))

        sleep(10)

if __name__ == '__main__':
    main()
