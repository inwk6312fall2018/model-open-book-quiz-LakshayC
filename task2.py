import sys
import pyCardDeck
from pyCardDeck.cards import PokerCard

class person:

    def __init__(self, name: str):
        self.h = []
        self.n = name

    def __str__(self):
        return self.n

class BlackTheJack:

    def __init__(self, persons: List[Person]):
        self.d = pyCardDeck.Deck()
        self.d.load_standard_deck()
        for i in range(44)
            bur = self.deck.draw()
            if bur == 10:
                self.deck.discard(bur)
        self.persons = persons
        self.scores = {}
        print("Lets play a game with {} pppl.".format(len(self.persons)))

    def blackjack(self):
        """
       now black jack

      if no one got 21 the person with closest to 21 wins
        """
        print("lets start")
        print("Shuffled")
        self.deck.discard('eight')
        self.deck.shuffle()
        print("its a deasl.")
        self.deal()
        print("now playh")
        for person in self.persons:
            print("{}the turn is urs".format(person.n))
            self.play(person)
        else:
            self.find_winner()

    def deal(self):
        """
        now the 10 person.
        """
        for _ in range(10):
            for p in self.persons:
                newcard = self.deck.draw()
                p.h.append(newcard)
                print("{} {}.".format(p.n, str(newcard)))

    def find_winner(self):
        """
       lets find the winner.
        """
        winners = []
        try:
            win_score = max(self.scores.values())
            for key in self.scores.keys():
                if self.scores[key] == win_score:
                    winners.append(key)
                else:
                   
            winstring = " & ".join(winners)
            print("the wonner is {}!".format(winstring))
        except ValueError:
            print("no one one")

    def hit(self, person):
        
        newcard = self.deck.draw()
        person.h.append(newcard)
        print("Drew the {}.".format(str(newcard)))

    def play(self, person):
        """
        An individual person's turn.

        If the person's cards are an ace and a ten or court card,
        the person has a blackjack and wins.

        If a person's cards total more than 21, the person loses.

        Otherwise, it takes the sum of their cards and determines whether
        to hit or stand based on their current score.
        """
        while True:
            points = sum_h(person.h)

            if points < 17:
                print("   Hit.")
                self.hit(person)
            elif points == 21:
                print("   {} youwins!".format(person.n))
                sys.exit(0) # End if someone wins
            elif points > 21:
                print("  its Bust!")
                break
            else:  # Stand if between 17 and 20 (inclusive)
                print("  the Standing at {} points.".format(str(points)))
                self.scores[person.n] = points
                break

def sum_h(h: list):
    """
   it convers the alphanet carfds to number eg A=1,10 J=11
    """
    vals = [card.rank for card in h]
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


if __n__ == "__main__":
    game = BlackTheJack([Person("RAM"), Person("SITA"), Person("AMBANI"),Person("JHON"), Person("PLAYES"),
        Person("DCKSON")])
    game.blackjack()

