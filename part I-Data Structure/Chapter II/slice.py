l=[10,20,30,40,50,60]

### s[a:b:c] can be used to specify a stride or step c
s = 'bicycle'
# print(s[::3])
# print(s[::-2])

import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchCard:

    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:

        self.card = [Card(rank,suit) for rank in self.ranks for suit in self.suits]

    def __getitem__(self,option):

        return (self.card[option])
    
    def __str__(self):
        
        output = ''
        for card in self.card:
            output += f'{card} \n'

        return output

deck = FrenchCard()
# print(deck)
# print(deck[12::13])

### if x is a four-dimensional array, x[i, ...] is a shortcut for x[i, :, :, :,]


import numpy as np

# a=np.zeros((4,2,1,1))

# print(a[1,...])

################  Assigning to Slices #####################

l = list(range(10))
# print(l)
l[2:5] = [20, 30]
del l[5:7]
# print(l)

# print(len(l[3::2]))

################  Using + and * with Sequences ##################

l=[[1]]
# print(l * 5)

################  Building Lists of Lists  #####################

## A list with three lists of length 3 can represent a tic-tac-toe board
board = [['_'] * 3 for i in range(3)]
# print(board)

# board[1][2] = 'X'
# print(board)

weird_board = [['_'] * 3] * 3
weird_board[1][2] = "O"
# print(weird_board)

row=['_']*3 
board = []
for i in range(3):
    board.append(row)

# -----------------------------------

board = []
for i in range(3):
    row=['_']*3
    board.append(row)

