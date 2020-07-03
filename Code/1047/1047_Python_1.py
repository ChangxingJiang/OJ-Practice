class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if len(stack) == 0 or stack[-1] != s:
                stack.append(s)
            else:
                stack.pop(-1)
        return "".join(stack)


if __name__ == "__main__":
    print(Solution().removeDuplicates("abbaca"))  # ca
