class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("(al)", "al").replace("()", "o")


if __name__ == "__main__":
    print(Solution().interpret("G()(al)"))  # Goal
    print(Solution().interpret("G()()()()(al)"))  # Gooooal
    print(Solution().interpret("(al)G(al)()()G"))  # alGalooG
