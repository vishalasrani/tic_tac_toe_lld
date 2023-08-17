from src.board import Board
from src.rule_type import RuleType


class Winner:

    @staticmethod
    def __check_horizontal(board: Board, row: int, col: int, playing_piece: str):
        for col in range(0, board.get_board_size()):
            if board.get_cell_value(row, col) != playing_piece:
                return False
        return True

    @staticmethod
    def __check_vertical(board: Board, row: int, col: int, playing_piece: str):
        for row in range(0, board.get_board_size()):
            if board.get_cell_value(row, col) != playing_piece:
                return False
        return True

    @staticmethod
    def __check_diagonal(board: Board, row: int, col: int, playing_piece: str):
        board_size = board.get_board_size()
        if row == col:
            for row in range(0, board_size):
                if board.get_cell_value(row, row) != playing_piece:
                    return False
            return True
        elif row + col == board.get_board_size() - 1:
            for row in range(0, board_size):
                if board.get_cell_value(row, board_size - row - 1) != playing_piece:
                    return False
            return True
        else:
            return False

    winning_strategies_map = {
        RuleType.HORIZONTAL.value: __check_horizontal,
        RuleType.VERTICAL.value: __check_vertical,
        RuleType.DIAGONAL.value: __check_diagonal
    }

    @staticmethod
    def check_winner(board: Board, rules: list, row: int, col: int, playing_piece: str):
        for rule in rules:
            strategy = Winner.winning_strategies_map.get(rule)
            if not strategy:
                continue
            winner = strategy(board, row, col, playing_piece)
            if winner:
                return winner
        return False
