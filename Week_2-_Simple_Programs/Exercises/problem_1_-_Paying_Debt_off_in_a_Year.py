from math import *

# monthlyInterestRate = annualInterestRate / 12.0
# minimumMonthlyPayment = balance - (annualInterestRate / 12)
# monthlyUnpaidBalance = ""
# updatedMonthlyBalance = round(5.0/4, 2)

# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

def annualCreditDebtPayoff(balance, annualInterestRate, monthlyPaymentRate):
    # print("Month " + str(month_counter) + " Remaining Balance: " + str(updatedMonthlyBalance))
    # Zero Month's balance = initial balance input
    # Payment zero (pO) = balance * minimumMonthlyPayment

    month_counter = 0

    while month_counter < 12:
        month_counter += 1
        print(month_counter)

print(annualCreditDebtPayoff(484, 0.2, 0.04))