class Solution:
    def solveEquation(self, equation: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().solveEquation("x+5-3+x=6+x-2"))  # "x=2"
    print(Solution().solveEquation("x=x"))  # "Infinite solutions"
    print(Solution().solveEquation("2x=x"))  # "x=0"
    print(Solution().solveEquation("2x+3x-6x=x+2"))  # "x=-1"
    print(Solution().solveEquation("x=x+2"))  # "No solution"
