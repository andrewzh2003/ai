from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():

    def __init__(self, col, row, p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col, row, p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1: 2, 2: 1}
        self.color = 2

    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1

        # index = randint(0,len(moves)-1)
        # inner_index =  randint(0,len(moves[index])-1)
        # move = moves[index][inner_index]
        moves = self.board.get_all_possible_moves(self.color)
        best_move = moves[0][0]
        move = self.minMax(self.color, 3, best_move, float('-inf'), float('inf'))[1]
        self.board.make_move(move,self.color)
        return move
    def minMax(self, color, depth, best_move, alpha, beta) :
        if depth == 0:
            return self.evaluate_board(color), best_move

        potential_moves = self.board.get_all_possible_moves(color)
        best_score = float('-inf') if color == self.color else float('inf')

        for move in potential_moves:
            for sub_move in move:
                self.board.make_move(sub_move, color)

                if color == self.color:
                    temp_score = self.minMax(self.opponent[self.color], depth - 1, best_move, alpha, beta)[0]
                    if temp_score > best_score:
                        best_score = temp_score
                        best_move = sub_move
                        alpha = max(alpha, best_score)
                elif color == self.opponent[self.color]:
                    temp_score = self.minMax(self.color, depth - 1, best_move, alpha, beta)[0]
                    if temp_score < best_score:
                        best_score = temp_score
                        best_move = sub_move
                        beta = min(beta, best_score)

                self.board.undo()

        return best_score, best_move

    def evaluate_board(self, color):
        # A simple evaluation function that counts the material score.
        player_points = 0
        opponent_points = 0

        # evaluate score for the whole board
        for i in range(self.col):
            for j in range(self.row):
                temp_points = 0
                piece = self.board.board[i][j]
                if piece.is_king == True:
                    temp_points += 10
                else:
                    temp_points += 5

                if color == 1:
                    temp_points += ((self.row - j) / self.row) * 10
                else:
                    temp_points += ((j / self.row) * 10)

                if piece.get_color() == color:
                    player_points += temp_points
                else:
                    opponent_points += temp_points


        return player_points - opponent_points + randint(0,10)
