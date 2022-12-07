OPP_MAPP = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
}
OWN_MAPP = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
}


class RPCGame:
    def __init__(self, opp: str, own: str) -> None:
        self.opp = opp
        self.own = own

    def total_score(self) -> int:
        return self.card_score() + self.winner_score()

    def card_score(self) -> int:
        if self.own == 'Rock':
            return 1
        if self.own == 'Paper':
            return 2
        if self.own == 'Scissors':
            return 3

    def winner_score(self) -> int:
        if self.own == 'Rock':
            if self.opp == 'Scissors':
                return 6
            elif self.opp == 'Paper':
                return 0
        if self.own == 'Paper':
            if self.opp == 'Rock':
                return 6
            elif self.opp == 'Scissors':
                return 0
        if self.own == 'Scissors':
            if self.opp == 'Paper':
                return 6
            elif self.opp == 'Rock':
                return 0
        return 3


def main():
    res = 0
    for line in open('./input.txt'):
        opp_choise, own_choise = line.rstrip('\n').split(' ')
        res += RPCGame(OPP_MAPP[opp_choise], OWN_MAPP[own_choise]).total_score()
    print(f'res: {res}')


if __name__ == '__main__':
    raise SystemExit(main())
