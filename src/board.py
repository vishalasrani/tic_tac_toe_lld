from src.cell import Cell


class Board:

    def __init__(self, board_size: int):
        self.board_size = board_size
        self.cells = []
        self.initilize_cells(board_size)

    def initilize_cells(self, board_size: int):
        for row in range(board_size):
            self.cells.append([])
            for col in range(board_size):
                self.cells[row].append(Cell())

    def print_board(self):
        for row in range(self.board_size):
            print("|", end="")
            for col in range(self.board_size):
                cell_value = self.cells[row][col].get_cell_piece()
                if cell_value is None:
                    print("   ", end="")
                else:
                    print(" %s " % cell_value, end="")
                print("|", end="")
            print()

    def check_free_cells(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                cell_value = self.cells[row][col].get_cell_piece()
                if not cell_value:
                    return True
        return False

    def add_piece(self, row, col, piece):
        error = self.validate_input(row, col)
        if error:
            return error
        row = int(row)
        col = int(col)
        current_cell_value = self.cells[row][col].get_cell_piece()
        if current_cell_value is not None:
            return "This cell is already occupied. Please try again."
        self.cells[row][col].set_cell_piece(piece)

    def validate_input(self, row, col):
        if not (row.isnumeric() and 0 <= int(row) < self.board_size):
            return "Row must be numeric in the range 0-%s" % (self.board_size - 1)
        if not (col.isnumeric() and 0 <= int(col) < self.board_size):
            return "Column must be numeric in the range 0-%s" % (self.board_size - 1)
        return None

    def get_cell_value(self, row, col):
        return self.cells[row][col].get_cell_piece()

    def get_board_size(self):
        return self.board_size
