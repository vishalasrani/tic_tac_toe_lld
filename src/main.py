from src.player import Player
from src.game import Game


def main():
    p1 = Player("abc")
    p2 = Player("xyz")
    game = Game(p1, p2)
    game.start_game()

main()