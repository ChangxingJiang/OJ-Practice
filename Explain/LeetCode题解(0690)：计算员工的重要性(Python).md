# LeetCode题解(0690)：计算员工的重要性(Python)

题目：[原题链接](https://leetcode-cn.com/problems/employee-importance/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 168ms (96.22%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 172ms (91.96%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def getImportance(self, employees: List['Employee'], id: int) -> int:
    hashmap = {}
    for employee in employees:
        hashmap[employee.id] = employee

    ans = 0
    sub = [id]
    while len(sub) > 0:
        k = sub.pop()
        employee = hashmap[k]
        ans += employee.importance
        sub.extend(employee.subordinates)

    return ans
```

解法二（递归）：

```python
def getImportance(self, employees: List['Employee'], id: int) -> int:
    hashmap = {}
    for employee in employees:
        hashmap[employee.id] = employee

    def helper(eid):
        e = hashmap[eid]
        return e.importance + sum([helper(s) for s in e.subordinates])

    return helper(id)
```