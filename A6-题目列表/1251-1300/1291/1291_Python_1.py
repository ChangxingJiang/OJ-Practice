from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        pass


if __name__ == "__main__":
    # [123,234]
    print(Solution().sequentialDigits(low=100, high=300))

    # [1234,2345,3456,4567,5678,6789,12345]
    print(Solution().sequentialDigits(low=1000, high=13000))
