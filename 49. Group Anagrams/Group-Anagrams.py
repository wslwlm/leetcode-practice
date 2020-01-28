# 题目地址: https://leetcode.com/problems/group-anagrams/
# Runtime: 100 ms Memory Usage: 15.5 MB
# 字符串内部排序, 然后字典存储同一排序后的值, 再转为列表

class MySolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorts = self.sortString(s)
            if  sorts in res:
                res[sorts].append(s)
            else:
                res[sorts] = [s]
        result = []
        for key in res.keys():
            result.append(res[key])
        return result
                      
    def sortString(self, s):
        return ''.join(sorted(s))


# RunTime: 72ms
# 一样的思路
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #go through list, and count the number of each char per word
        # if that matches another word, append to same list 
        
        result={}
        
        for word in strs:
            s=''.join(sorted(word))
            if s not in result:
                result[s]=[word]
            else:
                result[s].append(word)
        return [result[x] for x in result]