import collections
from typing import List


# O(N)


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        num_list = list(sorted(count.values()))
        size = len(num_list)

        ans = size

        for i in range(size):
            if k >= num_list[i]:
                ans -= 1
                k -= num_list[i]
            else:
                return ans

        return 0


if __name__ == "__main__":
    print(Solution().findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1))  # 1
    print(Solution().findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))  # 2
