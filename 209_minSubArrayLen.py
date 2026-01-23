# 2525/12/27 二刷

'''
“子数组”默认指的就是连续的一段数组元素。
而“不连续”的则统一称为子序列，它允许元素不连续，但要保持原数组中的相对顺序。
'''

'''
*滑动窗口关键*
双指针 + 单向移动:left 和 right 都只向右移动，从不回退 → 保证 O(n) 时间
窗口的“有效性”条件:current_sum >= target
扩展右边界，收缩左边界:for 扩展 right → while 收缩 left
每当窗口有效时，更新最优解
while 而非 if，尽可能收缩左边界
float('inf') 初始化最小值
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        sum = 0
        left = 0
        n = len(nums)

        for right in range(n):
            sum += nums[right]
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0