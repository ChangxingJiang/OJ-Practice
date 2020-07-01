class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().backspaceCompare(S="ab#c", T="ad#c"))  # True
    print(Solution().backspaceCompare(S="ab##", T="c#d#"))  # True
    print(Solution().backspaceCompare(S="a##c", T="#a#c"))  # True
    print(Solution().backspaceCompare(S="a#c", T="b"))  # False
