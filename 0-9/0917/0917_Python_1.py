class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().reverseOnlyLetters("ab-cd"))  # "dc-ba"
    print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
    print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"
