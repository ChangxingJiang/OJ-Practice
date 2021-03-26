class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


class Solution:
    def expTree(self, s: str) -> 'Node':
        # 标记化字符串
        # O(N)
        tokens1 = []
        for ch in s:
            if ch in "+-*/()":
                tokens1.append(ch)
            else:
                if tokens1 and tokens1[-1].isnumeric():
                    tokens1[-1] += ch
                else:
                    tokens1.append(ch)

        # 生成算术表达式树
        stack = [[]]
        for t in tokens1:
            if t.isnumeric() or t in {"+", "-", "*", "/"}:
                stack[-1].append(Node(t))
            elif t == "(":
                stack.append([])
            elif t == ")":
                node = self.build(stack.pop())
                stack[-1].append(node)
            # print([[str(e) for e in part] for part in stack])

        return self.build(stack.pop())

    def build(self, nodes):
        # print("From:", [str(e) for e in nodes])

        # 处理乘除号
        stack1 = []
        for node in nodes:
            if node.val.isnumeric() and stack1 and stack1[-1].val in {"*", "/"}:
                mark = stack1.pop()
                sub1 = stack1.pop()
                mark.left = sub1
                mark.right = node
                # print("New-Mark:", mark)
                stack1.append(mark)
            else:
                stack1.append(node)

        # print("Stack1:", [str(e) for e in stack1])

        # 处理加减号
        stack2 = []
        for node in stack1:
            stack2.append(node)
            if len(stack2) >= 3:
                sub2 = stack2.pop()
                mark = stack2.pop()
                sub1 = stack2.pop()
                mark.left = sub1
                mark.right = sub2
                stack2.append(mark)

        # print("Stack2:", [str(e) for e in stack2])

        # print("Result:", stack2[-1])

        return stack2.pop()


if __name__ == "__main__":
    # [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
    print(Solution().expTree("2-3/(5*2)+1"))

    # [-,*,*,3,4,2,5]
    print(Solution().expTree("3*4-2*5"))

    # [+,+,5,+,4,null,null,+,3,null,null,1,2]
    print(Solution().expTree("1+2+3+4+5"))
