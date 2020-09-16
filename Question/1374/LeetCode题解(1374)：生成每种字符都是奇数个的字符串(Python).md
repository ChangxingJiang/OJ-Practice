# LeetCode题解(1374)：生成每种字符都是奇数个的字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 36ms (85.79%) |
| Ans 2 (Python) | $O(1)$     | $O(1)$     | 40ms (68.38%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
def generateTheString(self, n: int) -> str:
    if n % 2 == 0:
        return "a" + "b" * (n - 1)
    else:
        return "a" * n
```

解法二：

```python
def generateTheString(self, n: int) -> str:
    return "a" * (n - 1) + ("b" if n % 2 == 0 else "a")
```