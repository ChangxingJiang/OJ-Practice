from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1, sum2 = sum(array1), sum(array2)
        set1, set2 = set(array1), set(array2)
        if (sum1 - sum2) % 2 != 0:
            return []
        change = (sum1 - sum2) // 2
        for n in set1:
            if n - change in set2:
                return [n, n - change]
        return []


if __name__ == "__main__":
    # [1,3]
    print(Solution().findSwapValues(array1=[4, 1, 2, 1, 1, 2], array2=[3, 6, 3, 3]))

    # []
    print(Solution().findSwapValues(array1=[1, 2, 3], array2=[4, 5, 6]))
