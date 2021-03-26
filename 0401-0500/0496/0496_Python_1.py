from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            idx = nums2.index(n)
            for m in nums2[idx:]:
                if m > n:
                    ans.append(m)
                    break
            else:
                ans.append(-1)
        return ans


if __name__ == "__main__":
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # [-1,3,-1]
    print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))  # [3,-1]
