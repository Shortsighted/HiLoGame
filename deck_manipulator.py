import random

SUITS = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
SINGLE_SUIT = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14,
}
deck = {}
card_name_deck = []


class DeckManipulator:
    deck_size = 0
    hand_size = 0
    temporary_deck = {}
    temporary_card_name_deck = []
    player_hand = []
    secret_hand = []
    trump_suit = ''
    cards_on_table = []
    played_card_pile = []

    def __init__(self, deck_size, hand_size):
        self.deck_size = deck_size
        self.hand_size = hand_size
        self.create_deck()

    def create_deck(self):
        for suit in SUITS:
            for card_name, card_value in SINGLE_SUIT.items():
                if card_value > (52 - self.deck_size) / 4 + 1:
                    deck[f'{card_name} of {suit}'] = card_value
                    card_name_deck.append(f'{card_name} of {suit}')

        self.shuffle_deck()

    def shuffle_deck(self):
        self.temporary_deck = {}
        for card, value in deck.items():
            self.temporary_deck[card] = value

        self.temporary_card_name_deck = []
        for card in card_name_deck:
            self.temporary_card_name_deck.append(card)

        random.shuffle(self.temporary_card_name_deck)

    def check_deck(self):
        if self.temporary_card_name_deck:
            return True
        else:
            return False

    def draw_card(self, card_position=0):
        new_card = self.temporary_card_name_deck.pop(card_position)

        return new_card

    @staticmethod
    def delete_card(card_location, card_name):
        del card_location[card_location.index(card_name)]

    @staticmethod
    def find_card_suit(card_name):
        for suit in SUITS:
            if suit in card_name:
                return suit

    def change_card_value(self, card_name, add_to_card_value):
        self.temporary_deck[card_name] += add_to_card_value

    def change_suit_values(self, card_suit, add_to_card_values):
        for card in self.temporary_deck:
            if card_suit in card:
                self.change_card_value(card, add_to_card_values)

    @staticmethod
    def play_card(chosen_hand, chosen_card):
        played_card = chosen_hand.pop(chosen_hand.index(chosen_card))

        return played_card

    @staticmethod
    def take_card(card, hand):
        hand.append(card)

    def choose_trump_card(self):
        trump_card = self.draw_card(card_position=-1)
        self.temporary_card_name_deck.append(trump_card)
        self.trump_suit = self.find_card_suit(trump_card)

        return trump_card

    def compare_cards(self, card_one, card_two):
        if self.temporary_deck[card_one] > self.temporary_deck[card_two]:
            return 1
        elif self.temporary_deck[card_one] == self.temporary_deck[card_two]:
            return 0
        else:
            return -1

    def draw_hand(self, chosen_hand, cards_needed):
        while cards_needed > 0:
            if self.check_deck():
                chosen_hand.append(self.draw_card())
                cards_needed -= 1
            else:
                break

    def check_hand(self, chosen_hand):
        if len(chosen_hand) < self.hand_size:
            cards_needed = self.hand_size - len(chosen_hand)
            self.draw_hand(chosen_hand, cards_needed)

    @staticmethod
    def show_hand(chosen_hand):
        cards_in_hand = ''
        for card in chosen_hand:
            cards_in_hand += f' - {card}\n'

        return cards_in_hand
