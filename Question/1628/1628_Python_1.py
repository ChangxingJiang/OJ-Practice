from abc import ABC
from typing import List


class Node(ABC):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        if not self.left and not self.right:
            return self.val
        else:
            mark = self.val
            left_val = self.left.evaluate()
            right_val = self.right.evaluate()
            if mark == "+":
                return left_val + right_val
            elif mark == "-":
                return left_val - right_val
            elif mark == "*":
                return left_val * right_val
            else:
                return int(left_val / right_val)

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for t in postfix:
            if t.isnumeric():
                stack.append(Node(int(t)))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(t, left, right))
        return stack.pop()


if __name__ == "__main__":
    obj = TreeBuilder()
    expTree = obj.buildTree(["3", "4", "+", "2", "*", "7", "/"])
    ans = expTree.evaluate()
    print(ans)  # 2

    obj = TreeBuilder()
    expTree = obj.buildTree(["4", "5", "7", "2", "+", "-", "*"])
    ans = expTree.evaluate()
    print(ans)  # -16

    obj = TreeBuilder()
    expTree = obj.buildTree(["4", "2", "+", "3", "5", "1", "-", "*", "+"])
    ans = expTree.evaluate()
    print(ans)  # 18

    obj = TreeBuilder()
    expTree = obj.buildTree(["100", "200", "+", "2", "/", "5", "*", "7", "+"])
    ans = expTree.evaluate()
    print(ans)  # 757
