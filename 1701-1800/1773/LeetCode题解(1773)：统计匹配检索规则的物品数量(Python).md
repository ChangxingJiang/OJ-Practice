# LeetCode题解(1773)：统计匹配检索规则的物品数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-items-matching-a-rule/)（简单）

标签：数组、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 64ms (24.19%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2

        ans = 0
        for item in items:
            if item[index] == ruleValue:
                ans += 1
        return ans
```

