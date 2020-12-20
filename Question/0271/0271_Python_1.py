class Codec:
    def encode(self, strs: [str]) -> str:
        lst = [str(len(s)) for s in strs]
        return ",".join(lst) + "." + "".join(strs)

    def decode(self, s: str) -> [str]:
        idx = s.index(".")
        code = s[:idx]
        if not code:
            return []

        lst = [int(ss) for ss in code.split(",")]

        idx += 1

        ans = []
        for length in lst:
            ans.append(s[idx:idx + length])
            idx += length
        return ans


if __name__ == "__main__":
    pass
