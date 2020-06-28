# LeetCode题解(0387)：查找字符串中的第一个唯一字符的索引(Python)

题目：[原题链接](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 204ms (27.88%) |
| Ans 2 (Python) | O(n)       | O(n)       | 172ms (38.60%) |
| Ans 3 (Python) | --         | --         | 100ms (85.37%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表实现）：

```python
def firstUniqChar(self, s: str) -> int:
    hashmap = {}
    repeat = []
    for i in range(len(s)):
        c = s[i]
        if c not in repeat:
            if c not in hashmap:
                hashmap[c] = i
            else:
                del hashmap[c]
                repeat.append(c)
    if len(hashmap.values()) > 0:
        return min(hashmap.values())
    else:
        return -1
```

解法二（先找出目标字符，再获取目标字符的索引）：

```python
def firstUniqChar(self, s: str) -> int:
    once = []
    repeat = []
    for c in s:
        if c not in repeat:
            if c not in once:
                once.append(c)
            else:
                once.remove(c)
                repeat.append(c)
    if len(once) > 0:
        return s.index(once[0])
    else:
        return -1
```

解法三（Pythonic）：

```python
def firstUniqChar(self, s: str) -> int:
    count = collections.Counter(s)
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    else:
        return -1
```