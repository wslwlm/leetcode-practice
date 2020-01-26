# 题目地址: https://leetcode.com/problems/container-with-most-water/
# Runtime: 108 ms Memory Usage: 14.5 MB
# 两个指针, 分别指向列表头尾, 根据木桶盛水由短板决定, 将短板的指针进行移动, 直到出现比短板高的木板, 比较储水量.

class MySolution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxWater = 0
        lastMin = 0
        while start < end:
            curMin = 0
            if height[start] < height[end]:
                curMin = height[start]
                start += 1
            else:
                curMin = height[end]
                end -= 1
            if curMin < lastMin:
                continue
            curWater = curMin * (end - start + 1)
            if curWater > maxWater:
                maxWater = curWater
            lastMin = curMin
        return maxWater


# RunTime: 108ms
# 一样的思路
class bestSolution:
    def maxArea(self, height: List[int]) -> int:
        x1 = 0
        x2 = len(height)-1
        current_max=0
        top_height = max(height)
        while (x2 - x1)*top_height > current_max:
            current_max=max(current_max, min(height[x1],height[x2])*(x2-x1))
            if height[x1] < height[x2]:
                x1 += 1
            else:
                x2 -= 1
        return(current_max)