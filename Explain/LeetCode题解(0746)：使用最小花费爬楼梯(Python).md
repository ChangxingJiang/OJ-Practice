# LeetCode题解(0746)：使用最小花费爬楼梯(Python)

题目：[原题链接](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 72ms (76.61%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 72ms (76.61%) |
| Ans 3 (Python) | $O(N)$     | $O(1)$     | 64ms (96.90%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def minCostClimbingStairs(self, cost: List[int]) -> int:
    total = [cost[0], cost[1]]
    for i in range(2, len(cost)):
        total.append(min(total[i - 2], total[i - 1]) + cost[i])
    return min(total[-1], total[-2])
```

解法二：

```python
def minCostClimbingStairs(self, cost: List[int]) -> int:
    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 2], cost[i - 1])
    return min(cost[-1], cost[-2])
```

解法三：

```python
def minCostClimbingStairs(self, cost: List[int]) -> int:
    f1 = f2 = 0
    for i in cost:
        f1, f2 = min(f1, f2) + i, f1
    return min(f1, f2)
```