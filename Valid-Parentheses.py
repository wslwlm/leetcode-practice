class Solution:
    def isValid(self, s: str) -> bool:
        dictS = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        signList = []
        for s1 in s:
            if signList and signList[-1] in dictS and dictS[signList[-1]] == s1:
                signList.pop()
            else:
                signList.append(s1)
        if not signList:
            return True
        else:
            return False