from deck_manipulator import DeckManipulator


class HiLoGame:
    game_outcomes = {
        'higher': 'Wow, you were right! The second card is higher. You won!',
        'equal': "You guessed it correctly! It's a draw.",
        'lower': 'You were correct! The second card is lower and you win!',
    }
    expected_guess = ''
    player_guess = ''

    def __init__(self):
        self.new_game = DeckManipulator(52, 2)

    def start_game(self):
        if self.new_game.secret_hand:
            self.new_game.secret_hand[0] = self.new_game.secret_hand.pop(1)
            self.new_game.shuffle_deck()
            self.new_game.delete_card(self.new_game.temporary_card_name_deck,
                                      self.new_game.secret_hand[0])

        self.new_game.check_hand(self.new_game.secret_hand)

        print(f'The first card is:\n\t{self.new_game.secret_hand[0]}.')

        self.player_guess = input("Will the second card be 'higher',"
                                  " 'equal', or 'lower'?\n - ")

        print(f'The second card is:\n\t{self.new_game.secret_hand[1]}')
        print(self.analyzing_results())

    def analyzing_results(self):
        result = \
            -(self.new_game.compare_cards(self.new_game.secret_hand[0],
                                          self.new_game.secret_hand[1]))

        if result == -1:
            self.expected_guess = 'lower'
        elif result == 0:
            self.expected_guess = 'equal'
        elif result == 1:
            self.expected_guess = 'higher'

        if self.expected_guess == self.player_guess.lower():
            return f'{self.game_outcomes[self.player_guess.lower()]}\n'
        elif self.expected_guess != self.player_guess.lower():
            return 'Unfortunately, your guess was incorrect...\n'

    def continue_playing(self):
        while True:
            another_game = input('Would you like to play another game?'
                                 '\n\tYes/No'
                                 '\n - ')
            if another_game.lower() == 'yes' or another_game.lower() == 'y':
                print("Great! Let me reshuffle the deck...\n")
                self.start_game()
            elif another_game.lower() == 'no' or another_game.lower() == 'n':
                print('Okay. See you later!')
                break
            else:
                print('Unrecognized input. Please, restart the game.')
                break
