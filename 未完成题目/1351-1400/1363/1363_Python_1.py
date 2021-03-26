from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        pass


if __name__ == "__main__":
    print(Solution().largestMultipleOfThree([8, 1, 9]))  # 981
    print(Solution().largestMultipleOfThree([8, 6, 7, 1, 0]))  # 8760
    print(Solution().largestMultipleOfThree([1]))  #
    print(Solution().largestMultipleOfThree([0, 0, 0, 0, 0, 0]))  # 0
