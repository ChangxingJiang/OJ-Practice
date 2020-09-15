# LeetCode题解(0028)：字符串模式匹配(Python)

题目：[题目链接](https://leetcode-cn.com/problems/implement-strstr/)（简单）

标签：字符串、KMP算法

| 解法           | 时间复杂度                   | 空间复杂度 | 执行用时      |
| -------------- | ---------------------------- | ---------- | ------------- |
| Ans 1 (Python) | --                           | --         | 40ms (78.00%) |
| Ans 2 (Python) | $O(N×M)$: 其中M为needle长度  | $O(1)$     | 52ms (34.29%) |
| Ans 3 (Python) | $O(N×M)$: 其中M为needle长度  | $O(1)$     | 44ms (61.00%) |
| Ans 4 (Python) | $O(N+M)$ : 其中M为needle长度 | $O(M)$     | 48ms (43.20%) |

解法一（使用Python原生index实现）：

```python
def strStr(self, haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
```

解法二（逐字符比较；每次查找失败转移到开始坐标的下一个字节）：

```python
def strStr(self, haystack: str, needle: str) -> int:
    needle_len = len(needle)

    # 处理长度为0的情况
    if needle_len == 0:
        return 0

    # 循环处理字符串
    j = 0
    i = 0
    while i < len(haystack):
        c = haystack[i]
        if c == needle[j]:
            if j == needle_len - 1:
                return i - j
            else:
                j += 1
            i += 1
        else:
            i = i - j + 1
            j = 0
    return -1
```

解法三（遍历字符串，查看每个坐标是否为needle的起始坐标）：

```python
def strStr(self, haystack: str, needle: str) -> int:
    len_h = len(haystack)
    len_n = len(needle)
    for i in range(len_h - len_n + 1):
        if haystack[i: i + len_n] == needle:
            return i
    return -1
```

解法四（KMP算法）：

```python
def strStr(self, haystack: str, needle: str) -> int:
    def get_next_val(t):
        """通过计算返回子串t的next数组"""
        i = 0
        j = -1
        next = [-1] * len(t)
        while i < len(t) - 1:
            if j == -1 or t[i] == t[j]:
                i += 1
                j += 1
                if t[i] != t[j]:
                    next[i] = j
                else:
                    next[i] = next[j]
            else:
                j = next[j]  # 若字符不相同，则j值回溯
        return next

    i = 0  # i用于主串s中当前位置下标，若pos不为1则从pos位置开始匹配
    j = 0  # j用于子串t中当前位置下标值
    next = get_next_val(needle)
    while i < len(haystack) and j < len(needle):
        if j == -1 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j >= len(needle):
        return i - len(needle)
    else:
        return -1
```