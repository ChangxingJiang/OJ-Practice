import collections
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        size = len(A)

        hashmap = collections.Counter()
        for i in range(size):
            for j in range(size):
                hashmap[A[i] + B[j]] += 1

        ans = 0
        for i in range(size):
            for j in range(size):
                ans += hashmap[-C[i] - D[j]]

        return ans


if __name__ == "__main__":
    # 2
    print(Solution().fourSumCount(A=[1, 2],
                                  B=[-2, -1],
                                  C=[-1, 2],
                                  D=[0, 2]))

    # 6
    print(Solution().fourSumCount([-1, -1],
                                  [-1, 1],
                                  [-1, 1],
                                  [1, -1]))
