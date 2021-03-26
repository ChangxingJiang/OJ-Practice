# LeetCode题解(1046)：最后一块石头的重量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/last-stone-weight/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 36ms (91.72%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（模拟情景）：

```python
def lastStoneWeight(self, stones: List[int]) -> int:
    stones.sort()
    while len(stones) > 1:
        stone1 = stones.pop(-1)
        stone2 = stones.pop(-1)
        new_stone = stone1 - stone2

        idx1 = 0
        idx2 = len(stones)
        while idx1 < idx2:
            mid = (idx1 + idx2) // 2
            if new_stone > stones[mid]:
                idx1 = mid + 1
            elif new_stone < stones[mid]:
                idx2 = mid
            else:
                idx1 = mid
                break
        stones.insert(idx1, new_stone)

    return stones[0]
```