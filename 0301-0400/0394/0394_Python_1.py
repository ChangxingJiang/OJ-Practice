class Solution:
    def decodeString(self, s: str) -> str:
        size = len(s)
        stack = [""]
        idx = 0
        while idx < size:
            ch = s[idx]
            if ch.isdigit():
                number = ch
                while idx + 1 < size and s[idx + 1].isdigit():
                    idx += 1
                    number += s[idx]
                stack.append(int(number))
            elif ch == "[":
                stack.append("")
            elif ch == "]":
                text = stack.pop()
                p = stack.pop()
                stack[-1] += text * p
            else:
                stack[-1] += ch
            idx += 1
        return stack[0]


if __name__ == "__main__":
    print(Solution().decodeString("3[a]2[bc]"))  # "aaabcbc"
    print(Solution().decodeString("3[a2[c]]"))  # "accaccacc"
    print(Solution().decodeString("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
    print(Solution().decodeString("abc3[cd]xyz"))  # "abccdcdcdxyz"
    print(Solution().decodeString("100[leetcode]"))  # "abccdcdcdxyz"
