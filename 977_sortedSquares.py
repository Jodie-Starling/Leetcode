# 2025/12/26二刷

'''
暴力做法：先对每个元素平方 O(n)，再排序 O(n log n)，总时间 O(n log n)。
双指针做法：直接 O(n) 时间得到结果
'''

'''
*用例子直观感受关键点*
nums = [-4, -1, 0, 3, 10]
平方值：  16,  1, 0, 9, 100
两端最大：16 vs 100 → 100    最大 → 先放结果最后一位
剩下两端：16 vs 9   → 16     最大 → 放倒数第二位
剩下两端：1 vs 9    → 9      最大 → 放倒数第三位
剩下两端：1 vs 0    → 1      最大 → 放倒数第四位
剩下：0                         → 放第一位
结果：[0, 1, 9, 16, 100] 完美有序！
整个过程就像在“剥洋葱”：一层层从外往里剥最大的。
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        k = n - 1

        while left <= right:
            l, r = nums[left] ** 2, nums[right] ** 2
            if l < r:
                result[k] = r
                right -= 1
            else:
                result[k] = l
                left += 1
            k -= 1

        return result