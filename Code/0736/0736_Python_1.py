class Solution:
    def evaluate(self, expression: str) -> int:
        value_stack = [[]]  # 表达式数据栈
        param_stack = [{}]  # 表达式参数栈
        for elem in expression.replace("(", "( ").replace(")", " )").split():
            if elem == "(":
                value_stack.append([])
                param_stack.append(param_stack[-1].copy())
            elif elem == ")":
                values = value_stack.pop()
                if values[0] == "add":
                    value = values[1] + values[2]
                elif values[0] == "mult":
                    value = values[1] * values[2]
                else:
                    if isinstance(values[1], int):
                        value = values[1]
                    elif values[1].isdigit() or (values[1][0] == "-" and values[1][1:].isdigit()):
                        value = int(values[1])
                    else:
                        value = param_stack[-1][values[1]]
                value_stack[-1].append(value)
                param_stack.pop()
                if value_stack[-1][0] == "let" and len(value_stack[-1]) % 2 == 1:
                    value = value_stack[-1].pop()
                    param_stack[-1][value_stack[-1].pop()] = value
            else:
                if not value_stack[-1]:
                    value_stack[-1].append(elem)
                elif value_stack[-1][0] == "let":
                    if len(value_stack[-1]) % 2 == 0:
                        if elem.isdigit() or (elem[0] == "-" and elem[1:].isdigit()):
                            param_stack[-1][value_stack[-1].pop()] = int(elem)
                        else:
                            param_stack[-1][value_stack[-1].pop()] = param_stack[-1][elem]
                    else:
                        value_stack[-1].append(elem)
                else:
                    if elem.isdigit() or (elem[0] == "-" and elem[1:].isdigit()):
                        value_stack[-1].append(int(elem))
                    else:
                        value_stack[-1].append(param_stack[-1][elem])
            # print(elem, "->", value_stack, param_stack)
        return value_stack[0][0]


if __name__ == "__main__":
    print(Solution().evaluate("(add 1 2)"))  # 3
    print(Solution().evaluate("(mult 3 (add 2 3))"))  # 15
    print(Solution().evaluate("(let x 2 (mult x 5))"))  # 10
    print(Solution().evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"))  # 14
    print(Solution().evaluate("(let x 3 x 2 x)"))  # 2
    print(Solution().evaluate("(let x 1 y 2 x (add x y) (add x y))"))  # 5
    print(Solution().evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"))  # 6
    print(Solution().evaluate("(let a1 3 b2 (add a1 1) b2) "))  # 4
    print(Solution().evaluate("(let x 7 -12)"))  # -12
    print(Solution().evaluate("(let x -2 y x y)"))  # -2
    print(Solution().evaluate("(let x (add 12 -7) (mult x x))"))  # 25
