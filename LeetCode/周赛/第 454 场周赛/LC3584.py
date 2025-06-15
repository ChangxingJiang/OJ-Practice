from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        # 处理 m = 1 的特殊情况
        if m == 1:
            return max(max(nums) * max(nums), min(nums) * min(nums))

        nums1_max = None  # 之前的正数最大值
        nums1_min = None  # 之前的正数最小值
        nums2_max = None  # 之前的负数最小值（绝对值最大值）
        nums2_min = None  # 之前的负数最大值（绝对值最小值）
        has_zero = False  # 之前是否存在 0

        # 跳过 m 个元素，这些无法构成子序列的末尾
        # 遍历每个末尾未知选择最优解
        n = len(nums)
        result = None
        for i in range(m - 1, n):
            # 更新开头位置
            num_old = nums[i - m + 1]
            if num_old > 0:
                if (nums1_max is None or num_old > nums1_max):
                    nums1_max = num_old
                if (nums1_min is None or num_old < nums1_min):
                    nums1_min = num_old
            elif num_old < 0:
                if (nums2_max is None or num_old < nums2_max):
                    nums2_max = num_old
                if (nums2_min is None or num_old > nums2_min):
                    nums2_min = num_old
            else:
                has_zero = True

            # 计算末尾位置的值
            num_new = nums[i]

            # 如果已经有 0，则无论如何都可以取到 0
            if has_zero is True:
                if result is not None:
                    result = max(result, 0)
                else:
                    result = 0

            if num_new > 0:
                if nums1_max is not None:  # 已有正数
                    if result is not None:
                        result = max(result, nums1_max * num_new)
                    else:
                        result = nums1_max * num_new
                elif nums2_min is not None:  # 只有负数
                    if result is not None:
                        result = max(result, nums2_min * num_new)
                    else:
                        result = nums2_min * num_new
                else:
                    pass  # 之前只有 0
            elif num_new < 0:
                if nums2_max is not None:  # 已有负数
                    if result is not None:
                        result = max(result, nums2_max * num_new)
                    else:
                        result = nums2_max * num_new
                elif nums1_min is not None:  # 只有正数
                    if result is not None:
                        result = max(result, nums1_min * num_new)
                    else:
                        result = nums1_min * num_new
                else:  # 之前只有 0
                    pass
            else:  # num_new = 0:
                if result is not None:
                    result = max(result, 0)
                else:
                    result = 0

        return result


if __name__ == "__main__":
    print(Solution().maximumProduct(nums=[-1, -9, 2, 3, -2, -3, 1], m=1))  # 81
    print(Solution().maximumProduct(nums=[1, 3, -5, 5, 6, -4], m=3))  # 20
    print(Solution().maximumProduct(nums=[2, -1, 2, -6, 5, 2, -5, 7], m=2))  # 35

    # 测试用例
    print(Solution().maximumProduct(nums=[-1, 1], m=2))  # -1
    print(Solution().maximumProduct(nums=[-9, -9, -1, 2, -8, 10, 3, 10, 0], m=7))  # 0
    print(Solution().maximumProduct(nums=[10, 9, 3, 6, 6, 2, -7, -6, -6], m=7))  # -18
    print(Solution().maximumProduct(nums=[0, -4, 1, 0, 1], m=3))  #
