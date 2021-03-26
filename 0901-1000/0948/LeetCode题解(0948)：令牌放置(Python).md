# LeetCode题解(0948)：令牌放置(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bag-of-tokens/)（中等）

标签：贪心算法、排序、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 48ms (57.23%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        tokens = collections.deque(tokens)

        mark = 0
        while tokens:
            # 第一次补充积分
            if not mark:
                if power > tokens[0]:
                    power -= tokens.popleft()
                    mark += 1
                    continue
                else:
                    break

            # 补充能量
            if power < tokens[0]:
                if len(tokens) > 1:
                    power += tokens.pop()
                    mark -= 1
                else:
                    break

            else:
                power -= tokens.popleft()
                mark += 1

        return mark
```

