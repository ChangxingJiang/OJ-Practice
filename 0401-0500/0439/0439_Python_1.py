class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        count = 0
        now = ""
        for ch in expression:
            if ch == "?":
                if now == "T":
                    if stack:
                        count += 1
                        stack.append(now)
                else:
                    count += 1
                    stack.append(now)
            elif ch == ":":
                if count <= 0:
                    return now
                count -= 1
                stack.pop()
            else:
                now = ch
        return now


if __name__ == "__main__":
    print(Solution().parseTernary("T?2:3"))  # "2"
    print(Solution().parseTernary("F?1:T?4:5"))  # "4"
    print(Solution().parseTernary("T?T?F:5:3"))  # "F"
    print(Solution().parseTernary("F?T:F?T?1:2:F?3:4"))  # "4"
