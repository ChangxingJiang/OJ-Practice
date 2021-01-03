from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1, count2 = Counter(word1), Counter(word2)
        return (len(word1) == len(word2) and
                set(count1.keys()) == set(count2.keys()) and
                set(count1.values()) == set(count2.values()))


if __name__ == "__main__":
    print(Solution().closeStrings(word1="abc", word2="bca"))  # True
    print(Solution().closeStrings(word1="a", word2="aa"))  # False
    print(Solution().closeStrings(word1="cabbba", word2="abbccc"))  # True
    print(Solution().closeStrings(word1="cabbba", word2="aabbss"))  # False
    print(Solution().closeStrings(word1="abbzzca", word2="babzzcz"))  # False
