class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S

        N = []
        last, start = S[0], 0
        for i, ch in enumerate(S[1:]):
            if ch != last:
                N.append(last + str(i + 1 - start))
                last, start = ch, i + 1
        else:
            N.append(last + str(len(S) - start))

        N = "".join(N)

        if len(S) <= len(N):
            return S
        else:
            return N


if __name__ == "__main__":
    print(Solution().compressString("aabcccccaaa"))  # "a2b1c5a3"
    print(Solution().compressString("abbccd"))  # "abbccd"
    print(Solution().compressString("bb"))  # "bb"
