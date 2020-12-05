from typing import List


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().mergeStones(stones=[3, 2, 4, 1], K=2))  # 20
    print(Solution().mergeStones(stones=[3, 2, 4, 1], K=3))  # -1
    print(Solution().mergeStones(stones=[3, 5, 1, 2, 6], K=3))  # 25
