class Solution:
    def fractionAddition(self, expression: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().fractionAddition("-1/2+1/2"))  # "0/1"
    print(Solution().fractionAddition("-1/2+1/2+1/3"))  # "1/3"
    print(Solution().fractionAddition("1/3-1/2"))  # "-1/6"
    print(Solution().fractionAddition("5/3+1/3"))  # "2/1"
