def main():
    res = [0]

    for line in open('./input.txt'):
        if line != '\n':
            res[-1] += int(line)
        else:
            res.append(0)

    return max(res)


if __name__ == '__main__':
    print(main())
    raise SystemExit(0)
