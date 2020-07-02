class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        idx = len(S) - 1
        ans = ""
        for s in S:
            if s.isalpha():
                while idx >= 0 and not S[idx].isalpha():
                    idx -= 1
                ans += S[idx]
                idx -= 1
            else:
                ans += s
        return ans


if __name__ == "__main__":
    print(Solution().reverseOnlyLetters("ab-cd"))  # "dc-ba"
    print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
    print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"
