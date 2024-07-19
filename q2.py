#/**************************************************/
#/* SC03A - Summer 2024
#/* Assignment 1 - Question 2
#/* Student Name: Brandon Senaha
#/* SID: 20569834
#/*************************************************/

def run():
  print("===== Question 2 =====")

  # define user inputs
  while True:
    month = int(input('Enter a Month (numeric): ')) # month (IN)
    if month > 12 or month <= 0:                    # month validity check
      print('\n** Invalid Month ! **\n')
    else: # continue
      break

  while True:
    day = int(input('Enter a Day: '))               # day (IN)
    if day > 31 or day <= 0:                        # day validity check
      print('\n** Invalid Day ! **\n')
    else: # continue
      break
  
  while True:
    year = (input('Enter a Year (two-digit): '))    # year (IN)
    if len(year) != 2:                              # two-digit check
      print('\n** Invalid Year ! **\n')
    else:
      year = int(year)
      break

  # magic check
  if month * day == year:
    print(f'\nThe Date ({month}/{day}/{year}) is Magic!\n')
  else:
    print(f'\nThe Date ({month}/{day}/{year}) is not Magic.\n')