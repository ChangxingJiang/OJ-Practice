from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size

        length = [0] * size
        count = [1] * size

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if length[i] >= length[j]:
                        length[j] = length[i] + 1
                        count[j] = count[i]
                    elif length[i] + 1 == length[j]:
                        count[j] += count[i]

        longest = max(length)
        return sum(n for i, n in enumerate(count) if length[i] == longest)


if __name__ == "__main__":
    print(Solution().findNumberOfLIS([1, 3, 5, 4, 7]))  # 2
    print(Solution().findNumberOfLIS([2, 2, 2, 2, 2]))  # 5
