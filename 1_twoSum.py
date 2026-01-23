class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, num in enumerate(nums):  # 遍历列表的高效方式，同时获取index和val
            need = target - num
            if need in records:
                return [records[need], index]
            records[num] = index

        return []