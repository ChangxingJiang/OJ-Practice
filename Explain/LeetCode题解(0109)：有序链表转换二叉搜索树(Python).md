# LeetCode题解(0109)：有序链表转换二叉搜索树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/)（中等）

标签：链表、链表-双指针、链表-快慢针、二叉树-二叉搜索树、二叉树-递归、二叉树-中序遍历、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(logN)$  | 76ms (92.95%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 76ms (92.95%) |
| Ans 3 (Python) | $O(N)$     | $O(logN)$  | 76ms (92.95%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归）：

```python
def sortedListToBST(self, head: ListNode) -> TreeNode:
    # 边界处理
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)

    # 二分处理
    slow = head
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    tree = TreeNode(slow.next.val)
    tree.right = self.sortedListToBST(slow.next.next)
    slow.next = None
    tree.left = self.sortedListToBST(head)
    return tree
```

解法二（转换为数组）：

```python
def sortedListToBST(self, head: ListNode) -> TreeNode:
    # 异常情况处理
    if not head:
        return None

    # 二分处理
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

    # 定义递归函数
    def helper(vals):
        # 边界处理
        if len(vals) == 0:
            return None
        if len(vals) == 1:
            return TreeNode(vals[0])

        # 二分处理
        mid = len(vals) // 2
        tree = TreeNode(vals[mid])
        tree.left = helper(vals[:mid])
        tree.right = helper(vals[mid + 1:])
        return tree

    # 递归得到结果
    return helper(values)
```

解法三（利用中序遍历的性质：模拟中序遍历）：

```python
def sortedListToBST(self, head: ListNode) -> TreeNode:
    # 异常情况处理
    if not head:
        return None

    # 计算链表长度
    size = 1
    node = head
    while node.next:
        node = node.next
        size += 1
    print(size)

    # 定义递归函数
    def helper(start, end):
        nonlocal head

        # 边界处理
        if start > end:
            return None

        # 递归处理
        mid = (end + start) // 2
        left = helper(start, mid - 1)  # 处理左半部分
        tree = TreeNode(head.val)  # 取出当前树的值（链表刚好遍历的这个位置）
        tree.left = left
        head = head.next
        tree.right = helper(mid + 1, end)  # 处理右半部分
        return tree

    # 递归得到结果
    return helper(0, size - 1)
```