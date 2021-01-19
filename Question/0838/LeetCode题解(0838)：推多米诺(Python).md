# LeetCode题解(0838)：推多米诺(Python)

题目：[原题链接](https://leetcode-cn.com/problems/push-dominoes/)（中等）

标签：动态规划、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 192ms (37.89%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        size = len(dominoes)

        lefts = {i for i in range(size) if dominoes[i] == "L"}
        rights = {i for i in range(size) if dominoes[i] == "R"}

        while lefts or rights:
            new_lefts = set()
            for left in lefts:
                if left == 0:
                    continue
                if left > 0 and (dominoes[left - 1] == "R" or dominoes[left - 1] == "L"):
                    continue
                if left > 1 and dominoes[left - 2] == "R":
                    continue
                else:
                    dominoes[left - 1] = "L"
                    new_lefts.add(left - 1)
            new_rights = set()
            for right in rights:
                if right == size - 1:
                    continue
                if right < size - 1 and (dominoes[right + 1] == "L" or dominoes[right + 1] == "R"):
                    continue
                if right < size - 2 and dominoes[right + 2] == "L":
                    if right + 2 in new_lefts:
                        dominoes[right + 1] = "R"
                else:
                    dominoes[right + 1] = "R"
                    new_rights.add(right + 1)
            lefts, rights = new_lefts, new_rights

        return "".join(dominoes)
```

