class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        res = [0] * len(nums)   # 初始化为0即可，算法会完全填充该数组
        while i >= 0:
            if nums[l] ** 2 > nums[r] ** 2:
                res[i] = nums[l]  ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1
            i -= 1
        return res
    
'''
双指针数组排列法
时间复杂度 O(n)
空间复杂度 O(n)
 res = [float('inf')] * len(nums)   #float('inf') 在 Python 中表示正无穷大，是一个特殊的浮点数值。
 用0填充占用内存少还快；
'''