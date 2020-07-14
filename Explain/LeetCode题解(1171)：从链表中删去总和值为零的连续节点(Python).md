# LeetCode题解(1171)：从链表中删去总和值为零的连续节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)（中等）

标签：链表、哈希表、数组-前缀和

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N)$     | 超出时间限制  |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 72ms (34.26%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 52ms (90.28%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def removeZeroSumSublists(self, head: ListNode) -> ListNode:
    # 将链表转换为数组
    values = []
    while head:
        values.append(head.val)
        head = head.next

    # 删除总和为0的连续结点
    for k in range(len(values), 0, -1):
        while True:
            for i in range(len(values) - k + 1):
                if sum(values[i:i + k]) == 0:
                    values = values[:i] + values[i + k:]
                    break
            else:
                break

    head = node = ListNode(0)
    for v in values:
        node.next = ListNode(v)
        node = node.next
    return head.next
```

解法二（哈希表双层循环）：

```python
def removeZeroSumSublists(self, head: ListNode) -> ListNode:
    ans = ListNode(0)
    ans.next = head

    while True:
        hashmap = {0: ans}
        sum_ = 0
        node = ans.next
        while node:
            sum_ += node.val
            if sum_ not in hashmap:
                hashmap[sum_] = node
            else:
                hashmap[sum_].next = node.next
                break
            node = node.next
        else:
            break

    return ans.next
```

解法三（哈希表两次遍历）：

```python
def removeZeroSumSublists(self, head: ListNode) -> ListNode:
    ans = ListNode(0)
    ans.next = head

    hashmap = {0: ans}
    sum_ = 0

    while head:
        sum_ += head.val
        hashmap[sum_] = head
        head = head.next

    head = ans
    sum_ = 0

    while head:
        sum_ += head.val
        head.next = hashmap[sum_].next
        head = head.next

    return ans.next
```