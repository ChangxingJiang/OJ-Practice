class Solution:
    def arrangeWords(self, text: str) -> str:
        def helper(n):
            return len(n)

        ans = sorted(text.lower().split(" "), key=helper)
        ans[0] = ans[0].title()

        return " ".join(ans)


if __name__ == "__main__":
    print(Solution().arrangeWords(text="Leetcode is cool"))  # "Is cool leetcode"
    print(Solution().arrangeWords(text="Keep calm and code on"))  # "On and keep calm code"
    print(Solution().arrangeWords(text="To be or not to be"))  # "To be or to be not"
