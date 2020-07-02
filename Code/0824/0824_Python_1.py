class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split(" ")
        ans = []
        for i in range(len(S)):
            s = S[i]
            if s[0] not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
                s = s[1:] + s[0]
            s += "m" + "a" * (i + 2)
            ans.append(s)
        return " ".join(ans)


if __name__ == "__main__":
    print(Solution().toGoatLatin("I speak Goat Latin"))  # Imaa peaksmaaa oatGmaaaa atinLmaaaaa
    print(Solution().toGoatLatin(
        "The quick brown fox jumped over the lazy dog"))  # heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa
