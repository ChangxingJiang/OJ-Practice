# LeetCode题解(1700)：无法吃午餐的学生数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-students-unable-to-eat-lunch/)（简单）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N+M)$   | $O(1)$     | 32ms (95.19%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [students.count(0), students.count(1)]
        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
            else:
                break
        return sum(count)
```

