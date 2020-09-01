class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


if __name__ == "__main__":
    print(Solution().addStrings("0", "0"))  # "0"
    print(Solution().addStrings("135", "2"))  # "137"
    print(Solution().addStrings("1", "9"))  # "10"
