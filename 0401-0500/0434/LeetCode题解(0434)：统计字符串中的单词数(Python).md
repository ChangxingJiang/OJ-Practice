# LeetCode题解(0434)：统计字符串中的单词数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-segments-in-a-string/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (86.67%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 36ms (86.67%) |

解法一：

```Python
def countSegments(self, s: str) -> int:
    return sum([1 for i in re.split(" +", s) if len(i) > 0])
```

解法二：

```python
def countSegments(self, s: str) -> int:
    not_space = False
    ans = 0
    for c in s:
        if c != " ":
            not_space = True
        else:
            if not_space:
                ans += 1
                not_space = False
    ans += not_space
    return ans
```