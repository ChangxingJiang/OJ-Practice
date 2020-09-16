from toolkit import TreeNode


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # 将字符串格式转换为列表格式
        lst = []
        last = 0
        for i, ch in enumerate(S):
            if ch.isdigit() != S[last].isdigit():
                lst.append(S[last:i])
                last = i
        else:
            lst.append(S[last:])

        def build_tree(sub_lst, level=0):
            if sub_lst:
                sign = "-" * (level + 1)
                root = TreeNode(sub_lst[0])
                if sign in sub_lst[2:]:
                    idx = sub_lst[2:].index(sign) + 2
                    root.left = build_tree(sub_lst[2:idx], level + 1)
                    root.right = build_tree(sub_lst[idx + 1:], level + 1)
                else:
                    root.left = build_tree(sub_lst[2:], level + 1)
                return root

        return build_tree(lst)


if __name__ == "__main__":
    # [1,2,5,3,4,6,7]
    print(Solution().recoverFromPreorder("1-2--3--4-5--6--7"))

    # [1,2,5,3,null,6,null,4,null,7]
    print(Solution().recoverFromPreorder("1-2--3---4-5--6---7"))

    # [1,401,null,349,88,90]
    print(Solution().recoverFromPreorder("1-401--349---90--88"))
