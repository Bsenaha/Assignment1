#/**************************************************/
#/* SC03A - Summer 2024
#/* Assignment 1 - Question 3
#/* Student Name: Brandon Senaha
#/* SID: 20569834
#/*************************************************/

def run():
  print("===== Question 3 =====")

  import math

  # define ratio of seconds
  sec_in_min = 60
  min_in_hr = 60
  hr_in_day = 24
  
  minute = sec_in_min      # seconds in a minute
  hour = minute * min_in_hr# seconds in an hr
  day = hour * hr_in_day   # seconds in a day

  sec = int(input("Number of Seconds: ")) # seconds (IN)

  days = math.floor(sec/day)                    # calc num days
  hours = math.floor(sec/hour % hr_in_day)      # calc num hours
  minutes = math.floor(sec/minute % min_in_hr)  # calc num minutes
  seconds = sec % minute                        # calc num seconds

  print("\nThis is equivalent to:")
  if days >= 1:
    print(days, "Days,", hours, "Hours,", minutes, "Minutes,",  seconds, "Seconds\n")
  elif hours >= 1:
    print(hours, "Hours,", minutes, "Minutes,", seconds, "Seconds\n")
  elif minutes >= 1:
    print(minutes, "Minutes,", seconds, "Seconds\n")
  else:
    print(seconds, "Seconds\n")