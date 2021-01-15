from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.n = 0

    def lexicalOrder(self, n: int) -> List[int]:
        self.n = n

        for i in range(1, 10):
            self.dfs(i)

        return self.ans

    def dfs(self, i):
        if i <= self.n:
            self.ans.append(i)
            for j in range(0, 10):
                self.dfs(i * 10 + j)


if __name__ == "__main__":
    # [1,10,11,12,13,2,3,4,5,6,7,8,9]
    print(Solution().lexicalOrder(13))
