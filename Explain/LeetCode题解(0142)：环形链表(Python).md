# LeetCode题解(0142)：环形链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/linked-list-cycle-ii/)（中等）

标签：链表、链表-双指针、链表-快慢针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (98.07%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（快慢针）：

> 思路：
>
> 设从起点到入口的距离为x，慢针进入环后行进的距离为y（即从入口走到交点的距离），从慢针与快针的交点继续向前走到入口的距离为z（即从交点再走回入口的距离。由快慢针速度差2倍得如下方程：$2(x+y)=x+y+z+y$
>
> 解得：$x=z$
>
> 由此，从起点和交点开始向前走，相交点即是入口。

```python
def detectCycle(self, head: ListNode) -> ListNode:
    # 快慢针判断是否有环
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    # 找到入口
    node1 = slow
    node2 = head
    while node1 != node2:
        node1 = node1.next
        node2 = node2.next

    return node1
```