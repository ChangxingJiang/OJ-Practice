class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        pass


if __name__ == "__main__":
    print(Solution().angleClock(hour=12, minutes=30))  # 165
    print(Solution().angleClock(hour=3, minutes=30))  # 75
    print(Solution().angleClock(hour=3, minutes=15))  # 7.5
    print(Solution().angleClock(hour=4, minutes=50))  # 155
    print(Solution().angleClock(hour=12, minutes=0))  # 0
