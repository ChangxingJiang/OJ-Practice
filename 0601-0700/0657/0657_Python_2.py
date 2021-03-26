class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


if __name__ == "__main__":
    print(Solution().judgeCircle("UD"))  # True
    print(Solution().judgeCircle("LL"))  # False
