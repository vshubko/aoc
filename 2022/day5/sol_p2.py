import os.path
import re

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


def main() -> int:
    instructions = []
    crates = []
    for line in open(INPUT_FILE):
        line = line.rstrip('\n')
        if line.startswith('move '):
            instructions.append(line)
        elif line and not line.startswith(' 1 '):
            crates_amount = int((len(line) + 1) / 4)
            crates.append([line[i * 4 + 1] if line[i * 4 + 1] != ' ' else None for i in range(crates_amount)])
    # invert crates matrix (to have crates as an list element) and remove Nones
    crates = [[y for y in x if y is not None] for x in zip(*crates)]

    for ins in instructions:
        how_many, outof, to = re.findall(r"move (\d*) from (\d*) to (\d*)", ins)[0]
        crates[int(to) - 1] = list(crates[int(outof) - 1][0:int(how_many)]) + crates[int(to) - 1]
        del crates[int(outof) - 1][0:int(how_many)]
    print(f'res: {"".join([i[0] for i in crates])}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
