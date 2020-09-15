class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


if __name__ == "__main__":
    print(Solution().multiply(num1="2", num2="3"))  # 6
    print(Solution().multiply(num1="123", num2="456"))  # 56088
    print(Solution().multiply(num1="9", num2="99"))  # 891
    print(Solution().multiply(num1="99", num2="9"))  # 891
    print(Solution().multiply(num1="9133", num2="0"))  # 0
