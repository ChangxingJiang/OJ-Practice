from toolkit import TreeNode
from toolkit import build_TreeNode


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.queue = [root]
        for node in self.queue:
            if node.left:
                self.queue.append(node.left)
            else:
                break
            if node.right:
                self.queue.append(node.right)
            else:
                break

    def insert(self, v: int) -> int:
        self.queue.append(TreeNode(v))
        idx, sub = divmod(len(self.queue), 2)
        if sub == 0:
            self.queue[idx - 1].left = self.queue[-1]
        else:
            self.queue[idx - 1].right = self.queue[-1]
        return self.queue[idx - 1].val

    def get_root(self) -> TreeNode:
        return self.queue[0]


if __name__ == "__main__":
    obj = CBTInserter(build_TreeNode([1]))
    print(obj.insert(2))
