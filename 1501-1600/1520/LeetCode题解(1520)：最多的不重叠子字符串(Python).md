# LeetCode题解(1520)：最多的不重叠子字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-substrings/)（困难）

标签：数组、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(S)$     | $O(1)$     | 3416ms (35.81%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # 计算所有字母的第一个位置和最后一个位置
        # O(S)
        positions = [[-1, -1]] * 26
        for i, ch in enumerate(s):
            idx1 = ord(ch) - 97
            if positions[idx1] == [-1, -1]:
                positions[idx1] = [i, i]
            else:
                positions[idx1][1] = i

        # 26次遍历调整所有字母的左右范围
        # O(26×26×S) = O(S)
        for idx1 in range(26):
            if positions[idx1] != [-1, -1]:
                j = positions[idx1][0]
                while j <= positions[idx1][1]:
                    idx2 = ord(s[j]) - 97
                    if positions[idx1][0] <= positions[idx2][0] and positions[idx2][1] <= positions[idx1][1]:
                        pass
                    else:
                        positions[idx1][0] = min(positions[idx1][0], positions[idx2][0])
                        positions[idx1][1] = max(positions[idx1][1], positions[idx2][1])
                        j = positions[idx1][0]
                    j += 1

        # 过滤不存在的范围和重复的范围
        # O(26) = O(1)
        positions = [tuple(position) for position in positions if position != [-1, -1]]

        # 排序所有的范围
        # O(26log26) = O(1)
        positions = list(sorted(set(positions), key=lambda x: (x[1], x[0])))

        # 贪心选择字符串，得到结果
        # O(26) = O(1)
        ans = []
        end = -1
        for left, right in positions:
            if end == -1 or left > end:
                end = right
                ans.append(s[left:right + 1])
        return ans
```