from typing import List


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        pass

    def pick(self) -> int:
        pass


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
