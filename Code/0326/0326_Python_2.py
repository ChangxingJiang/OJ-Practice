import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return (math.log10(n) / math.log10(3)) % 1 == 0


if __name__ == "__main__":
    print(Solution().isPowerOfThree(27))  # True
    print(Solution().isPowerOfThree(0))  # False
    print(Solution().isPowerOfThree(9))  # True
    print(Solution().isPowerOfThree(45))  # False
