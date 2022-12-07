import os.path

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')


def main() -> int:
    res = 0
    for line in open(input_file):
        left, right = line.rstrip('\n').split(',')
        ll, lr = left.split('-')
        rl, rr = right.split('-')
        if (int(ll) >= int(rl) and int(lr) <= int(rr)) or (int(rl) >= int(ll) and int(rr) <= int(lr)):
            res += 1

    print(f'res: {res}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
