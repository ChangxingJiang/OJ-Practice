# LeetCode题解(0725)：尽可能长度相同地分隔链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/split-linked-list-in-parts/)（中等）

标签：链表、链表-双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(K)$     | 44ms (91.57%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
    # 计算链表长度
    size = 0
    node = root
    while node:
        node = node.next
        size += 1

    # 计算各个子串的长度
    avg_num = size // k
    plus_num = size % k

    ans = []
    node = root
    for i in range(k):
        num = avg_num + (i < plus_num)
        if num > 0:
            for _ in range(num - 1):
                node = node.next
            point = node.next
            node.next = None
            ans.append(root)
            root = node = point
        else:
            ans.append(None)

    return ans
```