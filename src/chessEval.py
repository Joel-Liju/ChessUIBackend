from Chessnut import Game
from stockfish import Stockfish
import json
import os

class ChessGame:
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(ChessGame,cls).__new__(cls)
            config = json.loads(open("./config.json","r").read())
            cls.stockfish = Stockfish(path = config["devWindows"]["stockfileLocation"])
            cls.startNewGame(cls)
        return cls.instance
    def startNewGame(self):
        self.game = Game()
        return self

    def makeAIMove(self):
        # print(self.stockfish.get_best_move())
        self.makeMove(self.stockfish.get_best_move())
    
    def makeMove(self,move):
        self.game.apply_move(move)
        self.stockfish.set_fen_position(self.game)
        # print(self.game)