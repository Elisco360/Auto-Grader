def compute_tax(income: float) -> float:
    """
    Calculate net income based on the provided formula with different tax rates for different income ranges.

    Parameters:
    - income (float): The total income for which the tax is to be calculated.

    Returns:
    - float: The calculated net income.
    """
    # Tax brackets and corresponding rates
    brackets = [402, 110, 130, 3000, 16395, 29963, 50000]
    rates = [0, 0.05, 0.1, 0.175, 0.25, 0.3, 0.35]

    tax_payable = 0
    remaining_income = income

    for bracket, rate in zip(brackets, rates):
        if remaining_income > bracket:
            taxable_amount = min(remaining_income, bracket)
            tax_payable += rate * taxable_amount
            remaining_income -= taxable_amount

    return income - tax_payable

print(compute_tax(100000))
