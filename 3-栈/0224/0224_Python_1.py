class Solution:
    def calculate(self, s: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().calculate("1 + 1"))  # 2
    print(Solution().calculate(" 2-1 + 2 "))  # 3
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
