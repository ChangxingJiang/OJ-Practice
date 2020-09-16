import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        return len(count.values()) == len(set(count.values()))


if __name__ == "__main__":
    print(Solution().uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]))  # True
    print(Solution().uniqueOccurrences(arr=[1, 2]))  # False
    print(Solution().uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # True
