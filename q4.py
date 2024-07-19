#/**************************************************/
#/* SC03A - Summer 2024
#/* Assignment 1 - Question 4
#/* Student Name: Brandon Senaha
#/* SID: 20569834
#/*************************************************/

def run():
  print("===== Question 4 =====")

  # define needed vars
  tuition = 8000 # [Dollars]
  tuition_increase = 0.03 # [decimal ratio]

  print('Semester Tuition in:')
  for i in range(5):
    tuition = tuition * (1 + tuition_increase)
    print(f'{i + 1} year(s) = ${tuition:.2f}')