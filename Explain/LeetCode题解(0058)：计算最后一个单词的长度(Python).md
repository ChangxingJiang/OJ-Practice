# LeetCode题解(0058)：字符串中最后一个单词的长度(Python)

题目：[题目链接](https://leetcode-cn.com/problems/length-of-last-word/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| :------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 40ms (65.82%) |
| Ans 2 (Python) | --         | --         | 36ms (86.50%) |

解法一（使用split拆分）：

```python
def lengthOfLastWord(self, s: str) -> int:
    for w in s.split(" ")[::-1]:
        len_w = len(w)
        if len_w != 0:
            return len_w
    return 0
```

解法二（在解法一的基础上使用strip()移除首尾空格）：

```python
def lengthOfLastWord(self, s: str) -> int:
    s = s.strip(" ")
    if s:
        return len(s.split(" ")[-1])
    else:
        return 0
```