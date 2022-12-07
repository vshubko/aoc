import string


def main():
    res = 0
    buffer = []
    # prio starting from 1, therefore string begins from empty space
    alphabet = ' ' + string.ascii_lowercase + string.ascii_uppercase

    with open('./input.txt') as infile:
        for line in infile:
            if len(buffer) < 2:
                buffer.append(line.rstrip('\n'))
                continue

            print(*buffer, line)
            commonalities = set(line).intersection(*buffer)
            print(commonalities)
            res += alphabet.index(commonalities.pop())
            buffer = []

    print(res)

if __name__ == '__main__':
    raise SystemExit(main())
