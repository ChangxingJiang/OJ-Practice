from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # 选取每个数组中最大的子序列
        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        # 合并两个数组的最大子序列
        def merge(A, B):
            lst = []
            while A or B:
                bigger = A if A > B else B
                lst.append(bigger[0])
                bigger.pop(0)
            return lst

        return max(merge(pick_max(nums1, i), pick_max(nums2, k - i)) for i in range(k + 1) if
                   i <= len(nums1) and k - i <= len(nums2))


if __name__ == "__main__":
    # [9, 8, 6, 5, 3]
    print(Solution().maxNumber(nums1=[3, 4, 6, 5],
                               nums2=[9, 1, 2, 5, 8, 3],
                               k=5))

    # [6, 7, 6, 0, 4]
    print(Solution().maxNumber(nums1=[6, 7],
                               nums2=[6, 0, 4],
                               k=5))

    # [9, 8, 9]
    print(Solution().maxNumber(nums1=[3, 9],
                               nums2=[8, 9],
                               k=3))
