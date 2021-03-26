class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for ch in s:
            if ch == "(":
                stack.append([])
            elif ch == ")":
                inner = stack.pop()
                while inner:
                    stack[-1].append(inner.pop())
            else:
                stack[-1].append(ch)
        return "".join(stack[0])


if __name__ == "__main__":
    print(Solution().reverseParentheses("(abcd)"))  # dcba
    print(Solution().reverseParentheses("(u(love)i)"))  # iloveu
    print(Solution().reverseParentheses("(ed(et(oc))el)"))  # leetcode
    print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q"))  # apmnolkjihgfedcbq
