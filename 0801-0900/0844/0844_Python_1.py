class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        for s in S:
            if s != "#":
                stack1.append(s)
            else:
                if len(stack1) > 0:
                    stack1.pop(-1)
        stack2 = []
        for t in T:
            if t != "#":
                stack2.append(t)
            else:
                if len(stack2) > 0:
                    stack2.pop(-1)
        return stack1 == stack2


if __name__ == "__main__":
    print(Solution().backspaceCompare(S="ab#c", T="ad#c"))  # True
    print(Solution().backspaceCompare(S="ab##", T="c#d#"))  # True
    print(Solution().backspaceCompare(S="a##c", T="#a#c"))  # True
    print(Solution().backspaceCompare(S="a#c", T="b"))  # False
