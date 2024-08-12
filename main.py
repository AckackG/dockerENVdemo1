from os import environ


def main():
    # show all env k,v
    print('-'*20)
    for k, v in environ.items():
        print(f'{k} = {v}\n')

    print('ENV_FILE_FOO: ', environ.get('ENV_FILE_FOO'))
    print('ENV_FILE_BAR: ', environ.get('ENV_FILE_BAR'))
    print('DOT_ENV_VARIABLE: ', environ.get('DOT_ENV_VARIABLE'))
    print('ENV_FROM_DOCKERFILE: ', environ.get('ENV_FROM_DOCKERFILE'))


if __name__ == '__main__':
    main()
