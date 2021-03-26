from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        x1, x2, x3, x4 = [], [], [], []
        for i in range(len(arr1)):
            x1.append(arr1[i] + arr2[i] + i)
            x2.append(arr1[i] + arr2[i] - i)
            x3.append(arr1[i] - arr2[i] + i)
            x4.append(arr1[i] - arr2[i] - i)
        return max(max(x1) - min(x1), max(x2) - min(x2), max(x3) - min(x3), max(x4) - min(x4))


if __name__ == "__main__":
    print(Solution().maxAbsValExpr(arr1=[1, 2, 3, 4], arr2=[-1, 4, 5, 6]))  # 13
    print(Solution().maxAbsValExpr(arr1=[1, -2, -5, 0, 10], arr2=[0, -2, -1, -7, -4]))  # 20
