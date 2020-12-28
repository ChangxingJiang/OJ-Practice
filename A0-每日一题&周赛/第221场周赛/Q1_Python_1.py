class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        a, b = s[:len(s) // 2], s[len(s) // 2:]
        return a.count("a") + a.count("e") + a.count("i") + a.count("o") + a.count("u") == \
               b.count("a") + b.count("e") + b.count("i") + b.count("o") + b.count("u")


if __name__ == "__main__":
    print(Solution().halvesAreAlike("book"))  # True
    print(Solution().halvesAreAlike("textbook"))  # False
    print(Solution().halvesAreAlike("MerryChristmas"))  # False
    print(Solution().halvesAreAlike("AbCdEfGh"))  # True
