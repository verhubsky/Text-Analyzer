import sys

from utils import startup

if __name__ == '__main__':
    try:
        line = "-" * 23
        print(line)
        print('| Text-Analyzer v0.2  |')
        print(line)

        words = input("Enter words, for ex. 'I love cookies'\n>>> ")
        startup(words)
    except KeyboardInterrupt:
        print('\nBye!')
        sys.exit()
