__author__ = 'howardau'


def countdown(n):
    print(n)
    if n > 0:
        return countdown(n - 1)


countdown(int(input('start countdown from: ')))
