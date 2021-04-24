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


if __name__ == "__main__":
    obj = AllOne()
    obj.inc("a")
    obj.inc("b")
    obj.inc("b")
    obj.inc("c")
    obj.inc("c")
    obj.inc("c")
    obj.dec("b")
    obj.dec("b")
    print(obj.getMaxKey())  # c
    obj.dec("a")
    print(obj.getMaxKey())  # c
    print(obj.getMinKey())  # c

    obj = AllOne()
    obj.inc("hello")
    obj.inc("hello")
    print(obj.getMaxKey())  # hello
    print(obj.getMinKey())  # hello
    obj.inc("leet")
    print(obj.getMaxKey())  # hello
    print(obj.getMinKey())  # leet
