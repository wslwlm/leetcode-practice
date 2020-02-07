# 题目地址: https://leetcode.com/problems/surrounded-regions/
# Runtime: 2620 ms Memory Usage: 13.5 MB
# 思路: 其实这不是dp问题, 有点瞎做, 因为从上到下, 从左到右过程中会有不确定量
# 也就是状态无法确定, 所以要进行多次遍历, 时间复杂度过大


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        m = len(board)
        n = len(board[0])

        dp = [[0] * n for i in range(m)]

        for i in range(n):
            dp[0][i] = True if board[0][i] == 'O' else False
            dp[m-1][i] = True if board[m-1][i] == 'O' else False

        for i in range(m):
            dp[i][0] = True if board[i][0] == 'O' else False
            dp[i][n-1] = True if board[i][n-1] == 'O' else False

        for k in range(m):
            for i in range(1, m-1):
                for j in range(1, n-1):
                    if board[i][j] == 'O':
                        dp[i][j] = dp[i-1][j] or dp[i+1][j] or dp[i][j-1] or dp[i][j+1]
                    else:
                        dp[i][j] = False

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    if not dp[i][j]:
                        board[i][j] = 'X'


# 思路: 递归从边界进入, 然后标记为A, 没有被标记的则为未与边界连通.
# 我刚开始也用了dfs, 不过是对每一个O进行dfs, 会导致TLE的问题.
class githubSolution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 如果数组长或宽小于等于2，则不需要替换
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        
        row, col = len(board), len(board[0])
        
        def dfs(i, j):
            """
            深度优先算法，如果符合条件，替换为A并进一步测试，否则停止
            """
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            board[i][j] = 'A'
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        # 从外围开始
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
        
        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)
        
        # 最后完成替换
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'   


# RunTime: 140ms
# 思路: 用queue实现dfs的功能, 先将边界O入队, 然后再依次将相邻入队
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])
        queue = []
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][n - 1] == 'O':    
                queue.append((i, n - 1))
        for j in range(n):        
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[m - 1][j]  == 'O':   
                queue.append((m - 1, j))
        border = [[False] * n for _ in range(m)]
        while len(queue) > 0:
            i, j = queue.pop(0)
            if border[i][j]:
                continue
            border[i][j] = True    
            if i > 0 and board[i - 1][j] == 'O':
                queue.append((i - 1, j))
            if i < m - 1 and board[i + 1][j] == 'O':    
                queue.append((i + 1, j))
            if j > 0 and board[i][j - 1] == 'O':    
                queue.append((i, j - 1))
            if j < n - 1 and board[i][j + 1] == 'O':
                queue.append((i, j + 1))
        for i in range(m):
            for j in range(n):
                if not border[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'  


# RunTime: 144ms
# 思路: 类似上面
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.pop(0)
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r-1, c)); queue.append((r+1, c))
                queue.append((r, c-1)); queue.append((r, c+1))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"                  