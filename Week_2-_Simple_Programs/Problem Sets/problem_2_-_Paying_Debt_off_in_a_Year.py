def lowestFixedMonthlyPaymentForAnnualCreditCardDebt(balance, annualInterestRate):
    '''
    Input: 3 parameters - balance, annualInterestRate
    Return: A printout of a suggested fixed payment amount each month to pay off the debt balance after one year
    even with accruing annual interest
    '''

    fixed_lowest_monthly_payment = 0
    monthly_interest_rate = annualInterestRate / 12

    # Loop until break condition is met
    while True:

        # restore original annual balance to test again for the new +10 fixed_lowest_monthly_payment
        annual_balance = balance

        # loop through the 12 months and save the 12th month value to the variable balance
        # Formula for a fixed monthly payment added with accrued monthly interest
        for i in range(12):
            balance = balance - fixed_lowest_monthly_payment + ((balance - fixed_lowest_monthly_payment) * monthly_interest_rate)

        # if balance is not 0 yet, keep doing the guess and check work (+10 to fixed lowest monthly payment)
        # when balance hits 0 or is less than 0, it means that the annual balance along with accrued interest
        # has been paid off. Thus, break out of this statement and print out the newly stored fixed lowest monthly
        # payment variable

        if balance > 0:
            fixed_lowest_monthly_payment += 10
            balance = annual_balance

        else:
            break

        # The lowest monthly payment to pay off credit card debt in a year even with annual credit card interest
        statement_printout = "Lowest Payment: " + str(round(fixed_lowest_monthly_payment, 2))
    
    print(statement_printout)

print(lowestFixedMonthlyPaymentForAnnualCreditCardDebt(3329, 0.2))
# Test Case 1: \\Expected Output: 310

print(lowestFixedMonthlyPaymentForAnnualCreditCardDebt(4773, 0.2))
# Test Case 2: \\Expected Output: 440

print(lowestFixedMonthlyPaymentForAnnualCreditCardDebt(5000, 0.2))
# Test Case 3: \\Expected Output: 460