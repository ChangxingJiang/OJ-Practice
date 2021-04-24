class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            mod = n % 3
            if mod == 0:
                n //= 3
            elif mod == 1:
                n -= 1
                n //= 3
            else:
                return False
        return True


if __name__ == "__main__":
    print(Solution().checkPowersOfThree(12))  # True
    print(Solution().checkPowersOfThree(91))  # True
    print(Solution().checkPowersOfThree(21))  # False
