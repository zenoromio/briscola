from enum import Enum, auto
from typing import *
from random import shuffle, seed, randint
from abc import ABC, abstractmethod

class Suit(Enum):
    """
    Class used for classification of card suits.
    """

    HEARTS = auto()
    CLUBS = auto()
    SPADES = auto()
    DIAMONDS = auto()

    def __str__(self) -> str:
        """
        __str__ method, returns the name of the suit as a string (eg. str(Suit.HEARTS) -> "HEARTS")

        :return: (str): The name of the suit as a string.
        """
        return self.name


class Rank(Enum):
    """
    Class defining the card ranks.
    """

    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()

    def __str__(self) -> str:
        """
        __str__ method, returns the name of the rank as a string (eg. str(Rank.ACE) -> "ACE")

        :return: (str): The name of the rank as a string.
        """
        return self.name


class Card(Enum):
    """
     Class defining individual cards.

    :param rank (Rank): The rank of the card.
    :param suit (Suit): The suit of the card.
    :param character (str): The character representation of the card.
    :attr rank (Rank): The rank of the card.
    :attr suit (Suit): The suit of the card.
    :attr character (str): The character representation of the card.
    """

    # Each possible card is definied below as a tuple of (rank, suit, character)
    ACE_HEARTS = (Rank.ACE, Suit.HEARTS)
    TWO_HEARTS = (Rank.TWO, Suit.HEARTS)
    THREE_HEARTS = (Rank.THREE, Suit.HEARTS)
    FOUR_HEARTS = (Rank.FOUR, Suit.HEARTS)
    FIVE_HEARTS = (Rank.FIVE, Suit.HEARTS)
    SIX_HEARTS = (Rank.SIX, Suit.HEARTS)
    SEVEN_HEARTS = (Rank.SEVEN, Suit.HEARTS)
    JACK_HEARTS = (Rank.JACK, Suit.HEARTS)
    QUEEN_HEARTS = (Rank.QUEEN, Suit.HEARTS)
    KING_HEARTS = (Rank.KING, Suit.HEARTS)

    ACE_CLUBS = (Rank.ACE, Suit.CLUBS)
    TWO_CLUBS = (Rank.TWO, Suit.CLUBS)
    THREE_CLUBS = (Rank.THREE, Suit.CLUBS)
    FOUR_CLUBS = (Rank.FOUR, Suit.CLUBS)
    FIVE_CLUBS = (Rank.FIVE, Suit.CLUBS)
    SIX_CLUBS = (Rank.SIX, Suit.CLUBS)
    SEVEN_CLUBS = (Rank.SEVEN, Suit.CLUBS)
    JACK_CLUBS = (Rank.JACK, Suit.CLUBS)
    QUEEN_CLUBS = (Rank.QUEEN, Suit.CLUBS)
    KING_CLUBS = (Rank.KING, Suit.CLUBS)
    
    ACE_SPADES = (Rank.ACE, Suit.SPADES)
    TWO_SPADES = (Rank.TWO, Suit.SPADES)
    THREE_SPADES = (Rank.THREE, Suit.SPADES)
    FOUR_SPADES = (Rank.FOUR, Suit.SPADES)
    FIVE_SPADES = (Rank.FIVE, Suit.SPADES)
    SIX_SPADES = (Rank.SIX, Suit.SPADES)
    SEVEN_SPADES = (Rank.SEVEN, Suit.SPADES)
    JACK_SPADES = (Rank.JACK, Suit.SPADES)
    QUEEN_SPADES = (Rank.QUEEN, Suit.SPADES)
    KING_SPADES = (Rank.KING, Suit.SPADES)

    ACE_DIAMONDS = (Rank.ACE, Suit.DIAMONDS)
    TWO_DIAMONDS = (Rank.TWO, Suit.DIAMONDS)
    THREE_DIAMONDS = (Rank.THREE, Suit.DIAMONDS)
    FOUR_DIAMONDS = (Rank.FOUR, Suit.DIAMONDS)
    FIVE_DIAMONDS = (Rank.FIVE, Suit.DIAMONDS)
    SIX_DIAMONDS = (Rank.SIX, Suit.DIAMONDS)
    SEVEN_DIAMONDS = (Rank.SEVEN, Suit.DIAMONDS)
    JACK_DIAMONDS = (Rank.JACK, Suit.DIAMONDS)
    QUEEN_DIAMONDS = (Rank.QUEEN, Suit.DIAMONDS)
    KING_DIAMONDS = (Rank.KING, Suit.DIAMONDS)

    def __init__(self, rank: Rank, suit: Suit) -> None:
        self.rank = rank
        self.suit = suit


    def __str__(self) -> str:
        """
        Str method for the card class.

        :return: (str): The string representation of the card.
        """
        return f"Card.{self.name}"


