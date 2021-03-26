from typing import List


class Solution:
    def __init__(self):
        self.lst = [[-1] * (2 ** i) for i in range(4)]

    def pathSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        for num in nums:
            a, b, c = num // 100 - 1, num % 100 // 10 - 1, num % 10
            self.lst[a][b] = c

        return self.dfs(0, 0, 0)

    def dfs(self, now, a, b):
        v = self.lst[a][b]
        if a == 3:
            return now + v
        elif self.lst[a + 1][b * 2] != -1 and self.lst[a + 1][b * 2 + 1] != -1:
            return self.dfs(now + v, a + 1, b * 2) + self.dfs(now + v, a + 1, b * 2 + 1)
        elif self.lst[a + 1][b * 2] != -1:
            return self.dfs(now + v, a + 1, b * 2)
        elif self.lst[a + 1][b * 2 + 1] != -1:
            return self.dfs(now + v, a + 1, b * 2 + 1)
        else:
            return now + v


if __name__ == "__main__":
    print(Solution().pathSum([113, 215, 221]))  # 12
    print(Solution().pathSum([113, 221]))  # 4
