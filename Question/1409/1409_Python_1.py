from typing import List


class BIT:
    def __init__(self, n):
        self.n = n
        self.a = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.a[x]
            x -= BIT.lowbit(x)
        return ret

    def update(self, x, dt):
        while x <= self.n:
            self.a[x] += dt
            x += BIT.lowbit(x)


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        size = len(queries)

        bit = BIT(m + size)

        pos = [0] * (m + 1)
        for i in range(1, m + 1):
            pos[i] = size + i
            bit.update(size + i, 1)

        ans = []
        for i, q in enumerate(queries):
            idx = pos[q]
            bit.update(idx, -1)
            ans.append(bit.query(idx))
            idx = pos[q] = size - i
            bit.update(idx, 1)
        return ans


if __name__ == "__main__":
    print(Solution().processQueries(queries=[3, 1, 2, 1], m=5))  # [2,1,2,1]
    print(Solution().processQueries(queries=[4, 1, 2, 2], m=4))  # [3,1,2,0]
    print(Solution().processQueries(queries=[7, 5, 5, 8, 3], m=8))  # [6,5,0,7,5]
