class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        lst = []
        for ch in abbr:
            if ch.isnumeric() and lst and lst[-1].isnumeric():
                lst[-1] += ch
            else:
                lst.append(ch)

        i1, size = 0, len(word)
        for ch2 in lst:
            if ch2.isalpha():
                if i1 >= size or word[i1] != ch2:
                    return False
                i1 += 1
            else:
                if ch2[0] == "0":
                    return False
                i1 += int(ch2)

        return i1 == size


if __name__ == "__main__":
    # True
    print(Solution().validWordAbbreviation(word="internationalization", abbr="i12iz4n"))

    # False
    print(Solution().validWordAbbreviation(word="apple", abbr="a2e"))
