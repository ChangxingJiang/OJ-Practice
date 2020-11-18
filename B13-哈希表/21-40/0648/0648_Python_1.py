from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        pass


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
