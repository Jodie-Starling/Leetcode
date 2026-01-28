class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []

        def backtrack(start):
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return

            for length in range(1, 4):
                if start + length > len(s): # 这里的和len(s)相等的边界是取不到的，应该用=
                    return
                segment = s[start:start + length]
                if len(segment) > 1 and segment.startswith('0') or int(segment) > 255:
                    return
                path.append(segment)
                backtrack(start + length)
                path.pop()

        backtrack(0)
        return res