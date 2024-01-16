from functools import reduce

def compute_tax(income: float) -> float:
    """
    Calculate net income based on the provided formula with different tax rates for different income ranges.

    Parameters:
    - income (float): The total income for which the tax is to be calculated.

    Returns:
    - float: The calculated net income.
    """
    # Tax brackets and corresponding rates as tuples
    tax_brackets = [(402, 0), (110, 0.05), (130, 0.1), (3000, 0.175), (16395, 0.25), (29963, 0.3), (50000, 0.35)]

    def calculate_tax(taxable_amount, bracket):
        amount, rate = bracket
        return taxable_amount + min(remaining_income, amount) * rate

    remaining_income = income
    total_tax = reduce(calculate_tax, tax_brackets, 0)

    return income - total_tax

print(compute_tax(100000))
