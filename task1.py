import sys
import pyCardDeck
from pyCardDeck.cards import *
import typing
from typing import List


class Person:

    def __init__(self, name: str):
	self.n = name
        self.hand = []
        

    def __str__(self):
        return self.n

class BlackjackGame:

    def __init__(self, person: List[Person]):
        self.d = pyCardDeck.Deck()
        self.d.load_standard_deck()
        self.person = persons
        self.score = {}
        print("lets make a game with {} people.".format(len(self.persons)))

    def blackjack(self):
        """
        The main blackjack game is

        every person comes ones and take a turn
	if no one wins, the person with the coser 21 wins
        """
        print("deal starts...")
        print("Lets Shuffle...")
        self.d.shuffle()
        print("shuffld")
        self.deal()
        print("its play time")
        for persons in self.persons:
            print("{} the turn is yours.".format(persons.name))
            self.play(persons)
        else:
            print("it was the last turn")
            self.find_winner()
	    print ("the winner was")

    def deal(self):
        """
        gIves 5 cards to each person
        """
        for i in range(5):
            for p in self.person:
                newcard = self.d.draw()
                p.hand.append(newcard)
                print("Dealt {} the {}.".format(p.name, str(newcard)))

    def find_winner(self):
        """
        it will find the max score and the player who is having the max score .
        """
        winners = []
        try:
            win_score = max(self.scores.values())
            for key in self.score.keys():
                if self.score[key] == win_score:
                    winners.append(key)
                else:
                    
            winstring = " & ".join(winners)
            print("And the winner is...{}!".format(winstring))
        except ValueError:
            print("Whoops! Everybody lost!")

    def hit(self, person):
        
        newcard = self.d.draw()
        person.hand.append(newcard)
        print("   Drew the {}.".format(str(newcard)))

    def play(self, person):
        
        while True:
            points = sum_hand(person.hand)

            if points < 17:
                print("   Hit.")
                self.hit(person)
            elif points == 21:
                print("   {} wins!".format(person.name))
                sys.exit(0) # End if someone wins
            elif points > 21:
                print("   Bust!")
                break
            else:  # Stand if between 17 and 20 (inclusive)
                print("   Standing at {} points.".format(str(points)))
                self.scores[person.name] = points
                break

def sum_hand(hand: list):
    """
    Converts ranks of cards into point values for scoring purposes.
    'K', 'Q', and 'J' are converted to 10.
    'A' is converted to 1 (for simplicity), but if the first hand is an ace
    and a 10-valued card, the player wins with a blackjack.
    """
    vals = [card.rank for card in hand]
    intvals = []
    while len(vals) > 0:
        value = vals.pop()
        try:
            intvals.append(int(value))
        except ValueError:
            if value in ['K', 'Q', 'J']:
                intvals.append(10)
            elif value == 'A':
                intvals.append(1)  # Keep it simple for the sake of example
    if intvals == [1, 10] or intvals == [10, 1]:
        print("   Blackjack!")
        return(21)
    else:
        points = sum(intvals)
        print("   Current score: {}".format(str(points)))
        return(points)


if __name__ == "__main__":
    game = BlackjackGame([Player("lakshay"), Player("akshay"), Player("baba"),
        Player("Simon"),Player("simon"),Player("thomas"),Player("deca"),Player("lovepreet"),Player("theTrump")])
    game.blackjack()

