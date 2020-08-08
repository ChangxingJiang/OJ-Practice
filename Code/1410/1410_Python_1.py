class Solution:
    def entityParser(self, text: str) -> str:
        marks = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        i = 0
        N = len(text)
        ans = []
        while i < N:
            try:
                start = text.index("&", i)
                end = text.index(";", start)
                mark = text[start:end + 1]
                if mark in marks:
                    ans.append(text[i:start])
                    ans.append(marks[mark])
                else:
                    ans.append(text[i:end + 1])
                i = end + 1
            except ValueError:
                ans.append(text[i:])
                break
        return "".join(ans)


if __name__ == "__main__":
    print(Solution().entityParser(text="&amp; is an HTML entity but &ambassador; is not."))  # & is an HTML entity but &ambassador; is not.
    print(Solution().entityParser(text="and I quote: &quot;...&quot;"))  # and I quote: "..."
    print(Solution().entityParser(text="Stay home! Practice on Leetcode :)"))  # Stay home! Practice on Leetcode :)
    print(Solution().entityParser(text="x &gt; y &amp;&amp; x &lt; y is always false"))  # x > y && x < y is always false
    print(Solution().entityParser(text="leetcode.com&frasl;problemset&frasl;all"))  # leetcode.com/problemset/all
