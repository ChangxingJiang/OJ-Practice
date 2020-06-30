from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        reverse_min_idx = len(nums) - 1
        reverse_max_idx = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    reverse_min_idx = min(reverse_min_idx, i)
                    reverse_max_idx = max(reverse_max_idx, j)

        if reverse_min_idx >= reverse_max_idx:
            return 0
        else:
            return reverse_max_idx - reverse_min_idx + 1


if __name__ == "__main__":
    print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # 5
    print(Solution().findUnsortedSubarray([2, 1]))  # 2
    print(Solution().findUnsortedSubarray([3, 2, 3, 2, 4]))  # 4
    print(Solution().findUnsortedSubarray([2, 3, 3, 2, 4]))  # 3
    print(Solution().findUnsortedSubarray([1, 2, 3, 3, 3]))  # 0
    print(Solution().findUnsortedSubarray([1, 2, 4, 5, 3]))  # 3
    print(Solution().findUnsortedSubarray([1, 3, 5, 2, 4]))  # 4
    print(Solution().findUnsortedSubarray([1]))  # 0
