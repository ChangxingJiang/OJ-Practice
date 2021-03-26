# LeetCode题解(1643)：第K条最小指令(Python)

题目：[原题链接](https://leetcode-cn.com/problems/kth-smallest-instructions/)（困难）

标签：数学、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时 |
| -------------- | ---------- | ---------- | -------- |
| Ans 1 (Python) | $O(M+N)$   | $O(1)$     | 40ms     |
| Ans 2 (Python) |            |            |          |
| Ans 3 (Python) |            |            |          |

解法一：

```python
def comb(n, m):
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        step_h = destination[1]  # 向右的步数
        step_v = destination[0]  # 向下的步数

        ans = []

        while k and step_h and step_v:
            nums = comb(step_h + step_v - 1, step_v)  # 如果当前位置为H，后续能够提供的最大数量
            # print(step_h + step_v - 1, step_v, "->", nums)
            if k > nums:
                ans.append("V")
                k -= nums
                step_v -= 1
            else:
                ans.append("H")
                step_h -= 1
            # print(ans)

        ans += ["H"] * step_h
        ans += ["V"] * step_v

        return "".join(ans)
```

