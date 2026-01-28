class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            if len(path) >= 2:
                res.append(path[:])

            uset = set()

            for i in range(start, len(nums)):
                if path and nums[i] < path[-1]:
                    continue
                if nums[i] not in uset:
                    uset.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)
        return res