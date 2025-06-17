class Solution:
    def is_neighbour(self, ch1, ch2):
        if abs(ord(ch1) - ord(ch2)) == 1:
            return True
        return ch1 == "a" and ch2 == "z" or ch1 == "z" and ch2 == "a"

    def resultingString(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            elif self.is_neighbour(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


if __name__ == "__main__":
    print(Solution().resultingString(s="abc"))
    print(Solution().resultingString(s="adcb"))
    print(Solution().resultingString(s="zadb"))
