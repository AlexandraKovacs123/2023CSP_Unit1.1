#   a114_divisible.py

# get two numbers from user
num = float(input("choose a number"))
nums = float(input("choose another number"))

# loop while the numbers are not divisible (the remainder is not 0)
while (num % nums != 0):

    # inform user of result
    print("the numbers did not work")
    # gather user input again
    num = float(input("choose a number"))
    nums = float(input("choose another number"))
# inform user of result
