from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_list = [-1] * len(nums)
        reverse_min_idx = None
        reverse_max_idx = None

        for i in range(len(nums)):
            if (i > 0 and nums[i] >= max_list[i - 1]) or i == 0:
                max_list[i] = nums[i]
            else:
                # 维护最大值数组
                max_list[i] = max_list[i - 1]

                # 计算起始坐标
                idx = i - 1
                while idx >= 0 and max_list[idx] > nums[i]:
                    idx -= 1
                idx += 1

                # 更新升序数组起始坐标和升序数组结尾坐标
                if reverse_min_idx is None or idx < reverse_min_idx:
                    reverse_min_idx = idx
                if reverse_max_idx is None or i > reverse_max_idx:
                    reverse_max_idx = i

        if reverse_min_idx is not None and reverse_max_idx is not None:
            return reverse_max_idx - reverse_min_idx + 1
        else:
            return 0


if __name__ == "__main__":
    print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # 5
    print(Solution().findUnsortedSubarray([2, 1]))  # 2
    print(Solution().findUnsortedSubarray([3, 2, 3, 2, 4]))  # 4
    print(Solution().findUnsortedSubarray([2, 3, 3, 2, 4]))  # 3
    print(Solution().findUnsortedSubarray([1, 2, 3, 3, 3]))  # 0
    print(Solution().findUnsortedSubarray([1, 2, 4, 5, 3]))  # 3
    print(Solution().findUnsortedSubarray([1, 3, 5, 2, 4]))  # 4
