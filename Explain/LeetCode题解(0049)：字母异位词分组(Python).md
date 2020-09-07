# LeetCode题解(0049)：字母异位词依据组成字母分组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/group-anagrams/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时      |
| -------------- | -------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×MlogM)$ : 其中M为字符串长度 | $O(N×M)$   | 48ms (98.67%) |
| Ans 2 (Python) |                                  |            |               |
| Ans 3 (Python) |                                  |            |               |

解法一（排序法）：

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hashmap = {}
    for s in strs:
        ordered = "".join(sorted(s))
        if ordered not in hashmap:
            hashmap[ordered] = [s]
        else:
            hashmap[ordered].append(s)
    return [value for value in hashmap.values()]
```