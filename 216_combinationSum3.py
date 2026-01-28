class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(n, k, start, cur_sum):
            if cur_sum > n:
                return

            if len(path) == k:
                if cur_sum == n:
                    res.append(list(path)) # **创建副本**
                return    # 已经选够k个该return了

            need = k - len(path)
            end_idx = 9 - need + 1   # 剪枝优化版

            for i in range(start, end_idx + 1):
                path.append(i)
                cur_sum += i
                backtracking(n, k, i + 1, cur_sum)
                path.pop()
                cur_sum -= i

        backtracking(n, k, 1, 0)
        return res