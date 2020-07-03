# LeetCode题解(1029)：两地最优调度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/two-city-scheduling/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 48ms (87.28%) |
| Ans 2 (Python) | $O(NlogN)$ | $O(N)$     | 44ms (97.01%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（自定义排序）：

```python
def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    def differ(cost):
        return cost[0] - cost[1]

    costs.sort(key=differ)

    center = len(costs) // 2
    ans = 0
    for i in range(center):
        ans += costs[i][0]
    for i in range(center, len(costs)):
        ans += costs[i][1]

    return ans
```

解法二（优雅化）：

```python
def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    costs.sort(key=lambda cost: cost[0] - cost[1])

    center = len(costs) // 2
    ans = 0
    for i in range(center):
        ans += costs[i][0] + costs[i + center][1]
    return ans
```