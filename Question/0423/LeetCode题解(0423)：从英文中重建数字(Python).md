# LeetCode题解(0423)：从英文中重建数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/)（中等）

标签：数学、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (87.69%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)

        ans = [0] * 10
        ans[0] = count["z"]
        ans[2] = count["w"]
        ans[4] = count["u"]
        ans[6] = count["x"]
        ans[8] = count["g"]
        ans[5] = count["f"] - ans[4]
        ans[3] = count["h"] - ans[8]
        ans[7] = count["s"] - ans[6]
        ans[9] = count["i"] - ans[5] - ans[6] - ans[8]
        ans[1] = count["n"] - ans[7] - 2 * ans[9]

        return "".join(str(i) * n for i, n in enumerate(ans))
```

