import bisect
from typing import List


class Solution:
    _MOD = 10 ** 9 + 7

    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        array1 = list(sorted(nums1))

        ans = 0  # 绝对差值和
        most = 0  # 最大可缩小值
        for i in range(n):
            n1, n2 = nums1[i], nums2[i]
            diff = abs(n2 - n1)

            ans += diff

            maybe = 0
            j = bisect.bisect_right(array1, n2)
            # print(array1, n2, j)
            if j > 0:
                diff1 = abs(n2 - array1[j - 1])
                maybe = max(maybe, diff - diff1)
            if j < n:
                diff2 = abs(n2 - array1[j])
                maybe = max(maybe, diff - diff2)

            most = max(most, maybe)

        # print(ans, most)

        return (ans - most) % self._MOD


if __name__ == "__main__":
    print(Solution().minAbsoluteSumDiff(nums1=[1, 7, 5], nums2=[2, 3, 5]))  # 3
    print(Solution().minAbsoluteSumDiff(nums1=[2, 4, 6, 8, 10], nums2=[2, 4, 6, 8, 10]))  # 0
    print(Solution().minAbsoluteSumDiff(nums1=[1, 10, 4, 4, 2, 7], nums2=[9, 3, 5, 1, 7, 4]))  # 20
