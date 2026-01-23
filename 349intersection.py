# 面试展示逻辑
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = set(nums1)
        result = set()

        for num in nums2:
            if num in nums:
                result.add(num)

        return list(result)

# 实际工作中用
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))   # &是列表求交集的符号