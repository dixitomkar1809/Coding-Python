# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/design-snake-game/

# Time Complexity: O(1)

import collections

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.height = height
        self.width = width
        self.food = food
        self.foodIndex = 0
        self.snake = collections.deque([(0, 0)])
        self.snakeLocations = {(0, 0): 1}
        self.directionMoves = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        newHead = (self.snake[0][0] + self.directionMoves[direction][0], 
                   self.snake[0][1] + self.directionMoves[direction][1])
        bitesItself = newHead in self.snakeLocations and newHead != self.snake[-1]
        if newHead[0] < 0 or newHead[0] >= self.height or newHead[1] < 0 or newHead[1] >= self.width or bitesItself:
            return -1
        nextFoodItem = self.food[self.foodIndex] if self.foodIndex < len(self.food) else None
        if self.foodIndex < len(self.food) and nextFoodItem[0] == newHead[0] and nextFoodItem[1] == newHead[1]:
            self.foodIndex += 1
        else:
            tail = self.snake.pop()
            del self.snakeLocations[tail]
        self.snake.appendleft(newHead)
        self.snakeLocations[newHead] = 1
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)




# class SnakeGame(object):

#     def __init__(self, width, height, food):
#         """
#         Initialize your data structure here.
#         @param width - screen width
#         @param height - screen height 
#         @param food - A list of food positions
#         E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
#         :type width: int
#         :type height: int
#         :type food: List[List[int]]
#         """
#         self.grid = [['' for _ in range(width)] for _ in range(height)]
#         self.food = collections.deque(food)
#         self.snake = collections.deque([[0, 0]])
#         foodItem = self.food.popleft()
#         self.grid[foodItem[0]][foodItem[1]] = 'F'
#         self.grid[0][0] = 'S'

#     def move(self, direction):
#         """
#         Moves the snake.
#         @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
#         @return The game's score after the move. Return -1 if game over. 
#         Game over when snake crosses the screen boundary or bites its body.
#         :type direction: str
#         :rtype: int
#         """
#         valid, newPosition = self.isValid(direction)
#         if not valid:
#             return -1
#         if self.grid[newPosition[0]][newPosition[1]] == '':
#             snakeTail = self.snake.popleft()
#             self.grid[snakeTail[0]][snakeTail[1]] = ''
#             self.snake.append(newPosition)
#             self.grid[newPosition[0]][newPosition[1]] = 'S'
#         elif self.grid[newPosition[0]][newPosition[1]] == 'F':
#             self.grid[newPosition[0]][newPosition[1]] = 'S'
#             self.snake.append(newPosition)
#             if len(self.food) > 0:
#                 foodItem = self.food.popleft()
#                 self.grid[foodItem[0]][foodItem[1]] = 'F'
#         return len(self.snake)-1
        
    
#     def isValid(self, direction):
#         currPosition = self.snake[-1]
#         newPosition = [float('inf'), float('inf')]
#         if direction == 'U':
#             newPosition = [currPosition[0] - 1, currPosition[1]]
#         elif direction == 'R':
#             newPosition = [currPosition[0], currPosition[1] + 1]
#         elif direction == 'L':
#             newPosition = [currPosition[0], currPosition[1] - 1]
#         else:
#             newPosition = [currPosition[0] + 1, currPosition[1]]
#         # print(newPosition, self.grid, self.snake)
#         if newPosition[0] >= 0 and newPosition[0] < len(self.grid) and newPosition[1] >= 0 and newPosition[1] < len(self.grid[0]):
#             if (self.grid[newPosition[0]][newPosition[1]] == 'S') and (newPosition != self.snake[0]):
#                 return (False, newPosition)
#             return (True, newPosition)
        
#         return (False, newPosition)
            
# # Your SnakeGame object will be instantiated and called as such:
# # obj = SnakeGame(width, height, food)
# # param_1 = obj.move(direction)