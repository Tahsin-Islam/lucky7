from random import shuffle
class Card:

    def __init__(self, suit, value):
        '''Constructor of Card class'''
        self.suit = suit
        self.value = value

    def __repr__(self):
        '''Representation of Card attributes'''
        return f"{self.value} of {self.suit}"

    def __eq__(self, other):
        '''Compares two card values'''
        return self.value == other.value

    def __gt__(self, other):
        '''Comparator method to check if card value is greater than other card value'''
        value_map = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
        return True if value_map[self.value] > value_map[other.value] else False

    def __lt__(self, other):
        '''Comparator method to check if the card value is less than other card value'''
        value_map = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,'K': 13}
        return True if value_map[self.value] < value_map[other.value] else False


class Deck:

    def __init__(self):
        '''Constructor of Deck class'''
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def __repr__(self):
        '''Representation of Deck attributes'''
        return f"Deck of {self.count()} cards."

    def __iter__(self):
        return iter(self.cards)

    def reset(self):
        '''Resets the Deck class'''
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        '''Return a list of cards dealt'''
        if self.count() == 0:
            raise ValueError("All cards have been dealt")

        actual = min([num, self.count()])  # make sure we don't try to over-deal

        if actual == 1:
            return self.cards.pop()

        cards = self.cards[-actual:]  # slice off the end
        self.cards = self.cards[:-actual]  # adjust cards

        return cards

    def shuffle(self):
        if self.count() < 52: #if not a full deck
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)

    def deal_card(self, number):
        '''Returns a single Card'''
        return self._deal(number)


if __name__ == "__main__":
    deck = Deck()
    deck.reset()
    for card in deck:
        print(card)

