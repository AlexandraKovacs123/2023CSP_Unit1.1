# Follow the instructions in the lab document to calculate the mortgage information.
# Everytime you have a new value to output to the screen, make sure to use the proper variable from below.
# Starting data and variable setup - DO NOT EDIT
principal = 250000
annualRate = 4.85
numYears = 30
monthlyPayment = 0
totalPayments = 0
totalInterest = 0
# All student work should be between this and the output section.
#DO NOT EDIT ABOVE HERE

monthRate = (annualRate / 100)
numMonths = (numYears * 12)
partOne = (monthRate * ((1 + monthRate) ** numMonths))
partTwo = (((1 + monthRate) ** numMonths) - 1)
monthlyPayments = (partOne / partTwo) * principal

#DO NOT EDIT BELOW HERE
#Output the data after you r calculations here:
print("Principle: " + str(principal))
print("Annual rate: " + str(annualRate))
print("Number of Years: " + str(numYears))
print("Monthly Payments: " + str(monthlyPayments))
print("Total Payments: " + str(totalPayments))
print("Total Interest: " + str(totalInterest))