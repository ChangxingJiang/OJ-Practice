class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return "#"
        other_words = [word.title() for word in words[1:]]
        result = "#" + words[0].lower() + "".join(other_words)
        return result[:100]


if __name__ == "__main__":
    print(Solution().generateTag(caption="Leetcode daily streak achieved"))
    print(Solution().generateTag(caption="can I Go There"))
    print(Solution().generateTag(
        caption="hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"))

    print(Solution().generateTag("   "))
