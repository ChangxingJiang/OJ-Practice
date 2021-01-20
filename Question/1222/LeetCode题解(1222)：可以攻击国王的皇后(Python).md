# LeetCode题解(1222)：可以攻击国王的皇后(Python)

题目：[原题链接](https://leetcode-cn.com/problems/queens-that-can-attack-the-king/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(8^2)$   | $O(1)$     | 36ms (97.37%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = {(i, j) for i, j in queens}

        ans = []

        # 下
        i = king[0] + 1
        while i < 8:
            if (i, king[1]) in queens:
                ans.append([i, king[1]])
                break
            i += 1

        # 上
        i = king[0] - 1
        while i >= 0:
            if (i, king[1]) in queens:
                ans.append([i, king[1]])
                break
            i -= 1

        # 右
        j = king[1] + 1
        while j < 8:
            if (king[0], j) in queens:
                ans.append([king[0], j])
                break
            j += 1

        # 左
        j = king[1] - 1
        while j >= 0:
            if (king[0], j) in queens:
                ans.append([king[0], j])
                break
            j -= 1

        # 右下
        i = king[0] + 1
        j = king[1] + 1
        while i < 8 and j < 8:
            if (i, j) in queens:
                ans.append([i, j])
                break
            i += 1
            j += 1

        # 左上
        i = king[0] - 1
        j = king[1] - 1
        while i >= 0 and j >= 0:
            if (i, j) in queens:
                ans.append([i, j])
                break
            i -= 1
            j -= 1

        # 左下
        i = king[0] + 1
        j = king[1] - 1
        while i < 8 and j >= 0:
            if (i, j) in queens:
                ans.append([i, j])
                break
            i += 1
            j -= 1

        # 右上
        i = king[0] - 1
        j = king[1] + 1
        while i >= 0 and j < 8:
            if (i, j) in queens:
                ans.append([i, j])
                break
            i -= 1
            j += 1

        return ans
```

