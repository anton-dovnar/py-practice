"""
Check for Balanced Brackets in an expression (well-formedness)
using Stack.

Time compexity: O(n)
Space complexity: O(n+k)
"""


def validate(exp: str) -> str:
    stack = []
    brackets = {
        "]": "[",
        "}": "{",
        ")": "("
    }
    for b in exp:
        if b in brackets:
            closed = stack.pop()
            if brackets[b] == closed:
                continue
            else:
                return "Not Balanced"
        else:
            stack.append(b)

    return "Balanced"


if __name__ == '__main__':
    exp = "[()]{}{[()()]()}"
    print(validate(exp))

    exp = "[(])"
    print(validate(exp))
