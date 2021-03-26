class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().findMinStep(board="WRRBBW", hand="RB"))  # -1
    print(Solution().findMinStep(board="WWRRBBWW", hand="WRBRW"))  # 2
    print(Solution().findMinStep(board="G", hand="GGGGG"))  # 2
    print(Solution().findMinStep(board="RBYYBBRRB", hand="YRBGB"))  # 3
