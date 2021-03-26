class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            else:
                n /= 3
        else:
            return True


if __name__ == "__main__":
    print(Solution().isPowerOfThree(27))  # True
    print(Solution().isPowerOfThree(0))  # False
    print(Solution().isPowerOfThree(9))  # True
    print(Solution().isPowerOfThree(45))  # False
