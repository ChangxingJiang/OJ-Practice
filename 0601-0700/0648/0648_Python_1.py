from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = {}

        for word in dictionary:
            now = root
            for ch in word:
                if ch not in now:
                    now[ch] = {}
                now = now[ch]
            now["@"] = None

        def replace(w):
            n = root
            for i, c in enumerate(w):
                if "@" in n:
                    return w[:i]
                if c not in n:
                    return w
                else:
                    n = n[c]
            return w

        return " ".join(replace(word) for word in sentence.split(" "))


if __name__ == "__main__":
    # "the cat was rat by the bat"
    print(Solution().replaceWords(dictionary=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery"))

    # "a a b c"
    print(Solution().replaceWords(dictionary=["a", "b", "c"], sentence="aadsfasf absbs bbab cadsfafs"))

    # "a a a a a a a a bbb baba a"
    print(Solution().replaceWords(dictionary=["a", "aa", "aaa", "aaaa"],
                                  sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))

    # "the cat was rat by the bat"
    print(Solution().replaceWords(dictionary=["catt", "cat", "bat", "rat"],
                                  sentence="the cattle was rattled by the battery"))

    # "it is ab that this solution is ac"
    print(Solution().replaceWords(dictionary=["ac", "ab"], sentence="it is abnormal that this solution is accepted"))
