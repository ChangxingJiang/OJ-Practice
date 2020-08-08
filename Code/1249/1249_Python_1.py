class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        i = 0
        N = len(s)
        while i < N:
            if s[i] == ")":
                if not stack:
                    s = s[:i] + s[i + 1:]
                    N -= 1
                    i -= 1
                else:
                    stack.pop()
            elif s[i] == "(":
                stack.append(i)
            i += 1
        while stack:
            i = stack.pop()
            s = s[:i] + s[i + 1:]

        return s


if __name__ == "__main__":
    print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))  # "lee(t(c)o)de"
    print(Solution().minRemoveToMakeValid("a)b(c)d"))  # "ab(c)d"
    print(Solution().minRemoveToMakeValid("))(("))  # ""
    print(Solution().minRemoveToMakeValid("(a(b(c)d)"))  # "a(b(c)d)"
