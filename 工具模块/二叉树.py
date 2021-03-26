# 计算二叉树的最大深度
def max_depth(node):
    if not node:
        return 0
    return max(max_depth(node.left), max_depth(node.right)) + 1


# 二叉树的中序遍历(生成迭代器)
def inorder_traversal_to_iter(node):
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            yield node.val
            node = node.right
