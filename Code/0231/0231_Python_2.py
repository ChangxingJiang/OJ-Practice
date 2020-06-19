class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m = 1
        while m <= n:
            if m == n:
                return True
            m *= 2
        else:
            return False


if __name__ == "__main__":
    print(Solution().isPowerOfTwo(-2))  # False
    print(Solution().isPowerOfTwo(1))  # True
    print(Solution().isPowerOfTwo(16))  # True
    print(Solution().isPowerOfTwo(218))  # False
