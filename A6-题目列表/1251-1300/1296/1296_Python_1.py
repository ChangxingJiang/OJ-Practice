from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4))  # True
    print(Solution().isPossibleDivide(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3))  # True
    print(Solution().isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4))  # True
    print(Solution().isPossibleDivide(nums=[3, 3, 2, 2, 1, 1], k=3))  # False
