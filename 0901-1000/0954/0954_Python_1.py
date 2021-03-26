import collections
from typing import List


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = collections.Counter(A)

        for k in sorted(count.keys()):
            if count[k] > 0:
                if k > 0:
                    if count[k * 2] >= count[k]:
                        count[k * 2] -= count[k]
                    else:
                        return False
                elif k < 0:
                    if count[k / 2] >= count[k]:
                        count[k / 2] -= count[k]
                    else:
                        return False
                else:  # k=0
                    if count[k] % 2 != 0:
                        return False

        return True


if __name__ == "__main__":
    print(Solution().canReorderDoubled([3, 1, 3, 6]))  # False
    print(Solution().canReorderDoubled([2, 1, 2, 6]))  # False
    print(Solution().canReorderDoubled([4, -2, 2, -4]))  # True
    print(Solution().canReorderDoubled([1, 2, 4, 16, 8, 4]))  # False
