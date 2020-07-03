import collections
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = collections.Counter(arr1)
        ans = []
        for n in arr2:
            if n in count:
                for _ in range(count[n]):
                    ans.append(n)
                del count[n]
        ans += sorted(list(count.elements()))
        return ans


if __name__ == "__main__":
    print(Solution().relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
    # [2,2,2,1,4,3,3,9,6,7,19]

    print(Solution().relativeSortArray(arr1=[28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]))
    # [22,28,8,6,17,44]
