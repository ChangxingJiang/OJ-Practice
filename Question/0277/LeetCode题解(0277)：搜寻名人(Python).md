# LeetCode题解(0277)：搜寻名人(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-celebrity/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 1788ms (24.71%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 1536ms (81.03%) |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            for j in range(n):
                if i != j and (not knows(j, i) or knows(i, j)):
                    break
            else:
                return i
        return -1
```

解法二：

```python
class Solution:
    def findCelebrity(self, n: int) -> int:
        result = 0
        for i in range(n):
            # 如果result认识其他任何一个人，则说明result不是名人
            if knows(result, i):
                result = i

        for i in range(n):
            if result != i and (knows(result, i) or not knows(i, result)):
                return -1

        return result
```