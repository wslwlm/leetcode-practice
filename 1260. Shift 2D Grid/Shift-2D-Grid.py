# 题目地址: https://leetcode.com/problems/shift-2d-grid/
# Runtime: 388 ms Memory Usage: 12.6 MB
# 经过 m*n 次变换 --> 变回原样 --> 行列转换

class MySolution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        if k % (m*n) == 0:
            return grid
        
        k = k % (m*n)
        
        d, l = divmod(k, n)
        
        tmp_grid = copy.deepcopy(grid)
        
        for i in range(m):
            indr = (i+d)%m
            for j in range(n):
                ind = (j+l)%n
                if j < n-l:
                    grid[indr][ind] = tmp_grid[i][j]
                else:
                    grid[(indr+1)%m][ind] = tmp_grid[i][j]
        return grid


# 二维到一维, 然后进行循环移位
# 循环移位算法, 参考链接:
# https://lucifer.ren/blog/2019/12/11/rotate-list/
class githubSolution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        # 二维到一维
        arr = [grid[i][j] for i in range(n) for j in range(m)]
        # 取模，缩小k的范围，避免无意义的运算
        k %= m * n
        res = []
        # 首尾交换法

        def reverse(l, r):
            while l < r:
                t = arr[l]
                arr[l] = arr[r]
                arr[r] = t
                l += 1
                r -= 1
        # 三次旋转
        reverse(0, m * n - k - 1)
        reverse(m * n - k, m * n - 1)
        reverse(0, m * n - 1)
        # 一维到二维
        row = []
        for i in range(m * n):
            if i > 0 and i % m == 0:
                res.append(row)
                row = []
            row.append(arr[i])
        res.append(row)

        return res


# RunTime: 144 ms
# 类似github的思路 
class bestSolution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        row = len(grid)
        col = len(grid[0])
        n = row * col
        
        for row in grid:
            ans += row
        
        stack = []
        if k > n:
            k = k % n
        
        ans = ans[-k:] + ans[:-k]
        
        res = []
        
        for i in range(0, n, col):
            res.append(ans[i:i+col])
        return res