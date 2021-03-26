from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minimum = len(nums) - 1
        maximum = 0
        sorts = sorted(nums)
        for i in range(len(nums)):
            if sorts[i] != nums[i]:
                minimum = min(minimum, i)
                maximum = max(maximum, i)

        return maximum - minimum + 1 if minimum < maximum else 0


if __name__ == "__main__":
    print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # 5
    print(Solution().findUnsortedSubarray([2, 1]))  # 2
    print(Solution().findUnsortedSubarray([3, 2, 3, 2, 4]))  # 4
    print(Solution().findUnsortedSubarray([2, 3, 3, 2, 4]))  # 3
    print(Solution().findUnsortedSubarray([1, 2, 3, 3, 3]))  # 0
    print(Solution().findUnsortedSubarray([1, 2, 4, 5, 3]))  # 3
    print(Solution().findUnsortedSubarray([1, 3, 5, 2, 4]))  # 4
    print(Solution().findUnsortedSubarray([1]))  # 0
