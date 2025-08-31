class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L, R = 0, len(nums)
        while L < R:
            M = L + (R - L) // 2
            if target < nums[M]:
                R = M
            elif target > nums[M]:
                L = M+1
            elif target == nums[M]:
                return M
        return -1
#二分法查找
'''
两种，左闭右闭，左闭右开；在区间里找target；一点一点缩小范围；
'''
#注意
'''
方法写进函数里；
return写进循环和函数里；
判断相等用“==”；
'''