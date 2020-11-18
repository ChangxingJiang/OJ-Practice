import collections
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # 类型1
        ans = 0
        for i in range(len(nums1)):
            n1 = nums1[i] ** 2
            tmp = collections.Counter()
            for n2 in nums2:
                n3 = n1 / n2
                if n3 in tmp:
                    ans += tmp[n3]
                tmp[n2] += 1

        # 类型2
        for i in range(len(nums2)):
            n1 = nums2[i] ** 2
            tmp = collections.Counter()
            for n2 in nums1:
                n3 = n1 / n2
                if n3 in tmp:
                    ans += tmp[n3]
                tmp[n2] += 1

        return ans


if __name__ == "__main__":
    print(Solution().numTriplets([7, 4], [5, 2, 8, 9]))  # 1
    print(Solution().numTriplets([1, 1], [1, 1, 1]))  # 9
    print(Solution().numTriplets([7, 7, 8, 3], [1, 2, 9, 7]))  # 2
    print(Solution().numTriplets([4, 7, 9, 11, 23], [3, 5, 1024, 12, 18]))  # 0
