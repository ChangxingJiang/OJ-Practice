class Solution:
    def reorderSpaces(self, text: str) -> str:
        num = text.count(" ")
        words = [word for word in text.split() if word.isalpha()]

        size = len(words)

        if size == 1:
            return words[0] + " " * num

        a, b = divmod(num, len(words) - 1)

        return (" " * a).join(words) + " " * b


if __name__ == "__main__":
    print(Solution().reorderSpaces("  this   is  a sentence "))
    print(Solution().reorderSpaces(" practice   makes   perfect"))
    print(Solution().reorderSpaces("hello   world"))
    print(Solution().reorderSpaces("  walks  udp package   into  bar a"))
    print(Solution().reorderSpaces("a"))
