import itertools
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        for group in itertools.combinations([i for i in range(1, 10)], k):
            if sum(group) == n:
                ans.append(list(group))
        return ans


if __name__ == "__main__":
    print(Solution().combinationSum3(3, 7))  # [[1,2,4]]
    print(Solution().combinationSum3(3, 9))  # [[1,2,6], [1,3,5], [2,3,4]]
    print(Solution().combinationSum3(3, 15))  # [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
