from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i1, i2 = -1, -1
        for i in range(len(nums) - 1):
            # 处理递增的情况
            if nums[i] < nums[i + 1]:
                i1, i2 = i, i + 1

            # 处理递减的情况
            elif i1 == -1 or nums[i + 1] > nums[i1]:
                i2 = i + 1

        # 处理完全单调递减的情况
        if i1 == -1:
            i1, i2 = 0, len(nums) - 1
            while i1 <= i2:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i1, i2 = i1 + 1, i2 - 1

        # 处理不完全单调递减的情况
        else:
            # 交换最后一个递增和递减中最小的值
            nums[i1], nums[i2] = nums[i2], nums[i1]

            # 交换递减中的值
            i1, i2 = i1 + 1, len(nums) - 1
            while i1 <= i2:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i1, i2 = i1 + 1, i2 - 1


if __name__ == "__main__":
    lst = [1, 2, 3]
    Solution().nextPermutation(lst)
    print(lst)  # [1,3,2]

    lst = [3, 2, 1]
    Solution().nextPermutation(lst)
    print(lst)  # [1,2,3]

    lst = [1, 1, 5]
    Solution().nextPermutation(lst)
    print(lst)  # [1,5,1]

    lst = [2, 3, 1]
    Solution().nextPermutation(lst)
    print(lst)  # [3,1,2]

    lst = [1, 3, 2]
    Solution().nextPermutation(lst)
    print(lst)  # [2,1,3]

    lst = [5, 1, 1]
    Solution().nextPermutation(lst)
    print(lst)  # [1,1,5]