class RandomDeck:

    def __init__(self, seed_value: Optional[int] = None) -> None:
        
        if seed_value is None:
            seed_value = randint(0, 10000)
        seed(seed_value)

        self.cards = self._get_cards()

    def _get_cards(self) -> List[Card]:
        """
        Function use internally to create the deck's cards.
        """

        deck = []

        for card in Card:
            deck.append(card)
        
        shuffle(deck)

        return deck
    
    def last_card(self) -> Card:
        
        return self.cards[-1] 
    
    def generate_hands(self) -> tuple[List[Card], List[Card]]:

        hand1 = []
        hand2 = []

        for i in range(0, 6):

            if i % 2:
                card = self.cards.pop(0)
                hand1.append(card)
            else:
                card = self.cards.pop(0)
                hand2.append(card)

        return hand1, hand2

class TrickScorer:
    
    SCORES = {
            Rank.ACE: 10,
            Rank.TWO: 1,
            Rank.THREE: 9,
            Rank.FOUR: 2,
            Rank.FIVE: 3,
            Rank.SIX: 4,
            Rank.SEVEN: 5,
            Rank.JACK: 6,
            Rank.QUEEN: 7,
            Rank.KING: 8
        }
    
    POINTS = {
            Rank.ACE: 11,
            Rank.TWO: 0,
            Rank.THREE: 10,
            Rank.FOUR: 0,
            Rank.FIVE: 0,
            Rank.SIX: 0,
            Rank.SEVEN: 0,
            Rank.JACK: 2,
            Rank.QUEEN: 3,
            Rank.KING: 4
        }
    
    def rank_to_value(rank: Rank) -> int:
        
        return TrickScorer.SCORES[rank]
    
    def rank_to_points(rank: Rank) -> int:
        
        return TrickScorer.POINTS[rank]

class GameState:

    def __init__(self, name1: str, name2: str) -> None:
        self.won_cards: List[Card] = []
        self.points = {name1: 0, name2: 0}

class PlayingBot(ABC):

    def __init__(self, name: str) -> None:
        self.name = name
        self.hand: List[Card] = []

    @abstractmethod
    def make_move(self, opponent_card: Optional[Card], briscola: Suit, gamestate: GameState) -> Card:
        """
        Get the move this Bot wants to play. This is the method that gets called by the engine to get the bot's next move.
        If this Bot is leading, the leader_move will be None. If this both is following, the leader_move will contain the move the opponent just played

        :param perspective: (PlayerPerspective): The PlayerPerspective which contains the information on the current state of the game from the perspective of this player
        :param leader_move: (Optional[Move]): The move made by the leader of the trick. This is None if this bot is the leader.
        """

    def __eq__(self, other) -> bool:
        
        if self.name == other.name:
            return True
        
        return False
    
    def __str__(self) -> str:
        
        return f"{self.name}"

        
class GameEngine:

    def __init__(self, player1: PlayingBot, player2: PlayingBot) -> None:
        self.player1 = player1
        self.player2 = player2

    def play_game(self) -> Optional[PlayingBot]:

        deck = RandomDeck()
        hand1, hand2 = deck.generate_hands()
        briscola = deck.last_card().suit
        
        leader = self.player1
        follower = self.player2

        gamestate = GameState(leader.name, follower.name)

        leader.hand.extend(hand1)
        follower.hand.extend(hand2)

        while leader.hand and follower.hand:
            winner: PlayingBot
            won_cards: List[Card]
            winner, won_cards = self.calculate_winner(leader, follower, briscola, gamestate)

            gamestate.points[winner.name] += self.calculate_points_of_cards(won_cards)
            gamestate.won_cards.extend(won_cards)

            if deck.cards:
                first_draw = deck.cards.pop(0)
                leader.hand.append(first_draw)
                
                second_draw = deck.cards.pop(0)
                follower.hand.append(second_draw)

            if leader != winner and deck.cards:
                leader, follower = follower, leader

        if gamestate.points[leader.name] > gamestate.points[follower.name]:
            #print(f"{leader.name} won with a score of {gamestate.points[leader.name]}-{gamestate.points[follower.name]}!")
            
            return leader
        elif gamestate.points[leader.name] < gamestate.points[follower.name]:
            #print(f"{follower.name} won with a score of {gamestate.points[leader.name]}-{gamestate.points[follower.name]}!")

            return follower
        else:
            #print(f"Even wtf?? {gamestate.points[leader.name]}-{gamestate.points[follower.name]}")

            return None

    def calculate_winner(self, leader: PlayingBot, follower: PlayingBot, briscola: Suit, gamestate: GameState) -> tuple[PlayingBot, List[Card]]:
        
        ranker = TrickScorer
        leader_move = leader.make_move(None, briscola, gamestate)
        follower_move = follower.make_move(leader_move, briscola, gamestate)

        cards = [leader_move, follower_move]

        if leader_move.suit == follower_move.suit:

            if ranker.rank_to_value(leader_move.rank) > ranker.rank_to_value(follower_move.rank):
                return leader, cards
            
            return follower, cards
        
        elif leader_move.suit == briscola:
            
            return leader, cards
        
        elif follower_move.suit == briscola: 

            return follower, cards
        
        else:

            return leader, cards
        
    def calculate_points_of_cards(self, cards: List[Card]) -> int:

        ranker = TrickScorer

        score = 0

        for card in cards:
            score += ranker.rank_to_points(card.rank)

        return score