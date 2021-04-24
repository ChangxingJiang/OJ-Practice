from typing import List


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        s1, s2 = len(arr1), len(arr2)

        ans1 = 0
        ans2 = 0

        for i in range(s1):
            ans1 ^= arr1[i]

        for i in range(s2):
            ans2 ^= arr2[i]

        return ans1 & ans2


if __name__ == "__main__":
    print(Solution().getXORSum(arr1=[1, 2, 3], arr2=[6, 5]))  # 0
    print(Solution().getXORSum(arr1=[12], arr2=[4]))  # 4
