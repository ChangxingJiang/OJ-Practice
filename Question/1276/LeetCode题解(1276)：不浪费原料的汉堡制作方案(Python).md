# LeetCode题解(1276)：不浪费原料的汉堡制作方案(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-burgers-with-no-waste-of-ingredients/)（中等）

标签：数学、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (55.43%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if 2 * cheeseSlices <= tomatoSlices <= 4 * cheeseSlices and tomatoSlices % 2 == 0:
            n1 = (tomatoSlices - 2 * cheeseSlices) // 2
            n2 = cheeseSlices - n1
            return [n1, n2]
        else:
            return []
```

