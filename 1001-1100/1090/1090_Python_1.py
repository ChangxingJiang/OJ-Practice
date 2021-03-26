import collections
import heapq
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        heap = []
        for i in range(len(values)):
            heapq.heappush(heap, (-values[i], labels[i]))

        count = collections.Counter()
        ans = 0
        now = 0
        while heap and now < num_wanted:
            value, label = heapq.heappop(heap)
            if count[label] < use_limit:
                count[label] += 1
                ans -= value
                now += 1

        return ans


if __name__ == "__main__":
    # 9
    print(Solution().largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 1, 2, 2, 3], num_wanted=3, use_limit=1))

    # 12
    print(Solution().largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 3, 3, 3, 2], num_wanted=3, use_limit=2))

    # 16
    print(Solution().largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], num_wanted=3, use_limit=1))

    # 24
    print(Solution().largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], num_wanted=3, use_limit=2))
