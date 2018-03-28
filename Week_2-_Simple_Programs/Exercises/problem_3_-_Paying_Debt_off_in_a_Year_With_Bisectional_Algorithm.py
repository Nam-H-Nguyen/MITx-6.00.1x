def lowestFixedMonthlyPaymentForAnnualCreditCardDebt(balance, annualInterestRate):
    '''
    Input: 3 parameters - balance, annualInterestRate
    Return: Using a bisectional search algorithm to suggest a fixed payment amount each month to
    pay off the debt balance after one year even with accruing annual interest
    '''

    annual_balance = balance
    monthly_interest_rate = annualInterestRate / 12

    # Assume that you have not paid any of the month's balance so all 12 month's interest has accrued
    upper_limit_monthly_balance = (annual_balance * (1 + monthly_interest_rate)**12) / 12.0
    
    # Assume that you paid off all the balance in the first month so no monthly interest rate accrued
    lower_limit_monthly_balance = annual_balance / 12
    
    # Set first guess as the mean value of the upper/lower limit monthly balance
    fixed_lowest_monthly_payment = (upper_limit_monthly_balance + lower_limit_monthly_balance) / 2

    epsilon = 0.02

    # Loop until break condition is met
    while abs(balance) >= epsilon:

        # Reset the original value for balance to loop through again
        balance = annual_balance

        # Loop through each month for 12 months decreasing balance with new guess/check values for monthly payments
        for i in range(12):
            balance = balance - fixed_lowest_monthly_payment + ((balance - fixed_lowest_monthly_payment) * monthly_interest_rate)

        # if balance is not yet less than epsilon, keep dividing the upper/lower limit by 2 and setting that as the new
        # fixed lowest monthly payment to guess and check

        # Balance is greater than epsilon meaning the balance has not been paid off.
        # Increase the lower limit to the mean value
        if balance > epsilon:
            lower_limit_monthly_balance = fixed_lowest_monthly_payment

        # Balance is less than epsilon meaning the balance has been paid off.
        # Lower the upper limit value to the mean value
        elif balance < -epsilon:
            upper_limit_monthly_balance = fixed_lowest_monthly_payment
        
        # Reset fixed lowest monthly payment to the new values obtained from either the new upper or lower limit monthly balance
        fixed_lowest_monthly_payment = (upper_limit_monthly_balance + lower_limit_monthly_balance) / 2

        # The lowest monthly payment to pay off credit card debt in a year even with annual credit card interest
        statement_printout = "Lowest Payment: " + str(round(fixed_lowest_monthly_payment, 2))

    return statement_printout

print(lowestFixedMonthlyPaymentForAnnualCreditCardDebt(320000, 0.2))
# Test Case 1: \\Expected Output: 29157.09

# print(lowestFixedMonthlyPaymentForAnnualCreditCardDebt(999999, 0.18))
# Test Case 2: \\Expected Output: 90325.03