class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(start, cur_sum):
            if cur_sum == target:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:  # 每个数字只能出现一次
                    continue
                if cur_sum + candidates[i] > target:
                    return
                path.append(candidates[i])
                backtrack(i + 1, cur_sum + candidates[i])
                path.pop()

        backtrack(0, 0)
        return res