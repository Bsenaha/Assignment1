#/**************************************************/
#/* SC03A - Summer 2024
#/* Assignment 1 - Question 1
#/* Student Name: Brandon Senaha
#/* SID: 20569834
#/*************************************************/

def run():
  print("===== Question 1 =====")

  # define needed vars and ask user inputs
  P = float(input('Input Principal Deposit Amount (Dollars): '))        # principal amount [$] (IN)
  r = float(input('Annual Interest Rate (Percentage): ')) / 100         # annual interest rate [decimal ratio] (IN)
  n = int(input('Number of Times per year Interest is Compounded: '))   # number of times compounded per year (IN)
  t = int(input('Number of Years Account is Left to Earn Interest: '))  # number of years compounded (IN)

  # calc compound interest
  A = format(P * (1 + r/n) ** (n * t), '.2f') # [Dollars]

  print('\n',f'Total Amount after {t} years: ${A}','\n')