"""
Next Greater Element

Time complexity: O(n)
Space complexity: O(1)
"""


def nge(arr: list) -> list:
    stack = []
    stack.append(arr[0])

    for i in range(1, len(arr)):
        curr = arr[i]
        if stack:
            el = stack.pop()
            while el < curr:
                print(f"{el} --> {curr}")
                if not stack:
                    break
                el = stack.pop()

            if el > curr:
                stack.append(el)

        stack.append(curr)

    while stack:
        el = stack.pop()
        print(f"{el} --> {-1}")


if __name__ == '__main__':
    arr = [11, 13, 21, 3]
    nge(arr)
