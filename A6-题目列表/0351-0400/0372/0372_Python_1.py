from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().superPow(a=2, b=[3]))  # 8
    print(Solution().superPow(a=2, b=[1, 0]))  # 1024
    print(Solution().superPow(a=1, b=[4, 3, 3, 8, 5, 2]))  # 1
    print(Solution().superPow(a=2147483647, b=[2, 0, 0]))  # 1198
