import collections
import math
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        s1, s2 = sum(i * c1[i] for i in range(1, 7)), sum(i * c2[i] for i in range(1, 7))

        if s1 == s2:
            return 0

        if s1 > s2:
            s1, s2 = s2, s1
            c1, c2 = c2, c1

        # s1 < s2

        diff = s2 - s1
        ans = 0

        if c1[1] > 0 or c2[6] > 0:
            if (c1[1] + c2[6]) * 5 >= diff:
                return ans + math.ceil(diff / 5)
            else:
                diff -= (c1[1] + c2[6]) * 5
                ans += (c1[1] + c2[6])

        if c1[2] > 0 or c2[5] > 0:
            if (c1[2] + c2[5]) * 4 >= diff:
                return ans + math.ceil(diff / 4)
            else:
                diff -= (c1[2] + c2[5]) * 4
                ans += (c1[2] + c2[5])

        if c1[3] > 0 or c2[4] > 0:
            if (c1[3] + c2[4]) * 3 >= diff:
                return ans + math.ceil(diff / 3)
            else:
                diff -= (c1[3] + c2[4]) * 3
                ans += (c1[3] + c2[4])

        if c1[4] > 0 or c2[3] > 0:
            if (c1[4] + c2[3]) * 2 >= diff:
                return ans + math.ceil(diff / 2)
            else:
                diff -= (c1[4] + c2[3]) * 2
                ans += (c1[4] + c2[3])

        if c1[5] > 0 or c2[2] > 0:
            if (c1[5] + c2[2]) * 1 >= diff:
                return ans + math.ceil(diff / 1)
            else:
                diff -= (c1[5] + c2[2]) * 1
                ans += (c1[5] + c2[2])

        return -1


if __name__ == "__main__":
    print(Solution().minOperations(nums1=[1, 2, 3, 4, 5, 6], nums2=[1, 1, 2, 2, 2, 2]))  # 3
    print(Solution().minOperations(nums1=[1, 1, 1, 1, 1, 1, 1], nums2=[6]))  # -1
    print(Solution().minOperations(nums1=[6, 6], nums2=[1]))  # 3

    # 测试用例:46/64
    print(Solution().minOperations(nums1=[5, 6, 4, 3, 1, 2], nums2=[6, 3, 3, 1, 4, 5, 3, 4, 1, 3, 4]))  # 4

    # 自制测试用例
    print(Solution().minOperations(nums1=[1, 1], nums2=[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))  # 13
