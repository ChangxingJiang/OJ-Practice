class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        if len(nodes) == 0 or nodes == ["#"]:
            return True
        stack = []
        i = 0
        while i < len(nodes):
            if nodes[i] != "#":
                stack.append(0)
            elif len(stack) > 0:
                stack[-1] += 1
                while stack and stack[-1] == 2:
                    stack.pop()
                    if stack:
                        stack[-1] += 1
            i += 1
            if not stack:
                break
        return len(stack) == 0 and i == len(nodes)


if __name__ == "__main__":
    print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))  # True
    print(Solution().isValidSerialization("1,#"))  # False
    print(Solution().isValidSerialization("9,#,#,1"))  # False
    print(Solution().isValidSerialization("1,#,#,#,#"))  # False
    print(Solution().isValidSerialization("#,#"))  # False
    print(Solution().isValidSerialization("#"))  # True
