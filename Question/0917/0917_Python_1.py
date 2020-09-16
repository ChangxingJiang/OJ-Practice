class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        idx1 = 0
        idx2 = len(S) - 1
        while idx1 < idx2:
            if not S[idx1].isalpha():
                idx1 += 1
            elif not S[idx2].isalpha():
                idx2 -= 1
            else:
                S[idx1], S[idx2] = S[idx2], S[idx1]
                idx1 += 1
                idx2 -= 1
        return "".join(S)


if __name__ == "__main__":
    print(Solution().reverseOnlyLetters("ab-cd"))  # "dc-ba"
    print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
    print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"
