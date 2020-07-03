class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


if __name__ == "__main__":
    print(Solution().divisorGame(2))  # True
    print(Solution().divisorGame(3))  # False
    print(Solution().divisorGame(20))  # True
