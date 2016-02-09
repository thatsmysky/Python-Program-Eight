import Card


class Player(object):
    def __init__(self):
        pass

    def IsBetterCard_Partner_Lead(self, card, trick, hand):
        # if your card is worse then theirs:
        if len(hand) == 1:
            return True
        if Card.Card.__lt__(card, trick[0]):
            # if your card is better than the person to your right's:
            if Card.Card.__ge__(card, trick[1]):
                # play that card
                return True
            else:
                # if your card is worse than the person to your right's:

                if Card.Card.Rank(trick[0]) == "A":  # you cant beat an Ace
                    return True
                if Card.Card.Rank(trick[1]) == "A":
                    return True
                if Card.Card.Rank(trick[0]) == "K":
                    # we know you dont have an ace
                    return True
                else:
                    return True  # chance it you dont have a better card
        else:  # if your card is better than your partner's:
            # but it's better than the person to your right's:
            if Card.Card.__ge__(card, trick[1]):
                # play that card
                return True
            else:  # better than partner but worse than person on right's:
                return True

    def IsBetterCard_Partner_Hasnt_Gone(self, card, trick, hand):
        # if your partner hasn't played at all:
        # if your card is better than the person on your right's:
        if Card.Card.__ge__(card, trick[0]):
            # play that card
            return True
        # if your card is worse than the person on your right's:
        if Card.Card.__lt__(card, trick[0]):
            if card == hand[-1]:
                return True
            else:
                # don't play that card
                return False

    def IsBetterCard(self, card, trick, hand):
        # if your partner has played:
        if len(hand) == 1:
            return True
        # if your card is worse then theirs:
        if Card.Card.__lt__(card, trick[1]):
            # if your card is better than the person to your right's:
            if Card.Card.__gt__(card, trick[2]):
                # play that card
                return True
            else:
                # if your card is worse than the person to your right's:
                return True  # you dont have a better card
        else:  # if your card is better than your partner's:
            # but it's better than the person to your right's:
            if Card.Card.__gt__(card, trick[2]):
                # play that card
                return True
            else:  # if it's worse than everyone's:
                # discard
                return True

    def IsAce(self, card):
        if Card.Card.Rank(card) == "A":
            return True

    def IsKing(self, card):
        if Card.Card.Rank(card) == "K":
            return True

    def IsTrumpCard(self, card, trump):
        if Card.Card.Suit(card) in trump:
            return True
        else:
            return False

    def IsValidCard(self, card, trick):
        if Card.Card.Suit(card) == Card.Card.Suit(trick[0]):
            return True
        else:
            return False

    def PlayCard(self, hand: [], trick, trump, position: "", played_tricks: [], Score):
        Spades = []
        Hearts = []
        Clubs = []
        Diamonds = []
        for card in hand:
            if Card.Card.Suit(card) == "S":
                Spades.append(card)
            if Card.Card.Suit(card) == "H":
                Hearts.append(card)
            if Card.Card.Suit(card) == "C":
                Clubs.append(card)
            if Card.Card.Suit(card) == "D":
                Diamonds.append(card)
        if len(trick) == 0:
            for card in hand:
                if len(hand) == 1:
                    return card
            for card in hand:
                if self.IsAce(card):
                    return card
            for card in hand:
                if self.IsKing(card):
                    return card
            for card in hand:
                if Card.Card.IsFaceCard(card):
                    return card
                elif self.IsTrumpCard(card, trump):
                    return card
            for card in hand:
                if card == hand[-1]:
                    return card
        if len(trick) <= 2:
            for card in hand:
                if len(hand) == 1:
                    return card
                if Card.Card.Suit(trick[0]) == "S":
                    if len(trick) == 2:
                        if len(Spades) > 0:
                            for spad in Spades:
                                if self.IsBetterCard_Partner_Lead(spad, trick, Spades):
                                    return spad
                    if len(trick) == 1:
                        if len(Spades) > 0:
                            for spad in Spades:
                                if self.IsBetterCard_Partner_Hasnt_Gone(spad, trick, Spades):
                                    return spad
                if Card.Card.Suit(trick[0]) == "H":
                    if len(trick) == 2:
                        if len(Hearts) > 0:
                            for heart in Hearts:
                                if self.IsBetterCard_Partner_Lead(heart, trick, Hearts):
                                    return heart
                    if len(trick) == 1:
                        if len(Hearts) > 0:
                            for heart in Hearts:
                                if self.IsBetterCard_Partner_Hasnt_Gone(heart, trick, Hearts):
                                    return heart
                if Card.Card.Suit(trick[0]) == "C":
                    if len(trick) == 2:
                        if len(Clubs) > 0:
                            for club in Clubs:
                                if self.IsBetterCard_Partner_Lead(club, trick, Clubs):
                                    return club
                    if len(trick) == 1:
                        if len(Clubs) > 0:
                            for club in Clubs:
                                if self.IsBetterCard_Partner_Hasnt_Gone(club, trick, Clubs):
                                    return club
                if Card.Card.Suit(trick[0]) == "D":
                    if len(trick) == 2:
                        if len(Diamonds) > 0:
                            for dim in Diamonds:
                                if self.IsBetterCard_Partner_Lead(dim, trick, Diamonds):
                                    return dim
                    if len(trick) == 1:
                        if len(Diamonds) > 0:
                            for dim in Diamonds:
                                if self.IsBetterCard_Partner_Hasnt_Gone(dim, trick, Diamonds):
                                    return dim
            else:
                for new in hand:
                    if self.IsTrumpCard(new, trump):
                        return new
                for new in hand:
                    if new == hand[-1]:
                        return new
                    else:
                        return new
        if len(trick) == 3:
            for card in hand:
                if len(hand) == 1:
                    return card
            if Card.Card.Suit(trick[0]) == "S":
                if len(trick) == 3:
                    if len(Spades) > 0:
                        for spad in Spades:
                            if self.IsBetterCard(spad, trick, Spades):
                                return spad
            if Card.Card.Suit(trick[0]) == "H":
                if len(trick) == 3:
                    if len(Hearts) > 0:
                        for heart in Hearts:
                            if self.IsBetterCard(heart, trick, Hearts):
                                return heart
            if Card.Card.Suit(trick[0]) == "C":
                if len(trick) == 3:
                    if len(Clubs) > 0:
                        for club in Clubs:
                            if self.IsBetterCard(club, trick, Clubs):
                                return club
            if Card.Card.Suit(trick[0]) == "D":
                if len(trick) == 3:
                    if len(Diamonds) > 0:
                        for dim in Diamonds:
                            if self.IsBetterCard(dim, trick, Diamonds):
                                return dim
            for card in hand:
                if self.IsTrumpCard(card, trump):
                    return card
            for card in hand:
                if card == hand[-1]:
                    return card
                else:
                    return card
