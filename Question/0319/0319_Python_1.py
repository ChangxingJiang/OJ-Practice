class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(pow(n, 0.5)) if n > 0 else 0


if __name__ == "__main__":
    print(Solution().bulbSwitch(3))  # 1
    print(Solution().bulbSwitch(0))  # 0
    print(Solution().bulbSwitch(1))  # 1
