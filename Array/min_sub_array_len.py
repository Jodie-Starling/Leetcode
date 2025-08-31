class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        min_len = float('inf')
        sum = 0
        while r < len(nums):
            sum += nums[r]
            while sum >= target:
                min_len = min(min_len, r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1
        return min_len if min_len != float('inf') else 0
''' 
滑动窗口
在没有达到时，右指针向右移动，增加窗口大小
在达到或超过时，左指针向右移动，缩小窗口大小
返回最小长度
如果没有满足条件的子数组，返回0
时间复杂度O(n)
空间复杂度O(1)
'''