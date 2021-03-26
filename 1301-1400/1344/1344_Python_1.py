class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        n1 = ((hour + minutes / 60) % 12) * 30
        n2 = minutes * 6
        if n1 < n2:
            n1, n2 = n2, n1
        return min(n1 - n2, n2 + 360 - n1)


if __name__ == "__main__":
    print(Solution().angleClock(hour=12, minutes=30))  # 165
    print(Solution().angleClock(hour=3, minutes=30))  # 75
    print(Solution().angleClock(hour=3, minutes=15))  # 7.5
    print(Solution().angleClock(hour=4, minutes=50))  # 155
    print(Solution().angleClock(hour=12, minutes=0))  # 0
