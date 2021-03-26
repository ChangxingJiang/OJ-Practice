import random
from typing import List


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.black = {}

        black_set = set(blacklist)
        last = N - 1

        # 保证黑名单连续数字不相同（如果黑名单超过白名单长度则为-1,-2，仍然会在白名单中向前遍历）
        blacklist.sort()
        for black in blacklist:
            while last in black_set:
                last -= 1
            self.black[black] = last
            last -= 1

        self.n = N - len(black_set)

        print(self.n, self.black)

    def pick(self) -> int:
        r = random.randint(0, self.n - 1)
        return self.black[r] if r in self.black else r


if __name__ == "__main__":
    obj = Solution(1, [])
    print(obj.pick())  # 0
    print(obj.pick())  # 0
    print(obj.pick())  # 0
    print()

    obj = Solution(2, [])
    print(obj.pick())  # 1
    print(obj.pick())  # 1
    print(obj.pick())  # 1
    print()

    obj = Solution(3, [1])
    print(obj.pick())  # 0
    print(obj.pick())  # 0
    print(obj.pick())  # 2
    print()

    obj = Solution(4, [2])
    print(obj.pick())  # 1
    print(obj.pick())  # 3
    print(obj.pick())  # 1
    print()

    Solution(4, [0, 1])
    Solution(4, [0, 1, 2])
