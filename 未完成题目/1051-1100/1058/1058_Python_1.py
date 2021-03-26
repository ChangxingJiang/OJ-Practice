from typing import List


class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        pass


if __name__ == "__main__":
    # "1.000"
    print(Solution().minimizeError(prices=["0.700", "2.800", "4.900"], target=8))

    # "-1"
    print(Solution().minimizeError(prices=["1.500", "2.500", "3.500"], target=10))
