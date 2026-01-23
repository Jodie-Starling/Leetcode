class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        records = {}

        for a in nums1:
            for b in nums2:
                tatal_ab = a + b
                records[tatal_ab] = records.get(tatal_ab, 0) + 1

        count = 0
        for c in nums3:
            for d in nums4:
                need = 0 - c - d
                if need in records:
                    count += records[need]

        return count

# 为什么使用2+2：计算量O(N^2)；1+3：O(N^3)