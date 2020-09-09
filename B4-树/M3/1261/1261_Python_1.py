from toolkit import TreeNode
from toolkit import build_TreeNode


class FindElements:

    def __init__(self, root: TreeNode):
        pass

    def find(self, target: int) -> bool:
        pass


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
