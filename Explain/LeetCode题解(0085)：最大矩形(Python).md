# LeetCode题解(0085)：最大矩形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximal-rectangle/)（困难）

标签：栈、栈-单调栈、动态规划

相关题目：0084（可以用于每行的统计）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2M)$  | $O(1)$     | 160ms (32.61%) |
| Ans 2 (Python) | $O(N×M)$   | $O(N×M)$   | 104ms (72.04%) |
| Ans 3 (Python) | $O(N^2M)$  | $O(N×M)$   | 56ms (99.41%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（借用0084的方法实现）：

```python
def maximalRectangle(self, matrix: List[List[str]]) -> int:
    # 处理特殊情况
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    ans = 0
    size = len(matrix[0])
    for idx in range(len(matrix)):
        stack = []
        for j in range(size):
            # 统计从当前位置向上的最大高度
            value = 0
            for i in range(idx, -1, -1):
                if matrix[i][j] == "1":
                    value += 1
                else:
                    break

            # 当空栈或栈顶高度小于当前高度时，直接将当前高度压入栈
            if not stack or stack[-1][1] < value:
                stack.append([j, value])
            else:
                # 计算当前所有可能的最大值
                now = None
                while stack and stack[-1][1] > value:
                    now = stack.pop()
                    ans = max(ans, (j - now[0]) * now[1])
                # 调整当前栈顶情况
                if now:
                    stack.append([now[0], value])

        # 统计剩余的情况
        while stack:
            now = stack.pop()
            ans = max(ans, (size - now[0]) * now[1])

    return ans
```

解法二（优化解法一）：

```python
def maximalRectangle(self, matrix: List[List[str]]) -> int:
    # 处理特殊情况
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    size = len(matrix[0])

    count_line = [0] * size

    ans = 0
    for i in range(len(matrix)):
        stack = []
        for j in range(size):
            # 统计从当前位置向上的最大高度
            if matrix[i][j] == "0":
                count_line[j] = 0
            else:
                count_line[j] += 1

            # 当空栈或栈顶高度小于当前高度时，直接将当前高度压入栈
            if not stack or stack[-1][1] < count_line[j]:
                stack.append([j, count_line[j]])
            else:
                # 计算当前所有可能的最大值
                now = None
                while stack and stack[-1][1] > count_line[j]:
                    now = stack.pop()
                    ans = max(ans, (j - now[0]) * now[1])
                # 调整当前栈顶情况
                if now:
                    stack.append([now[0], count_line[j]])

        # 统计剩余的情况
        while stack:
            now = stack.pop()
            ans = max(ans, (size - now[0]) * now[1])

    return ans
```

解法三：

> 将每一行视作一个二进制数，使用与运算计算最大宽度
>
> 虽然最坏情况的时间复杂度高，但是大部分循环都不需要运行到底。

```python
def maximalRectangle(self, matrix: List[List[str]]) -> int:
    # 处理特殊情况
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    size = len(matrix)

    ans = 0

    # 将每一行视作一个二进制数
    nums = [int("".join(row), base=2) for row in matrix]

    for i in range(size):
        num = nums[i]
        for j in range(i, size):
            # 使用与运算计算连续的、可以用作组成矩形的列
            num = num & nums[j]
            if not num:
                break

            # 计算矩形高度
            height = j - i + 1

            # 计算矩形宽度
            width = 0
            now = num
            while now:
                width += 1
                now = now & (now << 1)  # 通过移位来计算可以用作组成矩形的最长连续列的数量，即矩形的最大有效宽度

            ans = max(ans, height * width)

    return ans
```