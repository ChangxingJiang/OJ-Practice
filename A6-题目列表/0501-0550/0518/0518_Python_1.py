from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().change(amount=5, coins=[1, 2, 5]))  # 4
    print(Solution().change(amount=3, coins=[2]))  # 0
    print(Solution().change(amount=10, coins=[10]))  # 1
