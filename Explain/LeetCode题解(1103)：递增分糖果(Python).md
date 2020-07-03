# LeetCode题解(1103)：递增分糖果(Python)

题目：[原题链接](https://leetcode-cn.com/problems/distribute-candies-to-people/)（简单）

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时      |
| -------------- | ------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(\sqrt{N})$ | $O(1)$     | 48ms (76.57%) |
| Ans 2 (Python) |               |            |               |
| Ans 3 (Python) |               |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（情景模拟）：

```python
def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    ans = [0 for _ in range(num_people)]
    num = 1
    idx = 0
    while candies:
        if idx >= num_people:
            idx -= num_people
        if candies >= num:
            ans[idx] += num
            candies -= num
            num += 1
            idx += 1
        else:
            ans[idx] += candies
            break
    return ans
```



