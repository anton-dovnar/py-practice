"""
Sort a stack using recursion

Time comlexity: O(n^2)
Space complexity: O(n)
"""


def insort(stack: list, el):
    if not stack or stack[-1] > el:
        stack.append(el)
    else:
        temp = stack.pop()
        insort(stack, el)
        stack.append(temp)


def sort_stack(stack: list) -> list:
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        insort(stack, temp)
    return stack


if __name__ == '__main__':
    stack = [-3, 14, 18, -5, 30]
    print(sort_stack(stack))
