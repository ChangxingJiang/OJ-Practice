from typing import List


# 数学
# O(N)


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # 处理不相遇的特殊情况
        if not left:
            return n - min(right)
        if not right:
            return max(left)

        # 处理相遇的情况
        return max(n - min(right), max(left))


if __name__ == "__main__":
    print(Solution().getLastMoment(n=4, left=[4, 3], right=[0, 1]))  # 4
    print(Solution().getLastMoment(n=7, left=[], right=[0, 1, 2, 3, 4, 5, 6, 7]))  # 7
    print(Solution().getLastMoment(n=7, left=[0, 1, 2, 3, 4, 5, 6, 7], right=[]))  # 7
    print(Solution().getLastMoment(n=9, left=[5], right=[4]))  # 5
    print(Solution().getLastMoment(n=6, left=[6], right=[0]))  # 6
    print(Solution().getLastMoment(n=20, left=[4, 7, 15], right=[9, 3, 13, 10]))  # 17
