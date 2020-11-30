from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        size = len(nums)
        peak = True

        i = 0
        while i < size - 1:
            if peak:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                peak = False
            else:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                peak = True
            i += 1


if __name__ == "__main__":
    lst = [5, 3, 1, 2, 3]
    Solution().wiggleSort(lst)
    print(lst)  # [5,1,3,2,3]
