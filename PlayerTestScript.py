import Card
import unittest
import inspect
import random
import pickle

from Player import Player 





# If this module is being run as main then begin testing.
if __name__ == "__main__":

    card_suits = list("SHDC")
    card_ranks = list("AKQJT98765432")

    # Class used for testing.
    class TestWhistPlayerMethods(unittest.TestCase):
        def test_player_creation(self):
            """ Tests if the Player is an class that can be instanced """
            
            # There must be a WhistPlayer in the globals()
            self.assertTrue("Player" in globals(), "You must define a Player Class")

            # Whist player must be a class
            self.assertTrue(inspect.isclass(Player), "Player object must be a class")

            # The Player must be of type type.
            player = Player()
            self.assertIsInstance(player, Player)

        def test_PlayCard_creation(self):
            """ Tests that the Player has a PlayCard method with the proper number of parameters """            

            # Is there a playcard in the class.
            self.assertTrue("PlayCard" in Player.__dict__, "Player must have a PlayCard method")

            # Is playcard callable?
            self.assertTrue(callable(Player.PlayCard), "PlayCard should be a function")

            # Does playcard have correct number of parameters?
            self.assertEqual(len(inspect.getfullargspec(Player.PlayCard)[0]), 7, "There should be seven parameters for PlayCard method" )

        def test_PlayCard_returns_card(self):
            """ Given a single card to play, does the player play an instance of card? """

            players_cards = (Card.Card("D", "9"), )

            player = Player()
            return_card = player.PlayCard(players_cards, [], "C", "S", [], (0, 0))
            self.assertIsInstance(return_card, Card.Card, "PlayCard must return a card")
            

        def test_PlayCard_returns_lead_suit_card(self):
            """ If player has one of the trump cards, he must play one of the trump cards """
            trump = "D"
            lead_card = Card.Card("C", random.choice(card_ranks))

            # Player has one card that is the same card as the trump card.  Trump card is last card.
            players_cards = tuple((Card.Card(card[0], card[1]) for card in ['HA', 'D2', 'HJ', 'S9', 'H5', 'H2', 'D8', 'DA', 'SQ', 'H3', 'S7', 'S6', 'C9']))

            player = Player()
            return_card = player.PlayCard(players_cards, (lead_card, ), trump, "S", [], (0, 0))
            self.assertIsInstance(return_card, Card.Card, "PlayCard must return a card")
            self.assertEqual(return_card, players_cards[-1], "The last card should be the one played.  It is the only trump card")

        def test_PlayCard_returns_card_if_no_lead_suit_available(self):
            """ If player has one of the trump cards, he must play one of the trump cards """
            trump = "D"
            lead_card = Card.Card("C", random.choice(card_ranks))

            # Player has one card that is the same card as the trump card.  Trump card is last card.
            players_cards = tuple((Card.Card(card[0], card[1]) for card in ['HA', 'D2', 'HJ', 'S9', 'H5', 'H2', 'D8', 'DA', 'SQ', 'H3', 'S7', 'S6', 'H9']))

            player = Player()
            return_card = player.PlayCard(players_cards, (lead_card, ), trump, "S", [], (0, 0))
            self.assertIsInstance(return_card, Card.Card, "PlayCard must return a card")

            # The return card can be any of the cards in the players hand.
            for card in players_cards:
                if card == return_card:
                    break
            else:
                self.fail("The card returned must be one of the cards the player had. {} returned".format(repr(return_card)))

        def test_PlayCard_returns_valid_option_for_mass_data(self):
            """ use a data file to test users data for a lot of possibilities 2860 to be exact """

            play_card_lines = pickle.load(open("example_hands.pik", "rb"))
            for hand, trick, trump_suit, player_pos, played, score, valid_cards in play_card_lines:
                player = Player()
                return_card = player.PlayCard(hand, trick, trump_suit, player_pos, played, score)
                self.assertTrue(return_card in valid_cards, "Played Invalid Card {} for hand:{}, trick{}, valid_cards:{}".format(repr(return_card), hand, trick, valid_cards))


    can_create_suite = unittest.TestSuite()
    can_create_suite.addTest(TestWhistPlayerMethods("test_player_creation"))

    test_runner = unittest.TextTestRunner()
    print("Testing Creation and type of Player")
    result = test_runner.run(can_create_suite)
    if result.wasSuccessful():

        can_call_playcard = unittest.TestSuite()
        can_call_playcard.addTest(TestWhistPlayerMethods("test_PlayCard_creation"))
        print("\n\nTest PlayCard is a method of Player")
        result = test_runner.run(can_call_playcard)

        # Test proper play with small examples
        if result.wasSuccessful():
            play_suite = unittest.TestSuite()
            play_suite.addTest(TestWhistPlayerMethods("test_PlayCard_returns_card"))
            play_suite.addTest(TestWhistPlayerMethods("test_PlayCard_returns_lead_suit_card"))
            play_suite.addTest(TestWhistPlayerMethods("test_PlayCard_returns_card_if_no_lead_suit_available"))
            print("\n\nTest PlayCard operates properly.")
            result = test_runner.run(play_suite)

            if result.wasSuccessful():
                play_suite = unittest.TestSuite()
                play_suite.addTest(TestWhistPlayerMethods("test_PlayCard_returns_valid_option_for_mass_data"))
                print("\n\nTest PlayCard operates properly for pickled data.")
                result = test_runner.run(play_suite)
