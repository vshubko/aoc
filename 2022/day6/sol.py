import os.path

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
UNIQUE_CHR_LENGTH = 4


def main() -> int:
    with open(INPUT_FILE) as f:
        for line in f:
            for i in range(len(line) - UNIQUE_CHR_LENGTH):
                if len(set(line[i:(i+UNIQUE_CHR_LENGTH)])) == UNIQUE_CHR_LENGTH:
                    print(f'res: {i + UNIQUE_CHR_LENGTH}')
                    break
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
