from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        count = {}
        ans = []
        for name in names:
            s = name
            while s in count:
                s = "".join([name, "(", str(count[name]), ")"])
                count[name] += 1
            count[s] = 1
            ans.append(s)
        return ans


if __name__ == "__main__":
    # ["pes","fifa","gta","pes(2019)"]
    print(Solution().getFolderNames(names=["pes", "fifa", "gta", "pes(2019)"]))

    # ["pes","fifa","gta","pes(2019)","pes(1)"]
    print(Solution().getFolderNames(names=["pes", "fifa", "gta", "pes(2019)", "pes"]))

    # ["gta","gta(1)","gta(2)","avalon"]
    print(Solution().getFolderNames(names=["gta", "gta(1)", "gta", "avalon"]))

    # ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
    print(Solution().getFolderNames(names=["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]))

    # ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
    print(Solution().getFolderNames(names=["kaido", "kaido(1)", "kaido", "kaido(1)"]))

    # ["m","t","y(4)","t(1)","a","p","h","h(1)","z","z(2)(2)","x(3)","h(4)(3)","l","z(1)","h(2)","s(1)(2)","y(3)(2)","m(3)","i","h(3)","u","j(1)(4)","q","j(1)","c","n(4)","k","s(1)(4)","p(2)","m(1)","r(1)(4)","k(3)","d(3)(1)","e(4)"]
    print(Solution().getFolderNames(
        names=["m", "t", "y(4)", "t", "a", "p", "h", "h", "z", "z(2)(2)", "x(3)", "h(4)(3)", "l", "z(1)", "h", "s(1)(2)", "y(3)(2)", "m(3)", "i", "h",
               "u", "j(1)(4)", "q", "j(1)", "c", "n(4)", "k", "s(1)(4)", "p(2)", "m", "r(1)(4)", "k(3)", "d(3)(1)", "e(4)"]))

    # ["v(1)","r","k","e","h(3)","t","b(1)","s(4)","n(1)(4)","u(2)(4)","c(1)","v(4)(4)","f","m","y","w","p","n","j","i","z","b","h","r(1)","w(1)","j(1)","i(1)","h(4)","f(1)","u(1)","c","k(1)","t(2)(4)","m(1)","o(3)","s","e(1)","m(3)(4)","q","h(1)(3)","f(2)","w(2)","t(1)","w(3)","u(1)(2)","j(2)","k(2)","k(3)","n(1)","a","b(2)","v"]
    print(Solution().getFolderNames(
        names=["v(1)", "r", "k", "e", "h(3)", "t", "b(1)", "s(4)", "n(1)(4)", "u(2)(4)", "c(1)", "v(4)(4)", "f", "m", "y", "w", "p", "n", "j", "i",
               "z", "b", "h", "r", "w", "j", "i", "h(4)", "f", "u(1)", "c", "k", "t(2)(4)", "m", "o(3)", "s", "e", "m(3)(4)", "q", "h(1)(3)", "f",
               "w", "t", "w", "u(1)(2)", "j", "k", "k", "n", "a", "b", "v"]))
