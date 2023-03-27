from Chessnut import Game

class ChessGame:


    # def __init__(self) -> None:
        
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(ChessGame,cls).__new__(cls)
            cls.startNewGame(cls)
        return cls.instance
    def startNewGame(self):
        self.game = Game()
        return self
    
    def makeMove(self,move):
        self.game.apply_move(move)
        # print(self.game)