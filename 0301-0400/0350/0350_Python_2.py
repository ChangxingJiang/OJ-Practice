from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}

        # 选择较小的一个数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # 将较小的一个数组存入哈希表
        for n in nums1:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1

        ans = []
        for n in nums2:
            if n in hashmap and hashmap[n] > 0:
                ans.append(n)
                hashmap[n] -= 1
        return ans


if __name__ == "__main__":
    print(Solution().intersect([1, 2, 2, 1], [2, 2]))  # [2,2]
    print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4,9]
    print(Solution().intersect([1, 2], [1, 1]))  # [1]
