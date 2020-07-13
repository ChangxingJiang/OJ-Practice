# LeetCode题解(0023)：合并K个排序链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/merge-k-sorted-lists/)（困难）

标签：链表、分治算法、堆排序

| 解法           | 时间复杂度                      | 空间复杂度                | 执行用时       |
| -------------- | ------------------------------- | ------------------------- | -------------- |
| Ans 1 (Python) | $O(N×K^2)$ : K为列表元素数量    | $O(1)$                    | 超出时间限制   |
| Ans 2 (Python) | $O(N×K×logK)$: K为列表元素数量  | $O(K)$                    | 176ms (21.45%) |
| Ans 3 (Python) | $O(NKlog(NK))$: K为列表元素数量 | $O(N×K)$: K为列表元素数量 | 76ms (93.93%)  |
| Ans 4 (Python) | $O(NKlog(NK))$: K为列表元素数量 | $O(N×K)$: K为列表元素数量 | 72ms (97.36%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（完全的暴力法）：

```python
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    ans = node = ListNode(0)
    while any(lists):
        min_node = ListNode(float("inf"))
        min_num = -1
        for i in range(len(lists)):
            if lists[i] is not None and lists[i].val < min_node.val:
                min_num = i
                min_node = ListNode(lists[i].val)
        lists[min_num] = lists[min_num].next
        node.next = min_node
        node = node.next
    return ans.next
```

解法二（分治算法）：

```python
class Solution:
    # 合并两个顺序链表
    @staticmethod
    def helper(listNode1, listNode2):
        ans = node = ListNode(0)
        while listNode1 and listNode2:
            if listNode1.val < listNode2.val:
                node.next = ListNode(listNode1.val)
                listNode1 = listNode1.next
                node = node.next
            else:
                node.next = ListNode(listNode2.val)
                listNode2 = listNode2.next
                node = node.next
        if listNode1 or listNode2:
            node.next = listNode1 or listNode2
        return ans.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        return Solution.helper(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))
```

解法三（取出所有元素排序）：

```python
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    values = []
    for linked in lists:
        while linked:
            values.append(linked.val)
            linked = linked.next
    values.sort()

    ans = node = ListNode(0)
    for v in values:
        node.next = ListNode(v)
        node = node.next

    return ans.next
```

解法四（解法三使用堆排序）：

```python
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    import heapq

    values = []
    for node in lists:
        while node:
            heapq.heappush(values, node.val)
            node = node.next

    ans = node = ListNode(0)
    while values:
        node.next = ListNode(heapq.heappop(values))
        node = node.next

    return ans.next
```