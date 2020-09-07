class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?":
                maybe = ["a", "b", "c"]
                if i > 0 and s[i - 1] in maybe:
                    maybe.remove(s[i - 1])
                if i < len(s) - 1 and s[i + 1] in maybe:
                    maybe.remove(s[i + 1])
                s[i] = maybe.pop(0)
        return "".join(s)


if __name__ == "__main__":
    print(Solution().modifyString("?zs"))
    print(Solution().modifyString("ubv?w"))
    print(Solution().modifyString("j?qg??b"))
    print(Solution().modifyString("??yw?ipkj?"))
