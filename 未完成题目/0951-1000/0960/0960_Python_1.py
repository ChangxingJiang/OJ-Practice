from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minDeletionSize(["babca", "bbazb"]))  # 3
    print(Solution().minDeletionSize(["edcba"]))  # 4
    print(Solution().minDeletionSize(["ghi", "def", "abc"]))  # 0
