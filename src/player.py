from src.piece_type import PieceType


class Player:

    id = 1

    def __init__(self, name):
        self.player_id = Player.id
        Player.id += 1
        self.name = name
        self.playing_piece = None

    def set_playing_piece(self, piece: PieceType):
        self.playing_piece = piece

    def get_player_name(self):
        return self.name

    def get_playing_piece(self):
        return self.playing_piece
