import collections
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return len(collections.Counter(target) - collections.Counter(arr)) == 0


if __name__ == "__main__":
    print(Solution().canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))  # True
    print(Solution().canBeEqual(target=[7], arr=[7]))  # True
    print(Solution().canBeEqual(target=[1, 12], arr=[12, 1]))  # True
    print(Solution().canBeEqual(target=[3, 7, 9], arr=[3, 7, 11]))  # False
    print(Solution().canBeEqual(target=[1, 1, 1, 1, 1], arr=[1, 1, 1, 1, 1]))  # True
    print(Solution().canBeEqual(target=[1, 2, 2, 3], arr=[1, 1, 2, 3]))  # False
