class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack = []
        for s in S:
            if s != "#":
                stack.append(s)
            else:
                if len(stack) > 0:
                    stack.pop(-1)
        S = "".join(stack)
        stack = []
        for t in T:
            if t != "#":
                stack.append(t)
            else:
                if len(stack) > 0:
                    stack.pop(-1)
        T = "".join(stack)
        return S == T


if __name__ == "__main__":
    print(Solution().backspaceCompare(S="ab#c", T="ad#c"))  # True
    print(Solution().backspaceCompare(S="ab##", T="c#d#"))  # True
    print(Solution().backspaceCompare(S="a##c", T="#a#c"))  # True
    print(Solution().backspaceCompare(S="a#c", T="b"))  # False
