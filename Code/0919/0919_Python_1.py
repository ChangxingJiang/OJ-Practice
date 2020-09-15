import collections

from toolkit import TreeNode


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = collections.deque([root])
        while True:
            if self.queue[0].left:
                self.queue.append(self.queue[0].left)
            else:
                break
            if self.queue[0].right:
                self.queue.append(self.queue[0].right)
                self.queue.popleft()
            else:
                break

    def insert(self, v: int) -> int:
        if not self.queue[0].left:
            self.queue[0].left = TreeNode(v)
            self.queue.append(self.queue[0].left)
            return self.queue[0].val
        else:
            self.queue[0].right = TreeNode(v)
            self.queue.append(self.queue[0].right)
            return self.queue.popleft().val

    def get_root(self) -> TreeNode:
        return self.root


if __name__ == "__main__":
    pass