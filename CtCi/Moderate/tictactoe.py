# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Tic Tac Win: Design an algorithm to figure out if someone has won a game of tic-tac-toe.
'''

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.length = n
        self.playerone = {i: 0 for i in range((2*n)+2)}
        self.playertwo = {i: 0 for i in range((2*n)+2)}

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        moves = [row, col + self.length]
        if row == col:
            moves.append(2*self.length)
        if row == self.length - col - 1:
            moves.append((2*self.length)+1)
        if player == 1:
            for move in moves:
                if move in self.playerone:
                    self.playerone[move] += 1
                    if self.playerone[move] == self.length:
                        return player
                    if move in self.playertwo:
                        del self.playertwo[move]
        else:
            for move in moves:
                if move in self.playertwo:
                    self.playertwo[move] += 1
                    if self.playertwo[move] == self.length:
                        return player
                    if move in self.playerone:
                        del self.playerone[move]
        return 0
        