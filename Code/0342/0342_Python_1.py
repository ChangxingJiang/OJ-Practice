class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        while num > 1:
            if num % 4 == 0:
                num /= 4
            else:
                return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().isPowerOfFour(16))  # True
    print(Solution().isPowerOfFour(5))  # False
