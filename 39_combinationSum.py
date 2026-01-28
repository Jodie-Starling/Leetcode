class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtracking(start, cur_sum):
            if cur_sum == target:
                res.append(path[:])    # 入栈副本

            for i in range(start, len(candidates)):
                if cur_sum + candidates[i] > target:
                    return
                path.append(candidates[i])
                backtracking(i, cur_sum + candidates[i])    # 隐式回溯
                path.pop()

        backtracking(0, 0)
        return res

'''
显式回溯
for i in range(start, len(candidates)):
    if cur_sum + candidates[i] > target:
        return
    path.append(candidates[i])
    cur_sum += candidates[i]
    backtracking(i, cur_sum)    # 隐式回溯
    path.pop()
    cur_sum -= candidates[i]
'''