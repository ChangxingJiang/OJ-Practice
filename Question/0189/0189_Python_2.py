from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)  # 处理k超过列表长度的情况
        nums[-k:] = nums[-k:][::-1]
        nums[:-k] = nums[:-k][::-1]
        nums[:] = nums[::-1]


if __name__ == "__main__":
    nums_list = [1, 2, 3, 4, 5, 6, 7]
    print(Solution().rotate(nums_list, 3), nums_list)  # [5,6,7,1,2,3,4]
    nums_list = [-1, -100, 3, 99]
    print(Solution().rotate(nums_list, 2), nums_list)  # [3,99,-1,-100]
    nums_list = [1, 2]
    print(Solution().rotate(nums_list, 3), nums_list)  # [2,1]
