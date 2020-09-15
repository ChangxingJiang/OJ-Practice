from typing import List


class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        pass


if __name__ == "__main__":
    # 33
    print(Solution().busRapidTransit(target=31, inc=5, dec=3, jump=[6], cost=[10]))

    # 26
    print(Solution().busRapidTransit(target=612, inc=4, dec=5, jump=[3, 6, 8, 11, 5, 10, 4], cost=[4, 7, 6, 3, 7, 6, 4]))
