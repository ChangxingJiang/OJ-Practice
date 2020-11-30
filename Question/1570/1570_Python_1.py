from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = [(i, n) for i, n in enumerate(nums) if n != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        s1, s2 = len(self.array), len(vec.array)
        i1, i2 = 0, 0
        ans = 0
        while i1 < s1 and i2 < s2:
            idx1, n1 = self.array[i1]
            idx2, n2 = vec.array[i2]
            if idx1 == idx2:
                ans += n1 * n2
                i1 += 1
                i2 += 1
            elif idx1 < idx2:
                i1 += 1
            else:
                i2 += 1
        return ans


if __name__ == "__main__":
    nums1 = [1, 0, 0, 2, 3]
    nums2 = [0, 3, 0, 4, 0]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    print(v1.dotProduct(v2))  # 8

    nums1 = [0, 1, 0, 0, 0]
    nums2 = [0, 0, 0, 0, 2]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    print(v1.dotProduct(v2))  # 0

    nums1 = [0, 1, 0, 0, 2, 0, 0]
    nums2 = [1, 0, 0, 0, 3, 0, 4]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    print(v1.dotProduct(v2))  # 6
