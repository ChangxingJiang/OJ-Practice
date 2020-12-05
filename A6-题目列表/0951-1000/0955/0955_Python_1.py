from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minDeletionSize(["ca", "bb", "ac"]))  # 1
    print(Solution().minDeletionSize(["xc", "yb", "za"]))  # 0
    print(Solution().minDeletionSize(["zyx", "wvu", "tsr"]))  # 3
