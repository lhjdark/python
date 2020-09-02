import os, sys


def lister(root):
    for (dirname, sub, files) in os.walk(root):
        print('[' + dirname + ']')
        for fname in files:
            path = os.path.join(dirname, fname)
            print(path)


if __name__ == '__main__':
    lister(sys.argv[1])