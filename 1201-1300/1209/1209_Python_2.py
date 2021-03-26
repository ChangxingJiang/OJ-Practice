class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append([ch, 1])
            elif stack[-1][0] == ch:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([ch, 1])

        ans = ""
        for elem in stack:
            ans += elem[0] * elem[1]
        return ans


if __name__ == "__main__":
    print(Solution().removeDuplicates(s="abcd", k=2))  # "abcd"
    print(Solution().removeDuplicates(s="deeedbbcccbdaa", k=3))  # "aa"
    print(Solution().removeDuplicates(s="pbbcggttciiippooaais", k=2))  # "ps"
