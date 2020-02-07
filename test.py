class Solution:
    def numIslands(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        k = 2

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return 

            grid[i][j] = '2'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        for i in range(m):
            print(grid[i])

        return count    
        




s = [["1","1","1","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","1","0"],
    ["0","1","0","0","1"]]
print(Solution().numIslands(s))