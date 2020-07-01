from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().lemonadeChange([5, 5, 5, 10, 20]))  # True
    print(Solution().lemonadeChange([5, 5, 10]))  # True
    print(Solution().lemonadeChange([10, 10]))  # False
    print(Solution().lemonadeChange([5, 5, 10, 10, 20]))  # False
