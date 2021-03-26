class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # 处理链表为空的情况
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        # 处理链表不为空的情况
        node = head
        already = False  # 是否已转过一周

        while True:
            # 处理只有一个元素的链表的情况
            if node == node.next:
                new = Node(insertVal, node.next)
                node.next = new
                break

            # 处理在链表中的情况
            elif node.val <= node.next.val:
                if node.val <= insertVal <= node.next.val:
                    new = Node(insertVal, node.next)
                    node.next = new
                    break
                else:
                    node = node.next

            # 处理到达链表末尾的情况
            else:
                if already:
                    new = Node(insertVal, node.next)
                    node.next = new
                    break
                else:
                    node = node.next

            if node == head:
                if not already:
                    already = True
                else:
                    new = Node(insertVal, node.next)
                    node.next = new
                    break

        return head


if __name__ == "__main__":
    n1 = Node(1)
    n3 = Node(3)
    n4 = Node(4)
    n1.next = n3
    n3.next = n4
    n4.next = n1
    print(Solution().insert(n3, 2))

    n1 = Node(1)
    n1.next = n1
    print(Solution().insert(n1, 0))

    n1 = Node(1)
    n3 = Node(3)
    n5 = Node(5)
    n1.next = n3
    n3.next = n5
    n5.next = n1
    print(Solution().insert(n1, 0))

    n1 = Node(1)
    n3 = Node(3)
    n5 = Node(5)
    n1.next = n3
    n3.next = n5
    n5.next = n1
    print(Solution().insert(n1, 3))

    n1 = Node(6)
    n3 = Node(6)
    n5 = Node(7)
    n6 = Node(1)
    n1.next = n3
    n3.next = n5
    n5.next = n6
    n6.next = n1
    print(Solution().insert(n1, 5))

    n1 = Node(3)
    n3 = Node(3)
    n5 = Node(3)
    n1.next = n3
    n3.next = n5
    n5.next = n1
    print(Solution().insert(n1, 0))
