from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        bigger = True
        for i in range(len(nums) - 1):
            if bigger:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                bigger = False
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                bigger = True


if __name__ == "__main__":
    lst = [3, 5, 2, 1, 6, 4]
    Solution().wiggleSort(lst)
    print(lst)  # [3,5,1,6,2,4]
