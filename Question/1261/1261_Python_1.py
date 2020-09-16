from toolkit import TreeNode
from toolkit import build_TreeNode


class FindElements:

    def __init__(self, root: TreeNode):
        self.lst = set()

        def dfs(node, val):
            if node:
                self.lst.add(val)
                dfs(node.left, val * 2 + 1)
                dfs(node.right, val * 2 + 2)

        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.lst


if __name__ == "__main__":
    obj = FindElements(build_TreeNode([-1, None, -1]))
    print(obj.find(1))  # False
    print(obj.find(2))  # True

    obj = FindElements(build_TreeNode([-1, -1, -1, -1, -1]))
    print(obj.find(1))  # True
    print(obj.find(3))  # True
    print(obj.find(5))  # False

    obj = FindElements(build_TreeNode([-1, None, -1, -1, None, -1]))
    print(obj.find(2))  # True
    print(obj.find(3))  # False
    print(obj.find(4))  # False
    print(obj.find(5))  # True
