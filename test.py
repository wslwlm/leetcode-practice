class Node:
    def __init__(self, pos, c, l, path):
        self.pos = pos
        self.c = c
        self.l = l
        self.path = path

class Solution:
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start = (i, j)
                    if self.helper(board, start, word, m, n):
                        return True
        return False
                    
    def helper(self, board, start, word, m, n):
        stack = []
        s = Node(start, word[0], 1, [start])
        stack.append(s)
        while stack:
            node = stack.pop()
            pos = node.pos
            l = node.l
            path = node.path

            if l == len(word):
                return True
            for d in self.direction:
                new_x = pos[0] + d[0]
                new_y = pos[1] + d[1]
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and \
                    board[new_x][new_y]== word[l] and (new_x, new_y) not in path:
                    new_pos = (new_x, new_y)
                    new_path = path + [new_pos]
                    new_node = Node(new_pos, board[new_x][new_y], l+1, new_path)
                    stack.append(new_node) 
            print(stack)        
        return False

board = [["b"],["a"],["b"],["b"],["a"]]
word = "baa"
print(Solution().exist(board, word))