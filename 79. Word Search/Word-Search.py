# 题目地址: https://leetcode.com/problems/word-search/
# Runtime: 492 ms Memory Usage: 13.3 MB
# 找到开头, 然后用栈来走字符串, 标记'*'表示路径被走过, 回溯时需要清除

class MySolution:
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def exist(self, board: List[List[str]], word: str) -> bool:
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
        path = []
        stack.append((start, word[0], 1))
        path.append((start, word[0], 1))
        board[start[0]][start[1]] = '*'
        while stack:
            flag = False
            pos, char, l = stack.pop()
            board[pos[0]][pos[1]] = '*'
            if l == len(word):
                return True
            for d in self.direction:
                if pos[0] + d[0] >= 0 and pos[0] + d[0] < m and \
                    pos[1] + d[1] >= 0 and pos[1] + d[1] < n and \
                    board[pos[0] + d[0]][pos[1] + d[1]]== word[l]:
                    
                    next_pos = (pos[0]+d[0], pos[1]+d[1])
                    stack.append((next_pos, board[next_pos[0]][next_pos[1]], l+1))
                    path.append((next_pos, board[next_pos[0]][next_pos[1]], l+1))
                    flag = True
            if not flag:
                while path:
                    p, c, l= path.pop()
                    if board[p[0]][p[1]] == '*':
                        board[p[0]][p[1]] = c
                    else:
                        path.append((p, c, l))
                        break
        if path:
            p, c, _= path.pop()
            board[p[0]][p[1]] = c
        return False


# Runtime: 504 ms Memory Usage: 17 MB
# 用列表存储走过的路径
class Node:
    def __init__(self, pos, c, l, path):
        self.pos = pos
        self.c = c
        self.l = l
        self.path = path

class MySolution:
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
        return False


# RunTime: 144ms
from collections import Counter
class Solution:
    def exist0(self, board: List[List[str]], word: str) -> bool:
        
        dx = [0, -1, 1, 0, 0]
        dy = [0, 0, 0, -1, 1]
        
        def search(board, word, row, col, visited):
            if word == "":
                return True
            
            if board[row][col] != word[0]:
                return False

            for delx, dely in zip(dx, dy):
                nextRow = row + delx
                nextCol = col + dely
                if 0 <= nextRow < len(board) and 0 <= nextCol < len(board[0]) and \
                   visited[row][col] == False:
                    if board[row][col] == word[0]:
                        visited[row][col] = True
                        tmp = search(board, word[1:], nextRow, nextCol, visited)
                        if tmp == True:
                            return tmp
                        else:
                            visited[row][col] = False
            return False
        
        h = len(board)
        w = len(board[0])
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        return any(search(board, word, i, j, visited) for i in range(h) for j in range(w)) # 有一个为True则为True
    
    
    def exist1(self, board: List[List[str]], word: str) -> bool: 
        dx = [0, -1, 1, 0, 0]
        dy = [0, 0, 0, -1, 1]
        
        def search(board, word, row, col, visited):
            if word == "":
                return True
            
            if board[row][col] != word[0]:
                return False

            for delx, dely in zip(dx, dy):
                nextRow = row + delx
                nextCol = col + dely
                if 0 <= nextRow < len(board) and 0 <= nextCol < len(board[0]) and \
                   visited[row][col] == False:
                    if board[row][col] == word[0]:
                        visited[row][col] = True
                        tmp = search(board, word[1:], nextRow, nextCol, visited)
                        if tmp == True:
                            return tmp
                        else:
                            visited[row][col] = False
            return False
        
        h = len(board)
        w = len(board[0])
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for r in range(h):
            for c in range(w):
                if search(board, word, r, c, visited):
                    return True
        return False
    
    def exist2(self, board: List[List[str]], word: str) -> bool: 
        dx = [0, -1, 1, 0, 0]
        dy = [0, 0, 0, -1, 1]
        
        visited = set()
        def search(board, word, row, col, visited):
            if word == "":
                return True
            
            if board[row][col] != word[0]:
                return False

            for delx, dely in zip(dx, dy):
                nextRow = row + delx
                nextCol = col + dely
                if 0 <= nextRow < len(board) and 0 <= nextCol < len(board[0]) and \
                (row, col) not in visited:
                    if board[row][col] == word[0]:
                        visited.add((row, col))
                        tmp = search(board, word[1:], nextRow, nextCol, visited)
                        if tmp == True:
                            return tmp
                        else:
                            visited.remove((row, col))
            return False
        
        h = len(board)
        w = len(board[0])
        
        for r in range(h):
            for c in range(w):
                if search(board, word, r, c, visited):
                    return True
        return False
    
    def exist(self, A, word):
        if Counter(word) - Counter(c for row in A for c in row): return False
        rows, cols, N = len(A), len(A[0]), len(word)
        def dfs(r, c, d):
            if word[d] == A[r][c]:
                A[r][c] += '!'
                found = ((d + 1 == N) or
                         (r+1 < rows and dfs(r+1, c, d+1)) or
                         (c+1 < cols and dfs(r, c+1, d+1)) or
                         (r-1 >= 0 and dfs(r-1, c, d+1)) or
                         (c-1 >= 0 and dfs(r, c-1, d+1)))
                A[r][c] = A[r][c][0]
                return found
            return False
        for r in range(rows):
            for c in range(cols):
                if A[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False


# RunTime: 324ms
# 递归解决路径问题, 回溯时清除'*'
# Scan board, find starting position with matching word first letter
# From starting position, DFS (4 (up, down, left, right 4 directions) match word's rest letters
# For each visited letter, mark it as visited, here use board[i][j] = '*' to represent visited.
# If one direction cannot continue, backtracking, mark start position unvisited, mark board[i][j] = word[start]
# If found any matching, terminate
# Otherwise, no matching found, return false.
# 具体参见 https://github.com/azl397985856/leetcode/blob/master/problems/79.word-search-en.md
class githubSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def dfs(board, r, c, word, index):
            if index == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False
            board[r][c] = '*'
            res = dfs(board, r - 1, c, word, index + 1) or dfs(board, r + 1, c, word, index + 1) or dfs(board, r, c - 1, word, index + 1) or dfs(board, r, c + 1, word, index + 1)
            board[r][c] = word[index]
            return res
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(board, r, c, word, 0):
                        return True