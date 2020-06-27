import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        else:
            return (math.log10(num) / math.log10(4)) % 1 == 0


if __name__ == "__main__":
    print(Solution().isPowerOfFour(16))  # True
    print(Solution().isPowerOfFour(5))  # False
