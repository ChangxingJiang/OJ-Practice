class Solution:
    def reverseWords(self, s: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))  # "blue is sky the"
    print(Solution().reverseWords("  hello world!  "))  # "world! hello"
    print(Solution().reverseWords("a good   example"))  # "example good a"
