# LeetCode题解(1634)：求两个多项式链表的和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/add-two-polynomials-represented-as-linked-lists/)（中等）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(N1+n2)$ | 444ms (100.00%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        ans = node = PolyNode(0, 0)
        while poly1 and poly2:
            if poly1.power > poly2.power:
                node.next = PolyNode(poly1.coefficient, poly1.power)
                node = node.next
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                node.next = PolyNode(poly2.coefficient, poly2.power)
                node = node.next
                poly2 = poly2.next
            else:
                coefficient = poly1.coefficient + poly2.coefficient
                if coefficient != 0:
                    node.next = PolyNode(coefficient, poly1.power)
                    node = node.next
                poly1 = poly1.next
                poly2 = poly2.next
        if poly1:
            node.next = poly1
        if poly2:
            node.next = poly2
        return ans.next
```