from LeetTool import TreeNode


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        # 处理空树的情况
        if not root:
            return None

        # 递归处理
        head = TreeNode(root.val)
        head.right = TreeNode(None)
        p = head.right
        if root.children:
            for c in root.children:
                p.left = self.encode(c)
                p = p.left
        return head

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        # 处理空树的情况
        if not data:
            return None

        # 递归处理
        root = Node(val=data.val, children=[])
        data = data.right
        while data.left:
            root.children.append(self.decode(data.left))
            data = data.left
        return root


if __name__ == "__main__":
    pass
