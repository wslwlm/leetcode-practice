# 题目地址: https://leetcode.com/problems/merge-intervals/
# Runtime: 84 ms Memory Usage: 14.6 MB
# 根据list[0]排序, 然后上界和下界不断更新

class MySolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=lambda s: s[0])
        res = []
        up = intervals[0][1]
        down = intervals[0][0]
        for l in intervals[1:]:             
            if up >= l[0]:                    # 前面元素上界比下一个区间下界大, 说明要合并了
                up = max(up, l[1])
            else:                             # 前面元素上界比下一个区间下界小, 说明要加入res数组中去
                res.append([down, up])
                down = l[0]
                up = l[1]
        res.append([down, up])                # 添加最后一个区间
        return res


# RunTime: 60 ms
# 一样的思路
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        int_l = intervals[0][0]
        int_r = intervals[0][1]
        
        idx = 1
        result = []
        for idx in range(1, len(intervals)):
            if intervals[idx][0] <= int_r:
                if int_r < intervals[idx][1]:
                    int_r = intervals[idx][1]
            else:
                result.append([int_l, int_r])
                int_l = intervals[idx][0]
                int_r = intervals[idx][1]
        result.append([int_l, int_r])
        return result


# RunTime: 64ms
# 先加入outa数组中, 再进行比较修改
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0]<=out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            else: 
                out+=[i]
        return out