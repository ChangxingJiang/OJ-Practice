class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n /= 2
        else:
            return True


if __name__ == "__main__":
    print(Solution().isPowerOfTwo(1))  # True
    print(Solution().isPowerOfTwo(16))  # True
    print(Solution().isPowerOfTwo(218))  # False
