from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minKBitFlips(A=[0, 1, 0], K=1))  # 2
    print(Solution().minKBitFlips(A=[0, 1, 0], K=1))  # -1
    print(Solution().minKBitFlips(A=[0, 0, 0, 1, 0, 1, 1, 0], K=3))  # 3
