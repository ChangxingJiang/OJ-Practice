from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        index1 = 0
        index2 = 0
        ans = []
        while index1 <= len(nums1) - 1 and index2 <= len(nums2) - 1:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                ans.append(nums1[index1])
                index1 += 1
                index2 += 1
        return ans


if __name__ == "__main__":
    print(Solution().intersect([1, 2, 2, 1], [2, 2]))  # [2,2]
    print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4,9]
    print(Solution().intersect([1, 2], [1, 1]))  # [1]
