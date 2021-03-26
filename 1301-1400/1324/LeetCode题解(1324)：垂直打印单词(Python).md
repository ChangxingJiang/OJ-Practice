# LeetCode题解(1324)：垂直打印列表中的单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/print-words-vertically/)（中等）

标签：字符串

| 解法           | 时间复杂度                              | 空间复杂度 | 执行用时 |
| -------------- | --------------------------------------- | ---------- | -------- |
| Ans 1 (Python) | $O(N×max(|S|))$ : 其中S为字符串最大长度 | $O(N×max(  | S        |
| Ans 2 (Python) |                                         |            |          |
| Ans 3 (Python) |                                         |            |          |

解法一：

```python
class Solution:
    def printVertically(self, s: str) -> List[str]:
        return ["".join(elem).rstrip() for elem in itertools.zip_longest(*s.split(), fillvalue=" ")]
```