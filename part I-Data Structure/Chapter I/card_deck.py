### it demonstrates the power of implementing just two spe‐ cial methods, __getitem__ and __len__.
### Example 1-1. A deck as a sequence of playing cards

import collections 
# We use namedtuple to build classes of objects that are just bundles of attributes with no custom methods

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchCard:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self.cards = [Card(rank,suit) for rank in self.ranks
                                      for suit in self.suits]
    
    def __len__(self):

        return len(self.cards)

    def __getitem__(self,position):

        return(self.cards[position])

class FrenchCard_change:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank,suit) for rank in self.ranks
                                      for suit in self.suits]
    
    def __len__(self):

        return len(self.cards)

beer_card = Card('7','diamonds')
print(beer_card)

deck = FrenchCard()
deck_2 = FrenchCard_change()
# print(len(deck))

# print(deck[0])

from random import choice
## if not set getitem special method we can not use choice
# print('from random')
# print(choice(deck))

# print(deck[:4])

# for card in deck:

#     print(card)

# for card in reversed(deck):
#     print(card)

print(beer_card in deck)

#### sorting
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
# print(suit_value)

# print(deck.ranks.index("7"))

def spades_high(card:Card):

    rank_value = FrenchCard.ranks.index(card.rank)

    return rank_value * len(suit_value) + suit_value[card.suit]

for card in sorted(deck,key=spades_high):

    print(card)


