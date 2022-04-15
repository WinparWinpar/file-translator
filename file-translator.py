#!/usr/bin/env python3

import os
from deep_translator import GoogleTranslator
import sys

def touch(filename):
    os.system(command=f'touch {filename}')

class Translator:
    def translate(source, lang, msg):
        return GoogleTranslator(source=source, target=lang).translate(msg)

def main(args: String[]):
    if not args[0].contains('.txt'):
        print(f'FileError: file {args[0]} not text file')
    try:
        touch(args[2])
    except:
        try:
            with open(args[0], 'r') as f:
                file = f.readlines()
                f.close()
        except:
            print(f'FileError: Cannot open file {args[0]}')
            sys.exit(1)

        try:
            with open(args[2], 'w') as f1:
                for line in file:
                    newline = Translator.translate('auto', args[1], line)
                    f1.write(newline)
                f1.close()
        except:
            print(f'FileError: Cannot open file {args[2]}')
            sys.exit(1)

    print('Translation Complete!')

if __name__ == '__main__':
    main(sys.argv)
