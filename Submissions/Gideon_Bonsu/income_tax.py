def compute_tax(income: float) -> float:
    """
    Calculate net income based on the provided formula with different tax rates for different income ranges.

    Parameters:
    - income (float): The total income for which the tax is to be calculated.

    Returns:
    - float: The calculated net income.

    Example:
    >>> compute_tax(2000)
    1743.85
    """
    # Tax brackets and corresponding rates
    brackets = [402, 110, 130, 3000, 16395, 29963, 50000]
    rates = [0, 0.05, 0.1, 0.175, 0.25, 0.3, 0.35]

    tax_payable = 0
    taxable_amount = income

    for i in range(len(brackets)):
        if taxable_amount >= brackets[i]:
            # Calculate tax for the current bracket
            tax_payable += rates[i] * min(taxable_amount, brackets[i])
            taxable_amount -= min(taxable_amount, brackets[i])

    net_income = round(income - tax_payable, 2)
    return max(net_income, 0)  # Ensure the net income is not negative


# Example usage
print(compute_tax(2000))
