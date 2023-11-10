from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2
        self.piece_values = {
            "pawn": 1,
            "knight": 3,
            "bishop": 3,
            "rook": 5,
            "queen": 9,
            "king": 0
        }
    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1

        # index = randint(0,len(moves)-1)
        # inner_index =  randint(0,len(moves[index])-1)
        # move = moves[index][inner_index]
        move = self.minMax(self.color, 3)[1]
        self.board.make_move(move,self.color)
        return move
    def minimax(self, color, depth):
        if depth == 0:
            return self.evaluate_board(color), None

        best_score = float('-inf') if player == self.color else float('inf')
        best_move = None

        potential_moves = moves = self.board.get_all_possible_moves(self.color)

        for move in potential_moves:
            for sub_move in move:
                self.board.make_move(sub_move, color)
                cur_color = self.opponent[self.color] if color == self.color else self.color
                temp_score = minimax(cur_color, depth-1, )

                opponent_score, _ = self.minMax(self.opponent[color], depth - 1)

                if (player == self.color and opponent_score > best_score) or \
                        (player == self.opponent[self.color] and opponent_score < best_score):
                    best_score = opponent_score
                    best_move = sub_move

                self.board.undo()
        return best_score, best_move

    def evaluate_board(self, color):
        # A simple evaluation function that counts the material score.
        player_points = 0
        opponent_points = 0

        # evaluate score for the whole board
        for i in range(self.col):
            for j in range(self.rows):
                temp_points = 0
                piece = self.board[i][j]
                temp_points += self.piece_values[str(piece)]

                if color == 1:
                    temp_points += ((self.row - r) / self.row) * 10
                else:
                    temp_points += ((r / self.row) * 10)

                if piece.get_color() == color:
                    player_points += temp_points
                else:
                    opponent_points += temp_points


        return player_points - opponent_points + randint(0,10)


