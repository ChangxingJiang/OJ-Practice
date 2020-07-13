# LeetCode题解(0138)：复制带随机指针的链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/copy-list-with-random-pointer/)（中等）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 52ms (42.35%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 36ms (98.50%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用内置函数）：

```python
def copyRandomList(self, head: 'Node') -> 'Node':
    import copy
    return copy.deepcopy(head)
```

解法二（存储旧结点和新结点的对应关系）：

```python
def copyRandomList(self, head: 'Node') -> 'Node':
    # 处理特殊情况
    if not head:
        return None

    # 生成节点并存储在字典中
    hashmap = {}
    node = head
    while node:
        hashmap[node] = Node(node.val)
        node = node.next

    # 生成next和random指针
    node = head
    while node:
        if node.next:
            hashmap[node].next = hashmap[node.next]
        if node.random:
            hashmap[node].random = hashmap[node.random]
        node = node.next

    # 返回结果
    return hashmap[head]
```