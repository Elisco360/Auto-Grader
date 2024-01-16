def compute_tax(income: float) -> float:
    """
    Calculate net income based on the provided formula with different tax rates for different income ranges.

    Parameters:
    - income (float): The total income for which the tax is to be calculated.

    Returns:
    - float: The calculated net income.
    """
    # Tax brackets and corresponding rates as a dictionary
    tax_brackets = {
        402: 0,
        110: 0.05,
        130: 0.1,
        3000: 0.175,
        16395: 0.25,
        29963: 0.3,
        50000: 0.35
    }

    tax_payable = 0
    remaining_income = income

    for bracket, rate in tax_brackets.items():
        if remaining_income > bracket:
            taxable_amount = min(remaining_income, bracket)
            tax_payable += rate * taxable_amount
            # Intentional mistake: Incorrectly updating remaining_income outside the loop
            remaining_income -= taxable_amount

    return income - tax_payable

print(compute_tax(100000))
