class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s):
            ans = ""
            skip = 0
            for c in reversed(s):
                if c == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    ans += c
            return ans

        S = helper(S)
        T = helper(T)

        return S == T


if __name__ == "__main__":
    print(Solution().backspaceCompare(S="ab#c", T="ad#c"))  # True
    print(Solution().backspaceCompare(S="ab##", T="c#d#"))  # True
    print(Solution().backspaceCompare(S="a##c", T="#a#c"))  # True
    print(Solution().backspaceCompare(S="a#c", T="b"))  # False
