import collections
from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        count = collections.defaultdict(set)  # 以点(x,y)的y为key，x为值
        for x, y in points:
            count[y].add(x)

        val = None
        for x, lst in count.items():
            lst = list(sorted(lst))
            if len(lst) % 2 == 1:
                mid = lst[len(lst) // 2]
            else:
                mid = (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
            # 检查自身是否相对中线对称
            left, right = 0, len(lst) - 1
            while left < right:
                if lst[right] - mid != mid - lst[left]:
                    return False
                left += 1
                right -= 1
            # 检查中线是否一致
            if val is None:
                val = mid
            elif val != mid:
                return False

        return True


if __name__ == "__main__":
    print(Solution().isReflected([[1, 1], [-1, 1]]))  # True
    print(Solution().isReflected([[0, 0], [1, 0], [3, 0]]))  # True
    print(Solution().isReflected([[1, 1], [-1, -1]]))  # False
    print(Solution().isReflected([[-16, 1], [16, 1], [16, 1]]))  # True
