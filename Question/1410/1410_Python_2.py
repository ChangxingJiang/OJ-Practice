class Solution:
    def entityParser(self, text: str) -> str:
        return text.replace("&quot;", "\"").replace("&apos;", "'").replace("&gt;", ">").replace("&lt;", "<").replace("&frasl;", "/").replace("&amp;", "&")


if __name__ == "__main__":
    print(Solution().entityParser(text="&amp; is an HTML entity but &ambassador; is not."))  # & is an HTML entity but &ambassador; is not.
    print(Solution().entityParser(text="and I quote: &quot;...&quot;"))  # and I quote: "..."
    print(Solution().entityParser(text="Stay home! Practice on Leetcode :)"))  # Stay home! Practice on Leetcode :)
    print(Solution().entityParser(text="x &gt; y &amp;&amp; x &lt; y is always false"))  # x > y && x < y is always false
    print(Solution().entityParser(text="leetcode.com&frasl;problemset&frasl;all"))  # leetcode.com/problemset/all
