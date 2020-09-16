from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""

        words.sort()

        maximum = 0
        ans = ""
        hashmap = set()
        for word in words:
            if len(word) == 1:
                hashmap.add(word)
                if ans == "":
                    ans = word
            elif word[:-1] in hashmap:
                hashmap.add(word)
                if len(word) > maximum:
                    maximum = len(word)
                    ans = word
        return ans


if __name__ == "__main__":
    print(Solution().longestWord(["w", "wo", "wor", "worl", "world"]))  # world
    print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))  # apple
    print(Solution().longestWord(["a", "banana", "computer", "app", "appl", "ap", "apply", "apple"]))  # apple
    print(Solution().longestWord(
        ["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte", "c", "ca", "cat"]))  # latte
    print(Solution().longestWord(
        ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]))  # yodn
