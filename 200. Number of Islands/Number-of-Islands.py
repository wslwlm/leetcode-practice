# 题目地址: https://leetcode.com/problems/number-of-islands/
# Runtime: 132 ms Memory Usage: 14 MB
# 思路: 遇到'1'进行dfs染色, 然后找到下一个1, dfs多少次即为数量

class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])

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

        return count   


# RunTime: 100ms
# 思路: 通过一层一层进行循环填充，
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        name = 2
        islands = set()
        prev = ["0"]*len(grid[0])
        
        for row in grid:
            curr = ["0"]*len(prev)
            found_land = False
            
            # row + ["0"] ==> 避免边界问题
            for idx, i in enumerate(row + ["0"]):
                # 把连续"1"记录下来
                if i == '1' and not found_land:
                    start = idx
                    found_land = True
                elif found_land and i == '0':
                    end = idx
                    # 求出 cur 和 prev中相连接的islands集合, 因为cur中island会使prev中的两个不连通的islands连通
                    # 如果没有connected_islands, islands集合添加
                    # 如果存在连通, 将两个异名islands连通. 
                    connected_islands = set([el for el in prev[start:end] if el != "0"])
                    if len(connected_islands) == 0:
                        curname = str(name)
                        islands.add(curname)
                        name += 1
                    else:
                        curname = None
                        for el in connected_islands:
                            if not curname and el in islands:
                                curname = el
                            elif el in islands:
                                islands.remove(el)
                    for i in range(start,end):
                        curr[i] = curname
                    found_land = False
                    
            prev = curr
                
        return len(islands)


# RunTime: 108ms
# 思路: 比较复杂, 首先是north和west和当前比较, 优先使用north, 如果与west产生冲突的话就进行unionByLabel
from collections import defaultdict
# Beats 99%, but complex

# disjoint-set node
class DsNode:
    def __init__(self):
        self.rank = 0
        self.parent = self

class DisjointSets:
    # DisjointSets Constructors and public methods.
    def __init__(self):
        self._sets = defaultdict(DsNode)

    def find(self, x):
        # path compression
        while x.parent is not x:
            x.parent = x.parent.parent
            x = x.parent
        return x

    def findByLabel(self, label):
        return self.find(self._sets[label])

    def unionByLabel(self, labelA, labelB):
        # union by rank
        a, b = self.find(self._sets[labelA]), self.find(self._sets[labelB])
        if a is not b:
            if a.rank > b.rank:
                b.parent = a
            else:
                a.parent = b
                if a.rank == b.rank:
                    b.rank += 1

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        if rows <= 0 or len(grid[0]) <= 0:
            return 0
        cols = len(grid[0])
        
        ds = DisjointSets()
        labels = [[0] * cols for _ in range(rows)]
        next_label = 1
        
        # Iterate throw all rows and cols
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != '1':
                    continue
                
                # land, check get north and west 
                north, west = row - 1, col - 1
                if north >= 0:
                    # use label of north cell for now
                    labels[row][col] = labels[north][col]
                if west >= 0 and grid[row][west] == '1':
                    if labels[row][col] == 0:
                        # current cell not labeled, use label of west
                        labels[row][col] = labels[row][west]
                    elif labels[row][col] != labels[row][west]:
                        # labels of north and west are different, union the two labels
                        ds.unionByLabel(labels[row][col], labels[row][west])
                if labels[row][col] == 0:
                    # current cell not labeled: must be an isolated cell. Use next label
                    labels[row][col] = next_label
                    next_label += 1
        node_set = set()
        for label in range(1, next_label):
            node_set.add(ds.findByLabel(label))
        return len(node_set)

        return 0
# class Solution:    
#     def numIslands(self, grid):
#         '''128ms, beating 95.56%. 
#         '''
#         def dfs(grid, i, j):
#             if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] !='1':
#                 return
#             grid[i][j] = '#'
#             dfs(grid, i+1, j)
#             dfs(grid, i-1, j)
#             dfs(grid, i, j+1)
#             dfs(grid, i, j-1)
        
        
#         if not grid:
#             return 0
            
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1":
#                     dfs(grid, i, j)
#                     count += 1
#         return count


#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         Beats 136ms, 87.27%
#         """
#         if len(grid) == 0: return 0
#         row = len(grid); col = len(grid[0])
#         self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
#         parent = [i for i in range(row*col)]
        
#         def find(x):
#             if parent[x]!= x:
#                 return find(parent[x])
#             return parent[x]
        
