import re


def arithmetic_arranger(problems: list, answer: bool = False):
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    text = ' '.join(problems)
    first_line = re.findall(r'(\d+)\s[-+]', text)
    second_line = re.findall(r'[-+]\s(\d+)', text)
    signs = re.findall(r'[^\d\s]', text)

    if len(problems) > 5:
        return 'Error: Too many problems.'
    elif re.search(r'[a-zA-Z]', text):
        return "Error: Numbers must only contain digits."
    elif set(signs).difference({'-', '+'}):
        return "Error: Operator must be '+' or '-'."
    elif len(max(re.findall(r'\d+', text), key=len)) > 4:
        return "Error: Numbers cannot be more than four digits."

    for key, (num1, num2, sign) in enumerate(zip(first_line, second_line, signs)):
        col_margin = ' ' * 4
        length = len(max(num1, num2, key=len))
        if key != len(first_line) - 1:
            row1.append(num1.rjust(length + 2) + col_margin)
            row2.append(sign + num2.rjust(length + 1) + col_margin)
            row3.append('-' * (length + 2) + col_margin)
            if answer:
                x = str(eval(f'{num1} {sign} {num2}'))
                row4.append(x.rjust(length + 2) + col_margin)
        else:
            row1.append(num1.rjust(length + 2))
            row2.append(sign + num2.rjust(length + 1))
            row3.append('-' * (length + 2))
            if answer:
                x = str(eval(f'{num1} {sign} {num2}'))
                row4.append(x.rjust(length + 2))

    row1.append('\n')
    row2.append('\n')
    if answer:
        row3.append('\n')
    return ''.join(row1 + row2 + row3 + row4)