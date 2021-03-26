from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num) - 1] = -nums[abs(num) - 1]
        return ans


if __name__ == "__main__":
    print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # [2,3]
    print(Solution().findDuplicates([2, 2]))  # [2]
