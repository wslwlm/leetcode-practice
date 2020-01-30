# 题目地址: https://leetcode.com/problems/walking-robot-simulation/
# Runtime: 384 ms Memory Usage: 18.1 MB
# 将障碍存入两个字典中, 通过字典查找, 防止TLE

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        rowdict = {}
        coldict = {}
        directlist = ['n', 'w', 's', 'e']
        direct = 0
        pos = [0, 0]
        dis = 0
        for o in obstacles:
            if o[0] in rowdict:
                rowdict[o[0]].append(o[1])
            else:
                rowdict[o[0]] = [o[1]]
                
            if o[1] in coldict:
                coldict[o[1]].append(o[0])
            else:
                coldict[o[1]] = [o[0]]
        
        for c in commands:
            flag = False
            if c == -2:
                direct = (direct + 1) % 4
            elif c == -1:
                direct = (direct + 3) % 4
            else:
                if direct == 0:
                    if pos[0] in rowdict:
                        for row in rowdict[pos[0]]:
                            if pos[1] < row and pos[1]+c >= row:
                                pos[1] = row - 1
                                flag = True
                    if not flag:
                        pos[1] += c
                elif direct == 2:
                    if pos[0] in rowdict:
                        for row in rowdict[pos[0]]:
                            if pos[1] > row and pos[1]-c <= row:
                                pos[1] = row + 1
                                flag = True
                    if not flag:
                        pos[1] -= c
                elif direct == 3:
                    if pos[1] in coldict:
                        for col in coldict[pos[1]]:
                            if pos[0] < col and pos[0]+c >= col:
                                pos[0] = col - 1
                                flag = True
                    if not flag:
                        pos[0] += c
                else:
                    if pos[1] in coldict:
                        for col in coldict[pos[1]]:
                            if pos[0] > col and pos[0]-c <=col:
                                pos[0] = col + 1
                                flag = True
                    if not flag:
                        pos[0] -= c
            dis = max(dis, pos[0]**2+pos[1]**2)
        return dis


# RunTime: 332ms
# 将obstacles列表通过bisect.insort有序化, 然后bisect.bisect来查找插入位置
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        X, Y = {}, {}
        for x, y in obstacles:
            if x in X:
                bisect.insort(X[x], y)
                
            else:
                X[x] = [y]
            
            if y in Y:
                bisect.insort(Y[y], x)
                
            else:
                Y[y] = [x]
        
        d, x, y, mx = 0, 0, 0, 0
        for z in commands:
            if z == -2:
                d = 3 if d == 0 else d - 1
                
            elif z == -1:
                d = 0 if d == 3 else d + 1
                
            else:
                if d == 0:
                    if x not in X or X[x][-1] <= y:
                        y += z
                        
                    else:
                        i = bisect.bisect(X[x], y)
                        y = y + z if X[x][i] > y + z else X[x][i] - 1
                    
                elif d == 1:
                    if y not in Y or Y[y][-1] <= x:
                        x += z
                        
                    else:
                        i = bisect.bisect(Y[y], x)
                        x = x + z if Y[y][i] > x + z else Y[y][i] - 1
                    
                elif d == 2:
                    if x not in X or X[x][0] >= y:
                        y -= z
                        
                    else:
                        i = bisect.bisect(X[x], y) - 1
                        y = y - z if X[x][i] < y - z else X[x][i] + 1
                    
                else:
                    if y not in Y or Y[y][0] >= x:
                        x -= z
                        
                    else:
                        i = bisect.bisect(Y[y], x) - 1
                        x = x - z if Y[y][i] < x - z else Y[y][i] + 1
                
                mx = max(mx, x ** 2 + y ** 2)
        
        return mx


# RunTime: 340ms
# 单步移动, 然后查看移动过程中坐标是否在obstacles集合中
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        #solution1
        dirX = [0, 1, 0, -1]    #N-E-S-W
        dirY = [1, 0, -1, 0]
        d = 0           # start facing North
        (x,y) = (0,0)   # start from origin
        obstacleSet = set(map(tuple, obstacles))    # convert to hashmap to improve performance
        ans = 0

        for command in commands:
            if (command == -1): d = (d+1)%4
            elif (command == -2): d = (d-1)%4
            else:
                for i in range(command):
                    newPos = (x+dirX[d], y+dirY[d])
                    if (newPos in obstacleSet): break
                    else: x,y = newPos
                ans = max(ans, x*x+y*y)
        return ans