#         def union(x,y):
#             xroot, yroot = find(x),find(y)
#             if xroot == yroot: return 
#             parent[xroot] = yroot
#             self.count -= 1
        
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == '0':
#                     continue
#                 index = i*col + j
#                 if j < col-1 and grid[i][j+1] == '1':
#                     union(index, index+1)
#                 if i < row-1 and grid[i+1][j] == '1':
#                     union(index, index+col)
#         return self.count


# RunTime: 112ms
# 思路: BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 
        
        # def dfs(grid,i,j):
        #     if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
        #         return 
        #     if grid[i][j]=='1': 
        #         grid[i][j]='0'
        #         dfs(grid,i+1,j)
        #         dfs(grid,i-1,j)
        #         dfs(grid,i,j+1)
        #         dfs(grid,i,j-1)
        # count = 0 
        # for i in range(len(grid)): 
        #     for j in range(len(grid[0])): 
        #         if grid[i][j]=='1': 
        #             count +=1
        #             dfs(grid,i,j)
        # return count
        
        # BFS solution
        count =0 
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j]=='1': 
                    count+=1
                    grid[i][j]='0'
                    q = collections.deque()
                    q.append((i,j))
                    while q: 
                        r,c = q.popleft()
                        if r>0 and grid[r-1][c]=='1':
                            q.append((r-1,c))
                            grid[r-1][c]='0'
                        if r+1<len(grid) and grid[r+1][c]=='1': 
                            q.append((r+1,c))
                            grid[r+1][c]='0'
                        if c>0 and grid[r][c-1]=='1':
                            q.append((r,c-1))
                            grid[r][c-1]='0'
                        if c+1<len(grid[0]) and grid[r][c+1]=='1':
                            q.append((r,c+1))
                            grid[r][c+1]='0'
        return count

# RunTime: 120ms
# 思路: DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
######################### Sol 3: DFS(1) ###########################
        icount = 0
        if grid:
            rows = len(grid) 
            cols = len(grid[0])
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == '1': 
                        st = [(r,c)] 
                        while st:
                            (x,y) = st.pop()
                            grid[x][y] = '0'
                            for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
                                xi, yj = x+i, y+j
                                if 0<= xi <rows and 0 <= yj <cols and grid[xi][yj] == '1':
                                    st.append((xi, yj))
                        icount += 1 
        return icount
######################### Sol 2: DFS(2) ###########################
#         icount = 0
#         if grid:
#             rows = len(grid) 
#             cols = len(grid[0])
#             v = set()
#             for r in range(rows):
#                 for c in range(cols):
#                     if grid[r][c] == '1' and (r,c) not in v: 
#                         v.add((r,c))
#                         grid[r][c] = '0'
#                         st = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
#                         while st:
#                             (x,y) = st.pop()
#                             if 0<= x <rows and 0<= y <cols and (x,y) not in v and grid[x][y] == '1': 
#                                 st.extend([(x+1, y),(x-1,y),(x,y+1),(x,y-1)])
#                                 v.add((x,y))
#                         icount += 1 
#         return icount

######################### Sol 3: BFS ###########################
#         if grid:
#             rows = len(grid)
#             cols = len(grid[0])
#             v = set()
#             c = 0
#             for i in range(rows):
#                 for j in range(cols):
#                     if grid[i][j] == '1' and (i,j) not in v:
#                         v.add((i,j))
#                         q = collections.deque([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
#                         while q:
#                             (x,y) = q.popleft()
#                             if 0<= x <rows and 0<= y <cols and (x,y) not in v and grid[x][y] == '1':
#                                 q.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
#                                 v.add((x,y))
#                         c += 1                  
#         return c if grid else 0


# RunTime: 124ms
# 思路: BFS
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
          return 0
        
        num_islands = 0
        for row_idx, row in enumerate(grid):
          for col, el in enumerate(row):
            if el == '1':
              grid[row_idx][col] = '0'
              
              def BFS(x, y):
                q = deque()
                
                q.append((x,y))
                nonlocal grid
                while q:
                  x, y = q.popleft()
                  
                  # Up.
                  if (x - 1) >= 0 and grid[x - 1][y] == '1':
                    grid[x - 1][y] = '0'
                    
                    q.append((x - 1, y))
                  
                  # Down.
                  if (x + 1) < len(grid) and grid[x + 1][y] == '1':
                    grid[x + 1][y] = '0'
                    
                    q.append((x + 1, y))
                   
                  # Right.
                  if (y + 1) < len(grid[0]) and grid[x][y + 1] == '1':
                    grid[x][y + 1] = '0'
                    
                    q.append((x, y + 1))
                    
                  # Left.
                  if (y - 1) >= 0 and grid[x][y - 1] == '1':
                    grid[x][y - 1] = '0'
                    
                    q.append((x, y - 1))
                    
              
              BFS(row_idx, col)
              
              num_islands += 1
              
        return num_islands