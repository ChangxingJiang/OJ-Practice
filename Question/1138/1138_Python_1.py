class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # 整理字母板坐标
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        hashmap = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                hashmap[board[i][j]] = (i, j)

        # 生成路径
        ans = ""
        now = (0, 0)
        for ch in target:
            aim = hashmap[ch]
            move1 = aim[0] - now[0]
            move2 = aim[1] - now[1]
            # 因为最后一行列数不同，因此先向左右，再向右下，以避免移除字母板
            if move1 < 0:
                ans += "U" * (-move1)
            if move2 < 0:
                ans += "L" * (-move2)
            if move1 > 0:
                ans += "D" * move1
            if move2 > 0:
                ans += "R" * move2

            now = aim
            ans += "!"

        return ans


if __name__ == "__main__":
    print(Solution().alphabetBoardPath(target="leet"))  # "DDR!UURRR!!DDD!"
    print(Solution().alphabetBoardPath(target="code"))  # "RR!DDRR!UUL!R!"
