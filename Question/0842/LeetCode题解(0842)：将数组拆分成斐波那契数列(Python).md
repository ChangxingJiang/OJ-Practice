# LeetCode题解(0842)：将数组拆分成斐波那契数列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/)（中等）

标签：字符串、贪心算法、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 224ms (12.77%) |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 40ms (96.72%)  |
| Ans 3 (Python) |            |            |                |

解法一（暴力解法）：

```python
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        N = len(S)

        # 判断数字是否合法
        def is_valid(n):
            return not (int(n) > 0 and n[0] == "0") and int(n) <= (2 ** 31 - 1)

        # 检查是否为斐波那契数列
        def is_fibonacci(m, n):
            if not is_valid(S[:m]) or not is_valid(S[m:n]):
                return False
            lst = [int(S[:m]), int(S[m:n])]
            idx1 = n
            while idx1 < N:
                nn = lst[-1] + lst[-2]  # 当前项
                s1 = str(nn)
                idx2 = idx1 + len(s1)
                s2 = S[idx1:idx2]
                if is_valid(s2) and s1 == s2:
                    lst.append(nn)
                    idx1 = idx2
                else:
                    return False
            return lst

        # 筛选所有的斐波那契数列
        for i in range(1, N):
            for j in range(i + 1, N):
                fibonacci_lst = is_fibonacci(i, j)
                if fibonacci_lst:
                    return fibonacci_lst
        return []
```

解法二（优化解法一）：

```python
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        MAX_INT = 2147483647
        N = len(S)

        # 判断数字是否合法
        def is_valid(n):
            return not (int(n) > 0 and n[0] == "0") and int(n) <= MAX_INT

        # 检查是否为斐波那契数列
        def is_fibonacci(m, n):
            if not is_valid(S[:m]) or not is_valid(S[m:n]):
                return False
            lst = [int(S[:m]), int(S[m:n])]
            idx1 = n
            while idx1 < N:
                nn = lst[-1] + lst[-2]  # 当前项
                s1 = str(nn)
                idx2 = idx1 + len(s1)
                s2 = S[idx1:idx2]
                if is_valid(s2) and s1 == s2:
                    lst.append(nn)
                    idx1 = idx2
                else:
                    return False
            return lst

        # 筛选所有的斐波那契数列
        for i in range(1, min(10, N)):
            for j in range(i + 1, min(i + 10, N)):
                fibonacci_lst = is_fibonacci(i, j)
                if fibonacci_lst:
                    return fibonacci_lst
        return []
```