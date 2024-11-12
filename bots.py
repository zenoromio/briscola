from typing import *
from game import Card, Suit, PlayingBot, TrickScorer, GameState
from random import choice

class RandBot(PlayingBot):

    def __init__(self, name: str) -> None:
        self.name = name
        self.hand: List[Card] = []

    def make_move(self, follower: bool, briscola: Suit, gamestate: GameState) -> Card:

        card = choice(self.hand)
        self.hand.remove(card)

        return card
    
    def __eq__(self, other) -> bool:
        
        if self.name == other.name:
            return True
        
        return False
    
    def __str__(self) -> str:
        
        return f"{self.name}"
    
class ZenoBot(PlayingBot):

    def __init__(self, name: str) -> None:
        super().__init__(name) 
        self.hand: List[Card] = []

    def make_move(self, opponent_card: Optional[Card], briscola: Suit, gamestate: GameState) -> Card:
        
        ranker = TrickScorer

        if opponent_card and opponent_card.suit != briscola:

            move = None

            for card in self.hand:
                if card.suit == opponent_card.suit and ranker.rank_to_value(card.rank) > ranker.rank_to_value(opponent_card.rank):
                    move = card
            
            if not move and ranker.rank_to_points(opponent_card.rank) in [10, 11]:
                
                for card in self.hand:
                    if card.suit == briscola:
                        move = card
                        break

            if move:
                self.hand.remove(move)
                return move
            
        card = choice(self.hand)
        self.hand.remove(card)

        return card