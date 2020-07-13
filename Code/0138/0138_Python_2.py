from toolkit import ListNode


class Node(ListNode):
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        super().__init__(x)
        self.next = next
        self.random = random


class Solution:
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


if __name__ == "__main__":
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1
    print(Solution().copyRandomList(n1))
