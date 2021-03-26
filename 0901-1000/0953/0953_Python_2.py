from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = [-1] * 26
        for i in range(len(order)):
            dictionary[ord(order[i]) - 97] = i

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for (c1, c2) in zip(word1, word2):
                o1 = dictionary[ord(c1) - 97]
                o2 = dictionary[ord(c2) - 97]
                if o1 < o2:
                    break
                elif o1 > o2:
                    return False
            else:
                if len(word1) > len(word2):
                    return False
        return True


if __name__ == "__main__":
    # True
    print(Solution().isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))

    # False
    print(Solution().isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))

    # False
    print(Solution().isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
