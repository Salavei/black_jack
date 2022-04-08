import random


class Card(object):
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def get_value(self) -> int:
        if self.rank in 'ТВДК':
            return 10
        else:
            return ' A23456789'.index(self.rank)

    def get_rank(self) -> str:
        return 'suit: {} rank: {}'.format(self.suit, self.rank)


class DeskCard(object):
    def __init__(self) -> None:
        _rank = 'A23456789ТВДК'
        _suit = '♠♦♥♣'
        self.__cards = [Card(rank=r, suit=s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)

    def get_card(self) -> Card:
        return self.__cards.pop()


class Player(object):
    def __init__(self, name: str) -> None:
        self._hand = []
        self.count = 0
        self.name = name

    @property
    def hand(self) -> str:
        return 'Карты в руке: {}; Очков - {}'.format(self._hand, self.count)

    @hand.setter
    def hand(self, card: Card) -> None:
        self.count += card.get_value()
        self._hand.append(card.get_rank())


class Dealer(Player):
    # def get_cards(self, cards: DeskCard):
    #     while self.count < 18:
    #         self.hand = cards.get_card()
    def get_cards(self, cards: DeskCard):
        while self.count < 21:
            _card = cards.get_card()
            if _card.get_value() + self.count <= 21:
                self.hand = _card
            else:
                break


class Game(object):
    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name='Dealer')

    def print(self) -> str:
        return '\n{}:\n{}\n{}:\n{}'.format(self.player.name, self.player.hand, self.dealer.name, self.dealer.hand)

    def check_count(self):
        if self.player.count > 21:
            print('\nYou Loose', self.print())
        elif self.dealer.count > 21 and self.player.count <= 21:
            print('\nYou Win', self.print())
        elif self.dealer.count == self.player.count:
            print('\nDead Heat', self.print())
        elif self.dealer.count > self.player.count:
            print('\nYou Loose', self.print())
        elif self.dealer.count < self.player.count:
            print('\nYou Win', self.print())

    def start(self):
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()
        print(self.player.hand)

        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        while self.player.count < 21:
            answer = input('Карту? y/n ')
            if answer == 'y':
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer == 'n':
                self.dealer.get_cards(self.cards)
                break
        self.check_count()


def main() -> None:
    name = input('Введите Ваше имя: ')
    game = Game(player_name=name)
    game.start()


if __name__ == '__main__':
    main()
