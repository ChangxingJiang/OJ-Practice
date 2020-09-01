class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count = {}
        for ch in set(S):
            count[ch] = S.index(ch)

        return "".join(sorted(T, key=lambda k: count[k] if k in count else -1))


if __name__ == "__main__":
    print(Solution().customSortString(S="cba", T="abcd"))  # "cbad"
