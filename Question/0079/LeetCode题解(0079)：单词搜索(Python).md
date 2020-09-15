# LeetCode题解(0079)：在二维数组中寻找单词是否由连续的字母元素组成(Python)

题目：[原题链接](https://leetcode-cn.com/problems/word-search/)（中等）

标签：回溯算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N1×N2)$ | $O(N1×N2)$ | 184ms (95.14%) |
| Ans 2 (Python) | $O(N1×N2)$ | $O(N1×N2)$ | 64ms (99.80%)  |
| Ans 3 (Python) |            |            |                |

解法一（回溯算法）：

```python
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
```

解法二（增加前置判断）：

![LeetCode题解(0079)：截图](LeetCode题解(0079)：截图.png)

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 前置判断
        board_lst = []
        for line in board:
            board_lst += line
        board_count = collections.Counter(board_lst)
        word_count = collections.Counter(word)
        for k, v in word_count:
            if board_count[k] < v:
                return False

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
```