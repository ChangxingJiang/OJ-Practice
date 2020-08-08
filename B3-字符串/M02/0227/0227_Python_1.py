class Solution:
    def calculate(self, s: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().calculate("3+2*2"))  # 7
    print(Solution().calculate(" 3/2 "))  # 1
    print(Solution().calculate(" 3+5 / 2 "))  # 5
