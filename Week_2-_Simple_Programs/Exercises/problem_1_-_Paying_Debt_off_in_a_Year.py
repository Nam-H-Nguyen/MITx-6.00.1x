def annualCreditCardDebt(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Input: 3 parameters - balance, annualInterestRate, monthlyPaymentRate
    Return: A printout of the annual remaining credit card debt given a consistent monthlyPaymentRate made every month
    '''

    month_counter = 0

    # a while loop for 12 months or 1 year
    while month_counter < 12:

        # new balance every month will be saved here after each iteration
        paid_minimum_monthly_balance = balance * monthlyPaymentRate

        # Resave into balance variable the remaining balance after paying the minimum monthly payment
        balance -= paid_minimum_monthly_balance

        # Remaining monthly balance before interest accrued gets added to monthly accrued interest rate to get the final monthly balance
        balance *= (1 + annualInterestRate/12)

        # Keeps track of each month
        month_counter += 1

        # Credit Debt Payoff info rounded to two decimal places
        statement_printout = "Remaining Balance: " + str(round(balance, 2))

    return statement_printout

# Test Case 1: \\Expected Output: 361.61 as the remaining balance
# print(annualCreditCardDebt(484, 0.2, 0.04))

# Test Case 2: \\Expected Output: 31.38 as the remaining balance
# print(annualCreditCardDebt(42, 0.2, 0.04))