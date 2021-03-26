from typing import List


class Master:
    def guess(self, word: str) -> int:
        pass


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        maybe_words = set(wordlist)

        for _ in range(10):
            guess = maybe_words.pop()
            result = master.guess(guess)
            if result == 6:
                return

            for word in list(maybe_words):
                same = sum(1 if word[i] == guess[i] else 0 for i in range(6))
                if same != result:
                    maybe_words.remove(word)


if __name__ == "__main__":
    pass
