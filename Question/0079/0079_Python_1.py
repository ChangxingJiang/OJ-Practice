from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N1 = len(board)
        N2 = len(board[0])
        size = len(word)

        visited = set()

        # 回溯递归函数(idx=当前字母的位置)
        def recursor(x=0, y=0, idx=0):
            # 判断是否已经完成查找
            if idx == size:
                return True

            # 寻找所有可能的结果
            maybe_list = []
            if idx == 0:  # 处理起始点的情况
                for i in range(N1):
                    for j in range(N2):
                        if board[i][j] == word[0]:
                            maybe_list.append((i, j))
            else:  # 处理不是起始点的情况
                if x > 0 and (x - 1, y) not in visited and board[x - 1][y] == word[idx]:
                    maybe_list.append((x - 1, y))
                if x < N1 - 1 and (x + 1, y) not in visited and board[x + 1][y] == word[idx]:
                    maybe_list.append((x + 1, y))
                if y > 0 and (x, y - 1) not in visited and board[x][y - 1] == word[idx]:
                    maybe_list.append((x, y - 1))
                if y < N2 - 1 and (x, y + 1) not in visited and board[x][y + 1] == word[idx]:
                    maybe_list.append((x, y + 1))

            print(idx, "->", maybe_list)

            if not maybe_list:
                return False

            # 迭代所有可能的结果
            for maybe_point in maybe_list:
                visited.add(maybe_point)
                if recursor(maybe_point[0], maybe_point[1], idx + 1):
                    return True
                visited.remove(maybe_point)

            return False

        return recursor()


if __name__ == "__main__":
    word_board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    print(Solution().exist(word_board, "ABCCED"))  # True
    print(Solution().exist(word_board, "SEE"))  # True
    print(Solution().exist(word_board, "ABCB"))  # False
