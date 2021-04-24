from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 构造字典树
        root = {}
        for word in words:
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["#"] = word

        m, n = len(board), len(board[0])

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def neighbors(x, y):
            return [(xx, yy) for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if is_valid(xx, yy)]

        # 深度优先搜索
        def dfs(now, i1, j1, visited):
            if board[i1][j1] not in now:
                return
            now = now[board[i1][j1]]
            if "#" in now:
                ans.add(now["#"])
            for i2, j2 in neighbors(i1, j1):
                if (i2, j2) not in visited:
                    visited.add((i2, j2))
                    dfs(now, i2, j2, visited)
                    visited._remove((i2, j2))

        ans = set()

        # 遍历二维网格
        for i in range(m):
            for j in range(n):
                dfs(root, i, j, {(i, j)})

        return list(ans)


if __name__ == "__main__":
    # ["eat","oath"]
    print(Solution().findWords(
        board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        words=["oath", "pea", "eat", "rain"]))

    # []
    print(Solution().findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))

    # ["a"]
    print(Solution().findWords(board=[["a"]], words=["a"]))

    # []
    print(Solution().findWords(board=[["a", "a"]], words=["aaa"]))
