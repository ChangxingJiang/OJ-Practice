import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        size1, size2 = len(nums1), len(nums2)
        heap = [(nums2[0] + nums1[i], i, 0) for i in range(size1)]

        ans = []
        for _ in range(min(size1 * size2, k)):
            val, i1, i2 = heapq.heappop(heap)
            ans.append([nums1[i1], nums2[i2]])
            if i2 < size2 - 1:
                heapq.heappush(heap,(nums1[i1] + nums2[i2 + 1], i1, i2 + 1))

        return ans


if __name__ == "__main__":
    # [1,2],[1,4],[1,6]
    print(Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))

    # [1,1],[1,1]
    print(Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))

    # [1,3],[2,3]
    print(Solution().kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))
