from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        num = 0
        for n in nums:
            if n == 1:
                num += 1
            else:
                if num > maximum:
                    maximum = num
                num = 0
        else:
            if num > maximum:
                maximum = num
        return maximum


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 3
