# LeetCode题解(0205)：判断两个字符串是否是同构的(Python)

题目：[原题链接](https://leetcode-cn.com/problems/isomorphic-strings/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 44ms (>90.65%) |
| Ans 2 (Python) | O(n)       | O(1)       | 48ms (>80.32%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用哈希表存储对应关系）：

```python
def isIsomorphic(self, s: str, t: str) -> bool:
    size_s = len(s)
    size_t = len(t)
    if size_s != size_t:
        return False

    hashmap = {}
    for i in range(size_s):
        c = s[i]
        if c not in hashmap:
            if t[i] not in hashmap.values():
                hashmap[c] = t[i]
            else:
                return False
        if t[i] != hashmap[c]:
            return False

    return True
```

解法二（使用两个哈希表，不检索值是否存在于哈希表的值中）：

```python
def isIsomorphic(self, s: str, t: str) -> bool:
    size_s = len(s)
    size_t = len(t)
    if size_s != size_t:
        return False

    hashmap_s = {}
    hashmap_t = {}
    for i in range(size_s):
        c_s = s[i]
        c_t = t[i]
        at_s = c_s in hashmap_s
        at_t = c_t in hashmap_t
        if at_s and at_t:
            if hashmap_s[c_s] != hashmap_t[c_t]:
                return False
        elif (at_s and at_t) != (at_s or at_t):
            return False
        else:
            hashmap_s[c_s] = i
            hashmap_t[c_t] = i

    return True
```