from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums2:
            if n in nums1 and n not in ans:
                ans.append(n)
        return ans


if __name__ == "__main__":
    print(Solution().intersection([1, 2, 2, 1], [2, 2]))  # [2]
    print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # [9,4]
