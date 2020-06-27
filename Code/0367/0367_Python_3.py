class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        k = 1
        n = 0
        while n <= num:
            n += k
            k += 2
            if n == num:
                return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().isPerfectSquare(16))  # True
    print(Solution().isPerfectSquare(14))  # False
    print(Solution().isPerfectSquare(1))  # True
