class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(n, k, start):
            if len(path) == k:
                res.append(path[:])    # **创建副本，否则后面pop()执行后path改变，这里加入到res的部分也会改变**
                return

            need = k - len(path)
            end_idx = n - need + 1   # 剪枝优化版

            for i in range(start, end_idx + 1):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop()

        backtracking(n, k, 1)
        return res