import bisect
from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        s1, s2, s3 = len(arr1), len(arr2), len(arr3)

        ans = []

        i1, i2, i3 = 0, 0, 0
        while i1 < s1 and i2 < s2 and i3 < s3:
            if arr1[i1] == arr2[i2] == arr3[i3]:
                ans.append(arr1[i1])
                i1 += 1
            else:
                v = max(arr1[i1], arr2[i2], arr3[i3])
                i1 = bisect.bisect_left(arr1, v, lo=i1)
                i2 = bisect.bisect_left(arr2, v, lo=i2)
                i3 = bisect.bisect_left(arr3, v, lo=i3)

        return ans


if __name__ == "__main__":
    # [1,5]
    print(Solution().arraysIntersection(arr1=[1, 2, 3, 4, 5], arr2=[1, 2, 5, 7, 9], arr3=[1, 3, 4, 5, 8]))
