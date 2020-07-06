class Solution:
    def numberOfSteps(self, num: int) -> int:
        num = bin(num)[2:]
        return len(num) + num.count("1") - 1


if __name__ == "__main__":
    print(Solution().numberOfSteps(14))  # 6
    print(Solution().numberOfSteps(8))  # 4
    print(Solution().numberOfSteps(123))  # 12
