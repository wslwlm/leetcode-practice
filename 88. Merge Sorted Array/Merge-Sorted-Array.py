# 从前往后 merge, 创建了新的列表
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_c = nums1[:]
        p1 = 0
        p2 = 0
        k = 0
        while p1 < m and p2 < n:
            if nums1_c[p1] < nums2[p2]:
                nums1[k] = nums1_c[p1]
                p1 += 1
            else:
                nums1[k] = nums2[p2]
                p2 += 1
            k+=1
        if p1 == m:
            for i in nums2[p2:n]:
                nums1[k] = i
                k+=1
        else:
            for i in nums1_c[p1:m]:
                nums1[k] = i
                k+=1
        return nums1


# 从后往前 merge则不用创建一个新数组, 
class githubSolution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 整体思路相似，只不过没有使用 current 指针记录当前填补位置
        while m > 0 and n > 0:
            if nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -=1
        """
        由于没有使用 current，第一步比较结束后有两种情况:
            1. 指针 m>0，n=0，此时不需要做任何处理
            2. 指针 n>0，m=0，此时需要将 nums2 指针左侧元素全部拷贝到 nums1 的前 n 位
        """
        if n > 0:
            nums1[:n] = nums2[:n]