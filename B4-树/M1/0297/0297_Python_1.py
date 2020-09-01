from toolkit import TreeNode
from toolkit import build_TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


if __name__ == "__main__":
    tree = build_TreeNode([1, 2, 3, None, None, 4, 5])
    codec = Codec()
    print(codec.deserialize(codec.serialize(tree)))
