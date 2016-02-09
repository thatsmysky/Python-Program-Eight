import random

''' Card object.
Public methods:
    Initializer (__init__) has parameters S & R for Suit & Rank.
        Both default to empty strings. S is expected to be one
        of 'S', 'H', 'D', 'C'. R is expected to be a one-character
        string ('2', '3', '4', etc., to 'T' for 10, 'J', 'Q', 'K', 'A').
        Parameters are stripped of whitespace & made upper case. Non-string
        parameters will cause CardError to be raised. 
    Suit(): Returns suit (1-character string)
    Rank(): Returns rank (1-character string)
    FaceUp(): Returns true if card is currently face-up, false otherwise
    TurnFaceUp(): Turns card face up
    TurnFaceDown(): Turns card face down
    Color(): Returns 'B' for black if suit is 'S' or 'C', otherwise returns
             'R' for red
    str() returns 3-character string. Blank/rank/suit if card is face-up,
          ' XX' if card is face down.
    repr() method returns string as if card were face up. 
    Comparison operators are defined. Comparison is based on rank. Suit is
         ignored EXCEPT for equality/inequality. Ordering comparisons (lt, le, gt, etc.)
         ignore suit. Ace always counts high (above K).

See description farther down for DeckOfCards class.
'''         

class CardError(Exception):
    pass 
    

class Card(object):
    def __init__(self, S='', R=''):
        try:
            self.__suit = S.strip().upper()
            self.__rank = R.strip().upper()
        except TypeError:
            raise CardError 
        self.__faceUp = False
        

    def Suit(self):
        return self.__suit

    def Rank(self):
        return self.__rank

    def FaceUp(self):
        return self.__faceUp

    def TurnFaceUp(self):
        self.__faceUp = True

    def TurnFaceDown(self):
        self.__faceUp = False

    def Color(self):
        if self.__suit in "SC":
            return 'B'
        else:
            return 'R'

    def IsFaceCard(self):
        if self.__rank in 'JQK':
            return True
        else:
            return False

    def __lt__(self, rhs):
        ranks = 'AKQJT98765432'
        try:
            MyRank = ranks.index(self.__rank)
            ItsRank = ranks.index(rhs.Rank())
        except ValueError:  # wasn't in string of possible values
            raise CardError() 
        return MyRank > ItsRank

    def __ge__(self, rhs):
        return not(self.__lt__(rhs))
    
    def __le__(self, rhs):
        return (self.__lt__(rhs) or self.__rank == rhs.Rank())

    def __gt__(self, rhs):
        return not(self.__le__(rhs))

    def __eq__(self, rhs):
        return self.__rank == rhs.Rank() and self.__suit == rhs.Suit()
        
    def __ne__(self, rhs):
        return not(self.__eq__(rhs))
    
    def __str__(self):
        if self.__faceUp:
            return ' '+ self.__rank + self.__suit
        else:
            return ' XX'

    def __repr__(self): 
           return ' '+ self.__rank + self.__suit


class DeckError(Exception):
    pass

''' Deck of Cards class.
Public methods:
   Initializer has 1 parameter, NDecks, defaults to 1. The number of standard
      52-card decks should be created as part of this deck (some games require
      multiple decks shuffled together). Nonstandard decks such as Pinochle decks
      not supported at this time. Jokers not supported in this version.
   str() method prints values of all cards, arranged in rows of 8. (returns
      1 string with embedded \n characters.)
   repr() method: same as str() 
   len() returns number of cards in deck
   Count(): same as len()
   Shuffle(): uses random.shuffle() to rearrange cards in deck randomly
   DealOne(): Returns one Card, the top one from the deck, which is removed. If
      deck is empty, a DeckError is raised.
'''      
   
class DeckOfCards(object):
    def __init__(self, NDecks = 1):
        self.__cards = []
        for j in range(NDecks):
            for suit in 'SHDC':
                for rank in "AKQJT98765432":
                    self.__cards.append(Card( suit, rank))
                
    def __str__(self):
        Output = ''
        Counter = 0
        for card in self.__cards:
            Output = Output + repr(card)
            Counter = (Counter+1) % 8
            if Counter == 0:
                Output = Output + '\n'
        return Output

    def __len__(self):
        return len(self.__cards) 

    def Count(self):
        return len(self.__cards)
    
    def Shuffle(self):
        random.shuffle(self.__cards)

    def DealOne(self):
        try:
            return self.__cards.pop()
        except:
            raise DeckError()
        
    

        
if __name__ == '__main__':
    D = DeckOfCards()
    D.Shuffle()
    print(len(D))
    for j in range(5):
        C = D.DealOne()
        C.TurnFaceUp()
        print(C)
    print(len(D))
    # test of comparison operators
    C1 = Card('S', '5')
    C2 = Card('s', '6')
    if C1 < C2:
        print("< operator returns true when it should")
    if C1 == C2:
        print("== operator returns true when it shouldn't.")
    if C1 >= C2:
        print(">= operator returns true when it shouldn't.")
    if C1 > C2:
        print("> operator returns true when it shouldn't.")










'''
class PieException(Exception):
    pass


class Pie(object):
    def Hello(self):
        return "Hi, I'm a pie."
    
    def __init__(self, PieType='Apple'):
        self.Type = PieType
        self.Size = 9 

    def __str__(self):
        return "I'm a {}-inch {} pie.".format(self.Size, self.Type)
    

        
class Meringue(Pie):
    def Hello(self):
        return "My topping is light and fluffy."
    

class Oven(object):
    def __init__(self):
        self.Temp = 300
        self.InUse = False

    def __str__(self):
        return "Oven is at {} degrees.".format(self.Temp)

    def bake(self, treat, temp = 300):
        self.InUse = True
        self.Temp = temp
        
        
'''
