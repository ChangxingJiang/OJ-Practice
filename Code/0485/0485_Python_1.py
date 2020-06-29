from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = "".join([str(n) for n in nums])
        return max([len(n) for n in s.split("0")])


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 3
