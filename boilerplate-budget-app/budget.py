from operator import itemgetter


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append(
            {"amount": amount, "description": description}
        )

    def withdraw(self, amount, description=''):
        if _ := self.check_funds(amount):
            self.ledger.append(
                {"amount": -amount, "description": description}
            )
            return True
        return False

    def get_balance(self):
        amount = itemgetter('amount')
        total = 0
        if self.ledger:
            if len(self.ledger) == 1:
                total = amount(self.ledger[0])
            else:
                total = sum([amount(x) for x in self.ledger])
        return total

    def transfer(self, amount, other):
        if _ := self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if balance >= amount:
            return True
        return False

    def __str__(self):
        """
        Display ledger.
        """

        total = f"{self.get_balance():.2f}"
        amount = itemgetter('amount')
        description = itemgetter('description')

        text = ''
        text += self.name.center(30, '*') + '\n'
        for obj in self.ledger:
            val = f"{amount(obj):.2f}"
            text += f"{description(obj).ljust(23)[:23]}{val.rjust(7)}\n"
        text += f"Total: {total}"
        return text


def create_spend_chart(categories):
    """
    Generating a bar chart depends on spending data
    """

    text = 'Percentage spent by category\n'
    amount = itemgetter('amount')
    total_spent = sum([amount(obj.ledger[0]) - obj.get_balance() for obj in categories])
    categories_names = [obj.name for obj in categories]

    for percent in range(100, -10, -10):
        row = f"{str(percent).rjust(3)}|"
        for category in categories:
            category_spent = amount(category.ledger[0]) - category.get_balance()
            percent_by_category = round(category_spent * 100 / total_spent)
            if percent_by_category >= percent:
                row += ' o '
            else:
                row += ' ' * 3

        text += row + ' ' + '\n'

    horizontal_line_length = 3 * len(categories) + 1
    text += ('-' * horizontal_line_length).rjust(horizontal_line_length + 4) + '\n'
    for i in range(length := len(max(categories_names, key=len))):
        row = " " * 4
        idx = itemgetter(i)
        for name in categories_names:
            try:
                row += f" {idx(name)} "
            except IndexError:
                row += ' ' * 3

        if i == length - 1:
            text += row + ' '
        else:
            text += row + ' ' + '\n'

    return text
