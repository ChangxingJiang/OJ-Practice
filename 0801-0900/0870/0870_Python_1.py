import collections
from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        size = len(A)
        sorted_A, sorted_B = sorted(A), sorted(B)

        mapping = collections.defaultdict(list)
        useless = []
        i1, i2 = 0, 0
        while i1 < size:
            while i1 < size and sorted_A[i1] <= sorted_B[i2]:
                useless.append(sorted_A[i1])
                i1 += 1
            if i1 < size:
                mapping[sorted_B[i2]].append(sorted_A[i1])
                i1 += 1
            i2 += 1

        ans = []
        for b in B:
            if mapping[b]:
                ans.append(mapping[b].pop())
            else:
                ans.append(useless.pop())
        return ans


if __name__ == "__main__":
    # [2,11,7,15]
    print(Solution().advantageCount(A=[2, 7, 11, 15], B=[1, 10, 4, 11]))

    # [24,32,8,12]
    print(Solution().advantageCount(A=[12, 24, 8, 32], B=[13, 25, 32, 11]))

    # [2,0,2,1,4]
    print(Solution().advantageCount(A=[2, 0, 4, 1, 2], B=[1, 3, 0, 0, 2]))

    # [0]
    print(Solution().advantageCount(A=[0], B=[0]))

    # [5, 10, 10, 2, 8, 3, 15, 4, 0, 15, 3, 1, 7, 10, 1]
    print(Solution().advantageCount(A=[15, 15, 4, 5, 0, 1, 7, 10, 3, 1, 10, 10, 8, 2, 3],
                                    B=[4, 13, 14, 0, 14, 14, 12, 3, 15, 12, 2, 0, 6, 9, 0]))
