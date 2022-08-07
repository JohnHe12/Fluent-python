import collections

Card = collections.namedtuple('Card',['rank','suit'])


class FrenchDeck:
    k ="k"
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self.cards = [Card(rank,suit) for rank in self.ranks 
                                      for suit in self.suits]
    
    def __len__(self):

        return len(self.cards)

    def __getitem__(self,position):

        return self.cards[position]
    
    def __setattr__(self, name: str, __value):
        
        if name == "k":

            print("hello")

            

print(1)
fd = FrenchDeck()
fd.k

