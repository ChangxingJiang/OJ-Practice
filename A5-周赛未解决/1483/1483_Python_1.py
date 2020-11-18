from typing import List


# 设计
# 每次查询:O(N)


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.array = parent

    def getKthAncestor(self, node: int, k: int) -> int:
        if k == 0:
            return node
        elif node == 0:
            return -1
        else:
            return self.getKthAncestor(self.array[node], k - 1)


if __name__ == "__main__":
    tree_ancestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(tree_ancestor.getKthAncestor(3, 1))  # 1
    print(tree_ancestor.getKthAncestor(5, 2))  # 0
    print(tree_ancestor.getKthAncestor(6, 3))  # -1

    print()

    tree_ancestor = TreeAncestor(5, [-1, 0, 0, 1, 2])
    print(tree_ancestor.getKthAncestor(3, 5))  # -1
    print(tree_ancestor.getKthAncestor(3, 2))  # 0
    print(tree_ancestor.getKthAncestor(2, 2))  # -1
    print(tree_ancestor.getKthAncestor(0, 2))  # -1
    print(tree_ancestor.getKthAncestor(2, 1))  # 0
