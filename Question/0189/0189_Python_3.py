from typing import List


class Solution:
    def reverse(self, nums: List[int], start, end):
        while start < end:
            temp = nums[end]
            nums[end] = nums[start]
            nums[start] = temp
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k %= l  # 处理k超过列表长度的情况
        self.reverse(nums, 0, l - k - 1)
        self.reverse(nums, l - k, l - 1)
        self.reverse(nums, 0, l - 1)


if __name__ == "__main__":
    nums_list = [1, 2, 3, 4, 5, 6, 7]
    print(Solution().rotate(nums_list, 3), nums_list)  # [5,6,7,1,2,3,4]
    nums_list = [-1, -100, 3, 99]
    print(Solution().rotate(nums_list, 2), nums_list)  # [3,99,-1,-100]
    nums_list = [1, 2]
    print(Solution().rotate(nums_list, 3), nums_list)  # [2,1]
