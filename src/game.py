import random
from piece_type import PieceType
from queue import Queue

from src.board import Board
from src.rule_type import RuleType
from src.winner import Winner


class Game:

    def __init__(self, p1, p2):
        self.queue = Queue()
        self.board = None
        self.rules = []
        self.initialize_players(p1, p2)
        self.initialize_board()
        self.initialize_rules()

    def initialize_players(self, p1, p2):
        first_player = random.choice([p1, p2])
        second_player = list({p1, p2} - {first_player})[0]
        first_player.set_playing_piece(PieceType.X.value)
        second_player.set_playing_piece(PieceType.O.value)
        print("Player %s will play first with %s" %
              (first_player.get_player_name(), first_player.get_playing_piece()))
        print("Player %s will play Second with %s" %
              (second_player.get_player_name(), second_player.get_playing_piece()))
        self.queue.put(first_player)
        self.queue.put(second_player)

    def initialize_board(self):
        board_size = int(input("Enter board Size: "))
        self.board = Board(board_size)

    def initialize_rules(self):
        print("Enter Y or N to select or reject a rule")
        while True:
            for rule_type in RuleType:
                while True:
                    rule = input("Do you want a %s rule for your game: " % rule_type.value)
                    if rule not in ["Y", "N"]:
                        print("Invalid choice: %s. Enter Y or N to select or reject a rule" % rule)
                        continue
                    elif rule == "Y":
                        self.rules.append(rule_type.value)
                    break
            if len(self.rules) == 0:
                print("Please select atleast one rule")
            else:
                break
        print("Game Rules: %s" % self.rules)

    def start_game(self):
        free_cells = True
        winning_player = None
        while free_cells:
            self.board.print_board()
            free_cells = self.board.check_free_cells()
            if not free_cells:
                continue
            current_player = self.queue.get()
            print("Player %s your turn" % current_player.get_player_name())
            row = input("Enter row number: ")
            col = input("Enter col number: ")
            error = self.board.add_piece(row, col, current_player.get_playing_piece())
            if error:
                print(error)
                self.queue.put(current_player)
                current_player = self.queue.get()
                self.queue.put(current_player)
                continue
            winner = Winner.check_winner(self.board, self.rules, int(row), int(col), current_player.get_playing_piece())
            if winner:
                self.board.print_board()
                winning_player = current_player
                break
            self.queue.put(current_player)
        if winning_player:
            print("%s is the winner" % current_player.get_player_name())
        else:
            print("Game is Tied")
