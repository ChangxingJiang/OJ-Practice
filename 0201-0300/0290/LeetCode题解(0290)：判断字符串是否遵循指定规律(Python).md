# LeetCode题解(0290)：判断字符串是否遵循指定规律(Python)

题目：[原题链接](https://leetcode-cn.com/problems/word-pattern/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(n)       | 32ms (94.70%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def wordPattern(self, pattern: str, str: str) -> bool:
    words = str.split(" ")
    if len(pattern) != len(words):
        return False
    hashmap = {}
    for i in range(len(pattern)):
        if pattern[i] not in hashmap:
            if words[i] not in hashmap.values():
                hashmap[pattern[i]] = words[i]
            else:
                return False
        else:
            if hashmap[pattern[i]] != words[i]:
                return False
    else:
        return True
```