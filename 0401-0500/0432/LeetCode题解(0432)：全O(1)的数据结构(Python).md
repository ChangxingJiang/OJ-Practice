# LeetCode题解(0432)：全O(1)的数据结构(Python)

题目：[原题链接](https://leetcode-cn.com/problems/all-oone-data-structure/)（困难）

标签：设计、链表

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时       |
| -------------- | -------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | dec = $O(N)$ ; 其他操作 = $O(1)$ | $O(N)$     | 5364ms (5.71%) |
| Ans 2 (Python) | 所有操作 = $O(1)$                | $O(N)$     | 80ms (75.24%)  |
| Ans 3 (Python) |                                  |            |                |

解法一：

```python
class AllOne:
    def __init__(self):
        self.buckets = [set()]
        self.count = collections.Counter()
        self.max_idx = 0
        self.min_idx = 0

    def inc(self, key: str) -> None:
        # 移除之前的频数
        idx = self.count[key]
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

        # 更新最小值
        self.min_idx = min(self.min_idx, idx)
        if len(self.buckets[idx]) == 0 and self.min_idx == idx:
            self.min_idx += 1

        # 插入新的频数
        idx += 1
        if len(self.buckets) <= idx:
            self.buckets.append(set())
        self.buckets[idx].add(key)

        # 更新位置记录
        self.count[key] += 1

        # 更新最大值
        self.max_idx = max(self.max_idx, idx)

    def dec(self, key: str) -> None:
        # 如果没有该元素，不做任何事
        if self.count[key] == 0:
            return

        # 移除之前的频数
        idx = self.count[key]
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

        # 更新最大值
        if len(self.buckets[idx]) == 0 and self.max_idx == idx:
            self.max_idx -= 1

        # 插入新的频数
        idx -= 1
        if idx > 0:
            self.buckets[idx].add(key)

        # 更新位置记录
        self.count[key] -= 1
        if self.count[key] == 0:
            del self.count[key]

        # 更新最小值（未实现真正的O(1)）
        if len(self.buckets[idx + 1]) == 0 and self.min_idx == idx + 1:
            self.min_idx -= 1
        if self.min_idx == 0 and self.max_idx >= 1:
            for i in range(1, self.max_idx + 1):
                if len(self.buckets[i]) > 0:
                    self.min_idx = i
                    break

    def getMaxKey(self) -> str:
        if self.max_idx > 0:
            res = self.buckets[self.max_idx].pop()
            self.buckets[self.max_idx].add(res)
            return res
        else:
            return ""

    def getMinKey(self) -> str:
        if self.min_idx > 0:
            res = self.buckets[self.min_idx].pop()
            self.buckets[self.min_idx].add(res)
            return res
        else:
            return ""
```

解法二：

```python
class AllOne:
    _MOD = 10 ** 9

    class Node:
        def __init__(self, idx=0, lst=None, next=None, prev=None):
            self.idx = idx
            self.lst = lst if lst else set()
            self.next = next
            self.prev = prev

    def __init__(self):
        # 双向链表
        self.head = self.Node(idx=-self._MOD)
        self.tail = self.Node(idx=self._MOD)
        self.head.next, self.tail.prev = self.tail, self.head

        # key位置记录器
        self.mark = {}

    def inc(self, key: str) -> None:
        # 处理新key的情况
        if key not in self.mark:
            # 存在times=1的节点
            if self.head.next.idx == 1:
                self.head.next.lst.add(key)
                self.mark[key] = self.head.next
            # 不存在times=1的节点
            else:
                node = self.Node(idx=1, lst={key}, next=self.head.next, prev=self.head)
                self.head.next.prev, self.head.next = node, node
                self.mark[key] = node

        # 处理旧key的情况
        else:
            node = self.mark[key]
            # 当前节点只有一个key的情况
            if len(node.lst) == 1:
                # 存在times+1的节点
                if node.next.idx == node.idx + 1:
                    node.next.lst.add(key)
                    self.mark[key] = node.next
                    prev, next = node.prev, node.next
                    prev.next, next.prev = next, prev
                # 不存在times+1的节点
                else:
                    node.idx += 1

            # 当前节点不只一个key的情况
            else:
                node.lst._remove(key)
                # 存在times+1的节点
                if node.next.idx == node.idx + 1:
                    node.next.lst.add(key)
                    self.mark[key] = node.next
                # 不存在times+1的节点
                else:
                    prev, next = node, node.next
                    new = self.Node(idx=node.idx + 1, lst={key}, next=next, prev=prev)
                    prev.next, next.prev = new, new
                    self.mark[key] = new

    def dec(self, key: str) -> None:
        # 处理新key的情况
        if key not in self.mark:
            return

        # 处理旧key的情况
        else:
            node = self.mark[key]

            # 处理移除后key消失的情况
            if node.idx == 1:
                del self.mark[key]

                # 当前节点只有一个key的情况
                if len(node.lst) == 1:
                    prev, next = node.prev, node.next
                    prev.next, next.prev = next, prev

                # 当前节点不只一个key的情况
                else:
                    node.lst._remove(key)

            else:
                # 当前节点只有一个key的情况
                if len(node.lst) == 1:
                    # 存在times-1的节点
                    if node.prev.idx == node.idx - 1:
                        node.prev.lst.add(key)
                        self.mark[key] = node.prev
                        prev, next = node.prev, node.next
                        prev.next, next.prev = next, prev
                    # 不存在times+1的节点
                    else:
                        node.idx -= 1

                # 当前节点不只一个key的情况
                else:
                    node.lst._remove(key)
                    # 存在times+1的节点
                    if node.prev.idx == node.idx - 1:
                        node.prev.lst.add(key)
                        self.mark[key] = node.prev
                    # 不存在times+1的节点
                    else:
                        prev, next = node.prev, node
                        new = self.Node(idx=node.idx - 1, lst={key}, next=next, prev=prev)
                        prev.next, next.prev = new, new
                        self.mark[key] = new

    def getMaxKey(self) -> str:
        if self.head.next != self.tail:
            res = self.tail.prev.lst.pop()
            self.tail.prev.lst.add(res)
            return res
        else:
            return ""

    def getMinKey(self) -> str:
        if self.head.next != self.tail:
            res = self.head.next.lst.pop()
            self.head.next.lst.add(res)
            return res
        else:
            return ""

    def __repr__(self):
        node = self.head.next
        ans = []
        while node != self.tail:
            ans.append(str(node.idx) + ":" + str(node.lst))
            node = node.next
        return "->".join(ans)
```

