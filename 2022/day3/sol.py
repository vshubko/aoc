import string


def main():
    res = 0
    # prio starting from 1, therefore string begins from empty space
    alphabet = ' ' + string.ascii_lowercase + string.ascii_uppercase

    for line in open('./input.txt'):
        line = line.rstrip('\n')
        # print(int(len(line) / 2 - 1))
        middle = int(len(line) / 2)
        # split line on 2 parts
        left, right = line[0:middle], line[middle:len(line)]
        # find common charactes
        commonalities = set(left).intersection(set(right))
        res += alphabet.index(commonalities.pop())

    print(res)


if __name__ == '__main__':
    raise SystemExit(main())
