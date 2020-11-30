from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().validUtf8([197, 130, 1]))  # True
    print(Solution().validUtf8([235, 140, 4]))  # False
