import os.path

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')


def main() -> int:
    res = 0
    for line in open(input_file):
        left, right = line.rstrip('\n').split(',')
        ll, lr = left.split('-')
        rl, rr = right.split('-')
        if (int(lr) >= int(rl) and int(ll) <= int(rr)) or (int(rl) >= int(lr) and int(rr) <= int(ll)):
            # 5-7,7-9
            # 2-6,4-8
            # print(f'l: {left}, r: {right}')
            # print(f'll: {ll}, lr: {lr}, rl: {rl}, rr: {rr}, 1: {(ll >= rl and lr <= rr)}, 2: {(rl >= ll and rr <= lr)}')
            res += 1

    print(f'res: {res}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
