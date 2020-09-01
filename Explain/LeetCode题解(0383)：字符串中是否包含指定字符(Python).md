# LeetCode题解(0383)：判断报纸中的字是否够写赎金信(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ransom-note/)（简单）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(M+N)$   | $O(N)$     | 72ms (51.08%) |
| Ans 2 (Python) | $O(M+N)$   | $O(1)$     | 80ms (40.28%) |
| Ans 3 (Python) | --         | $O(1)$     | 36ms (99.46%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    hashmap = {}

    # 遍历统计杂志中个字母的数量
    for c in magazine:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1

    # 遍历赎金信判断杂志中字母数量是否充足
    for c in ransomNote:
        if c not in hashmap:
            return False
        elif hashmap[c] <= 0:
            return False
        else:
            hashmap[c] -= 1
    else:
        return True
```

解法二（依据字母使用列表存储数据）：

```python
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    hashmap = [0] * 26

    # 遍历统计杂志中个字母的数量
    for c in magazine:
        hashmap[ord(c) - 97] += 1

    # 遍历赎金信判断杂志中字母数量是否充足
    for c in ransomNote:
        if hashmap[ord(c) - 97] <= 0:
            return False
        else:
            hashmap[ord(c) - 97] -= 1
    else:
        return True
```

解法三（直接从杂志中裁剪）：

![LeetCode题解(0383)：截图1](LeetCode题解(0383)：截图1.png)

```python
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    for c in ransomNote:
        if c in magazine:
            magazine = magazine.replace(c, "", 1)
        else:
            return False
    else:
        return True
```



