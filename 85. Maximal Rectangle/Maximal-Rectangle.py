# 题目地址: https://leetcode.com/problems/maximal-rectangle/
# Runtime: 1676 ms Memory Usage: 13.8 MB
# 思路: 

class MySolution:
    def maximalRectangle(self, matrix) -> int:
        if (not matrix) or (not matrix[0]):
            return 0
        m = len(matrix)
        n = len(matrix[0])

        widths = [0] * m
        maxS = 0

        for j in range(n):
            for i in range(m):
                if matrix[i][j] == '1':
                    widths[i] += 1
                else:
                    widths[i] = 0
            
            for w in range(j+1):
                continuous_k = 0
                minW = float('inf')
                for i in range(m):
                    if widths[i] > w:
                        continuous_k += 1
                        minW = min(widths[i], minW)
                        maxS = max(minW * continuous_k, maxS)
                    else:
                        minW = float('inf')
                        continuous_k = 0
        return maxS


# RunTime: 148ms
# 思路: 
class Solution1:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: 
            return 0
        nums = [int("".join(row), base = 2) for row in matrix]
        ans = 0
        for i in range(len(nums)):
            cur = -1
            for j in range(i, len(nums)):
                cur &= nums[j]
                if cur == 0:
                    break
                cnt = 0
                tmp = cur
                while tmp:
                    cnt += 1
                    tmp &= tmp >> 1
                area = cnt * (j - i + 1)
                if area > ans: ans = area
        return ans


# RunTime: 180 ms
class Solution2:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        You can maintain a row length of Integer array height recorded its height of '1's, and scan and update row by row to find out the largest rectangle of each row.

For each row, if matrix[row][i] == '1'. height[i] +=1, or reset the height[i] to zero.
and accroding the algorithm of [Largest Rectangle in Histogram], to update the maximum area.
        '''
        
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n+1)
        ans = 0
        
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n+1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
        return ans


# RunTime: 196ms
# 思路: 
class Solution3:
    def maximalRectangle(self, A):
        def findLargestRectangle(height):
            # print(height, n)
            stack = [-1]
            for i in range(n+1):
                while height[i]<height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i-stack[-1]-1
                    self.res = max(self.res, w*h)
                stack.append(i)

        if not A or len(A)==0 or len(A[0])==0: return 0
        m, n = len(A), len(A[0])
        height = [0]*(n+1)
        self.res = 0
        for i in range(m):
            for j in range(n):
                height[j] = (height[j]+1 if A[i][j]=="1" else 0)
            findLargestRectangle(height)
        return self.res


# RunTime: 204 ms
# 思路: 
class Solution4:
    
    def largestHistRectangle(self, hist):
        if not hist:
            return 0
        max_area = 0
        stack = [(0, hist[0])]
        for i in range(1, len(hist)):
            if hist[i] <= stack[-1][1]:
                while stack and hist[i] <= stack[-1][1]:
                    j, h = stack.pop()
                    max_area = max(max_area, (i - j) * h)
                stack.append((j, hist[i]))
            else:
                stack.append((i, hist[i]))
        while stack:
            j, h = stack.pop()
            max_area = max(max_area, (len(hist) - j) * h)
        return max_area
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        heights_matrix = [[int(v) for v in matrix[0]]]
        for i in range(1, len(matrix)):
            heights = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == "1":
                    heights.append(1 + heights_matrix[-1][j])
                else:
                    heights.append(0)
            heights_matrix.append(heights)
        max_area = 0
        for heights in heights_matrix:
            max_area = max(max_area, self.largestHistRectangle(heights))
        return max_area