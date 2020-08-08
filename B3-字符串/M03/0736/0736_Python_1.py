class Solution:
    def evaluate(self, expression: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().evaluate("(add 1 2)"))  # 3
    print(Solution().evaluate("(mult 3 (add 2 3))"))  # 15
    print(Solution().evaluate("(let x 2 (mult x 5))"))  # 10
    print(Solution().evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"))  # 14
    print(Solution().evaluate("(let x 3 x 2 x)"))  # 2
    print(Solution().evaluate("(let x 1 y 2 x (add x y) (add x y))"))  # 5
    print(Solution().evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"))  # 6
    print(Solution().evaluate("(let a1 3 b2 (add a1 1) b2) "))  # 4
