from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        idx = 0
        for i in range(len(nums)):
            n = nums[i]
            if n % 2 == 1:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        return nums


if __name__ == "__main__":
    print(Solution().exchange(nums=[1, 2, 3, 4]))  # [1,3,2,4]
