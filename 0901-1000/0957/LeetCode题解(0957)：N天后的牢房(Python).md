# LeetCode题解(0957)：N天后的牢房(Python)

题目：[原题链接](https://leetcode-cn.com/problems/prison-cells-after-n-days/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^8)$   | $O(2^8)$   | 52ms (59.18%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        count = {"".join(str(c) for c in cells): 0}
        lst = [cells]
        i = 0
        while True:
            i += 1

            # 计算调换
            new = [0] * 8
            for j in range(1, 7):
                if cells[j - 1] == cells[j + 1]:
                    new[j] = 1
                else:
                    new[j] = 0
            cells = new
            lst.append(cells)

            s = "".join(str(c) for c in cells)

            if s in count:
                start = count[s]
                circle = i - count[s]  # 循环周期
                break
            else:
                count[s] = i

        return lst[(N - start) % circle + start]
```