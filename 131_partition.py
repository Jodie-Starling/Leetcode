class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if substr == substr[::-1]:   # 判断回文串
                    path.append(substr)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res