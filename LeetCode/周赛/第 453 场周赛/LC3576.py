from typing import List


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        # 尝试全变为 1
        nums1 = list(nums)
        k1 = k
        for i in range(n):
            if nums1[i] == -1:
                if i == n - 1:
                    k1 = -1
                    break  # 最后一个不可能换掉，放弃全变为 1 的方法
                elif k1 == 0:
                    k1 = -1
                    break  # 变化次数已经用尽
                else:
                    nums1[i + 1] *= -1
                    k1 -= 1
        if k1 >= 0:
            return True

        # 尝试全变为 -1
        nums2 = list(nums)
        k2 = k
        for i in range(n):
            if nums2[i] == 1:
                if i == n - 1:
                    return False
                elif k2 == 0:
                    return False
                else:
                    nums2[i + 1] *= -1
                    k2 -= 1
        if k2 >= 0:
            return True

        return False


if __name__ == "__main__":
    print(Solution().canMakeEqual([1, -1, 1, -1, 1], 3))  # True
    print(Solution().canMakeEqual([-1, -1, -1, 1, 1, 1], 5))  # False
