# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/design-tic-tac-toe/

# Time Complexity: O(n)

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.length = n
        self.playerOne = {i: 0 for i in range((2 * n) + 2)}
        self.playerTwo = {i: 0 for i in range((2 * n) + 2)}
        
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
            moves.append(2 * self.length)
        if row == self.length - col -1:
            moves.append((2 * self.length) + 1)
        if player == 1:
            for move in moves:
                if move in self.playerOne:
                    self.playerOne[move] += 1
                    if self.playerOne[move] == self.length:
                        return player
                    if move in self.playerTwo:
                        del self.playerTwo[move]
        else:
            for move in moves:
                if move in self.playerTwo:
                    self.playerTwo[move] += 1
                    if self.playerTwo[move] == self.length:
                        return player
                    if move in self.playerOne:
                        del self.playerOne[move]
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)