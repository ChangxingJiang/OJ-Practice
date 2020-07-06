class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().isPrefixOfWord(sentence="i love eating burger", searchWord="burg"))  # 4
    print(Solution().isPrefixOfWord(sentence="this problem is an easy problem", searchWord="pro"))  # 2
    print(Solution().isPrefixOfWord(sentence="i am tired", searchWord="you"))  # -1
    print(Solution().isPrefixOfWord(sentence="i use triple pillow", searchWord="pill"))  # 4
    print(Solution().isPrefixOfWord(sentence="hello from the other side", searchWord="they"))  # -1
