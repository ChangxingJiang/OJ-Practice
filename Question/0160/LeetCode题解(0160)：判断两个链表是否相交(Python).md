# LeetCode题解：0160（相交链表）

题目：[题目链接](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)（简单）

标签：链表、链表-相交链表、链表-双指针、链表-快慢针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| :------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 216ms (25.96%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 184ms (75.53%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 180ms (84.94%) |

解法一（使用Python的list直接实现）：

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    hashmap = set()
    while headA:
        hashmap.add(headA)
        headA = headA.next
    while headB:
        if headB in hashmap:
            return headB
        headB = headB.next
```

解法二（双指针；因为双指针经过长度相同，因此一定会同时到达终点）：

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if headA and headB:
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA
```

解法三（双指针）：

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    nodeA, nodeB = headA, headB
    while nodeA != nodeB:
        nodeA = nodeA.next if nodeA else headB
        nodeB = nodeB.next if nodeB else headA
    return nodeA
```

