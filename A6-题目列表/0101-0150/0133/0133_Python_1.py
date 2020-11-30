class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        pass


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    print(Solution().cloneGraph(n1))

    n1 = Node(1)
    print(Solution().cloneGraph(n1))

    print(Solution().cloneGraph(None))

    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors = [n2]
    n2.neighbors = [n1]
    print(Solution().cloneGraph(n1))
