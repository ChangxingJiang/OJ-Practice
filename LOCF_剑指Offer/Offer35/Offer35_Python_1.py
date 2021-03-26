from toolkit import ListNode


class Node(ListNode):
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        super().__init__(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ans = node = Node(0)

        # 第一次遍历生成链表和哈希表
        now = head
        hashmap = {}
        while now:
            node.next = Node(now.val)
            hashmap[now] = node.next
            node = node.next
            now = now.next

        # 第二次遍历生成链表随机指针
        now = head
        node = ans.next
        while now:
            if now.random:
                node.random = hashmap[now.random]
            node = node.next
            now = now.next

        return ans.next


if __name__ == "__main__":
    pass
