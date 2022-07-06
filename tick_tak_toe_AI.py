import  random

class player:
    def __init__(self, letter):
        #letter is  x or o
        self.letter= letter


        #we want all the player to get their next move given a game
    def get_move(self, game):
        pass
class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square= random.choice(game.available_moves())
        return square

class RandomHumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square= False
        val= None
        while not valid_square:
            square= input(self.letter+ '\'s turn. input move(0-9):')
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square= True
            except ValueError:print('invalid square. try again.')
        return val