"""
Reverse a stack using recursion

Time complexity: O(n^2)
Space complexity: O(n)
"""


def insert_at_bottom(stack: list, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)


def reverse(stack: list) -> list:
    if stack:
        temp = stack.pop()
        reverse(stack)
        insert_at_bottom(stack, temp)
    return stack


if __name__ == '__main__':
    stack = [1, 2, 3, 4]
    print(reverse(stack))
