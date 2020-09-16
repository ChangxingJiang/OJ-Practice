import collections

from toolkit import TreeNode
from toolkit import build_TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 处理根节点为空的情况
        if not root:
            return "[]"

        # 处理根节点不为空的情况
        ans = [str(root.val)]
        now_node = [root]
        while now_node:
            next_node = []
            for node in now_node:
                if node.left:
                    next_node.append(node.left)
                    ans.append(str(node.left.val))
                else:
                    ans.append("null")
                if node.right:
                    next_node.append(node.right)
                    ans.append(str(node.right.val))
                else:
                    ans.append("null")
            now_node = next_node

        while ans[-1] == "null":
            ans.pop()

        return "[" + ",".join(ans) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 处理根节点为空的情况
        if data == "[]":
            return None

        # 拆分根节点
        data = data[1:-1].split(",")
        size = len(data)
        root = TreeNode(int(data[0]))
        queue = collections.deque([root])
        i = 1
        while i < size:
            node = queue.popleft()
            if data[i] != "null":
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            if i + 1 < size and data[i + 1] != "null":
                node.right = TreeNode(int(data[i + 1]))
                queue.append(node.right)
            i += 2
        return root


if __name__ == "__main__":
    tree = build_TreeNode([1, 2, 3, None, None, 4, 5])
    codec = Codec()
    print(codec.serialize(tree))
    print(codec.deserialize(codec.serialize(tree)))
