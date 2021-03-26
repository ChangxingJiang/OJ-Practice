import bisect
import collections
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i2 = bisect.bisect_right(arr, x)
        i1 = i2 - 1
        print(i1, i2)
        ans = collections.deque()
        while len(ans) < k:
            if i1 < 0:
                ans.append(arr[i2])
                i2 += 1
            elif i2 == len(arr):
                ans.appendleft(arr[i1])
                i1 -= 1
            elif x - arr[i1] <= arr[i2] - x:
                ans.appendleft(arr[i1])
                i1 -= 1
            elif i2 < len(arr):
                ans.append(arr[i2])
                i2 += 1
        return list(ans)


if __name__ == "__main__":
    print(Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))  # [1,2,3,4]
    print(Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))  # [1,2,3,4]
