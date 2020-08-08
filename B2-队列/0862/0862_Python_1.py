from typing import List


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().shortestSubarray(A=[1], K=1))  # 1
    print(Solution().shortestSubarray(A=[1, 2], K=4))  # -1
    print(Solution().shortestSubarray(A=[2, -1, 2], K=3))  # 3
