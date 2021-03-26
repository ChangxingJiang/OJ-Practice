# LeetCode题解(0014)：多个字符串的最长公共前缀(Python)

题目：[题目链接](https://leetcode-cn.com/problems/longest-common-prefix/)（简单）

标签：字符串

| 解法           | 时间复杂度                   | 空间复杂度 | 执行用时      |
| -------------- | ---------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×M)$ : 其中M为字符串数量 | $O(1)$     | 40ms (78.57%) |
| Ans 2 (Python) | $O(N×M)$ : 其中M为字符串数量 | $O(1)$     | 32ms (97.34%) |

解法一（粗暴比较）：

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    # 处理空列表的情况
    if len(strs) == 0:
        return ""

    # 统计最长的字符串长度
    min_len = min([len(s) for s in strs])

    # 处理只有空字符串的情况
    if min_len == 0:
        return ""

    for i in range(min_len):
        t = strs[0][i]
        for s in strs:
            if s[i] != t:
                return strs[0][0:i]
    return strs[0][0:min_len]
```

解法二（转换组的方向进行比较）：

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    ans = ""
    for s in zip(*strs):
        if len(set(s)) != 1:
            return ans
        else:
            ans += s[0]
    return ans
```