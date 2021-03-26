from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # 处理中间为偶数的情况（数组一共一定为奇数个元素）
            if m % 2 == 0:
                if nums[m] == nums[m + 1]:
                    l = m + 1
                else:
                    r = m

            # 处理中间为奇数的情况
            else:
                if nums[m] == nums[m - 1]:
                    l = m + 1
                else:
                    r = m

        return nums[l]


if __name__ == "__main__":
    print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))  # 2
    print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))  # 10
