# 2025/12/26 二刷
# 二分法

'''
如果使用简单的线性搜索（从头到尾逐个检查），最坏情况下需要检查数组中的所有元素，时间复杂度为 O(n)（n 是数组长度）。
而二分查找每次将搜索范围缩小一半，时间复杂度仅为 O(log n).
'''

'''
*控制边界*
循环条件：left <= right（闭区间才有意义）
大于目标：right = mid - 1（排除当前 mid）
小于目标：left = mid + 1（排除当前 mid）
等于目标：直接返回 mid
计算 mid：用 left + (right - left) // 2 防溢出
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1  # 这里赋值不能"left = 0, right = len(nums) - 1"

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1