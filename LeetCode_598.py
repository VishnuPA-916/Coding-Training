class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        for a, b in ops:
            m = min(m, a)
            n = min(n, b)

        return m * n

    