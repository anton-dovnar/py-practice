"""
Take Stock Span Problem

The span Si of the stock’s price on a given day i is defined as the maximum
number of consecutive days just before the given day, for which the price of
the stock on the current day is less than or equal to its price on the given
day.

For example, if an array of 7 days prices is given as
{100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days
are {1, 1, 1, 2, 1, 4, 6}

Time complexity: O(n)
Space complexity: O(n)
"""


def calculate_span(price: list) -> list:
    n = len(price)
    stack = []
    stack.append(0)
    span = [0] * n
    span[0] = 1  # Span value of first element is always 1

    for i in range(1, n):
        while stack and price[stack[-1]] <= price[i]:
            stack.pop()
        span[i] = i - stack[-1] if stack else i + 1
        stack.append(i)
    return span


if __name__ == '__main__':
    price = [10, 4, 5, 90, 120, 80]
    print(calculate_span(price))
