class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        size = len(dominoes)

        lefts = {i for i in range(size) if dominoes[i] == "L"}
        rights = {i for i in range(size) if dominoes[i] == "R"}

        while lefts or rights:
            new_lefts = set()
            for left in lefts:
                if left == 0:
                    continue
                if left > 0 and (dominoes[left - 1] == "R" or dominoes[left - 1] == "L"):
                    continue
                if left > 1 and dominoes[left - 2] == "R":
                    continue
                else:
                    dominoes[left - 1] = "L"
                    new_lefts.add(left - 1)
            new_rights = set()
            for right in rights:
                if right == size - 1:
                    continue
                if right < size - 1 and (dominoes[right + 1] == "L" or dominoes[right + 1] == "R"):
                    continue
                if right < size - 2 and dominoes[right + 2] == "L":
                    if right + 2 in new_lefts:
                        dominoes[right + 1] = "R"
                else:
                    dominoes[right + 1] = "R"
                    new_rights.add(right + 1)
            lefts, rights = new_lefts, new_rights

        return "".join(dominoes)


if __name__ == "__main__":
    print(Solution().pushDominoes(".L.R...LR..L.."))  # "LL.RR.LLRRLL.."
    print(Solution().pushDominoes("RR.L"))  # "RR.L"
