from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap1 = {}
        hashmap2 = {}
        for n in nums1:
            if n not in hashmap1:
                hashmap1[n] = 1
            else:
                hashmap1[n] += 1
        for n in nums2:
            if n in hashmap1:
                if n not in hashmap2:
                    hashmap2[n] = 1
                else:
                    hashmap2[n] += 1
        ans = []
        for n in hashmap1:
            if n in hashmap2:
                ans += [n] * min(hashmap1[n], hashmap2[n])
        return ans


if __name__ == "__main__":
    print(Solution().intersect([1, 2, 2, 1], [2, 2]))  # [2,2]
    print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4,9]
