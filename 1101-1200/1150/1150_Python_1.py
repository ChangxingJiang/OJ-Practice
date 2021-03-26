from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        num = 0
        for n in nums:
            if n != target:
                num -= 1
            else:
                num += 1

        return num > 0


if __name__ == "__main__":
    print(Solution().isMajorityElement(nums=[2, 4, 5, 5, 5, 5, 5, 6, 6], target=5))  # True
    print(Solution().isMajorityElement(nums=[10, 100, 101, 101], target=101))  # False
