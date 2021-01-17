class Solution:
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        def get_next(x1, y1):
            res = []
            for (x2, y2) in [(x1 - 2, y1 - 1), (x1 - 2, y1 + 1), (x1 - 1, y1 + 2), (x1 + 1, y1 + 2),
                             (x1 + 2, y1 + 1), (x1 + 2, y1 - 1), (x1 + 1, y1 - 2), (x1 - 1, y1 - 2)]:
                if 0 <= x2 < n and 0 <= y2 < n:
                    res.append((x2, y2))
            return res

        now = [[0] * n for _ in range(n)]
        now[r][c] = 1
        for _ in range(k):
            next = [[0] * n for _ in range(n)]
            for i1 in range(n):
                for j1 in range(n):
                    if now[i1][j1]:
                        for (i2, j2) in get_next(i1, j1):
                            next[i2][j2] += now[i1][j1]
            now = next

        return sum(sum(row) for row in now) / 8 ** k


if __name__ == "__main__":
    print(Solution().knightProbability(3, 2, 0, 0))  # 0.0625
    print(Solution().knightProbability(3, 3, 0, 0))  # 0.01562
