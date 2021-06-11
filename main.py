# FORK ME or copy the code!  Please don't request edit access. This is the original so it needs to stay undedited for all users.

#Define four functions - add, subtract, multiply, divide that add multiply etc two numbers and return the result. Each should have two integer number arguments.

def add(num1,num2):
  return(num1 + num2)

def subtract(num1,num2):
  return(num1 - num2)

def multiply(num1,num2):
  return(num1 * num2)

def divide(num1,num2):
  return(num1 / num2)

# The user is asked to input two numbers.  These numbers will be passed as arguments into one of the functions.
userNum1 = int(input("Enter a number"))
userNum2 = int(input("Enter another number"))

# The user is asked to input 1 to add, 2 to subtract etc.

choice = int(input("Enter 1 to add, 2 to subtract, 3 to multiply or 4 to divide"))

# If they input 1, call the ‘add’ function, input 2 calls the ‘subtract’ function etc

if choice == 1:
  outputNum = add(userNum1, userNum2)
elif choice == 2:
  outputNum = subtract(userNum1, userNum2)
elif choice == 3:
  outputNum = multiply(userNum1, userNum2)
else:
  outputNum = divide(userNum1, userNum2)

# Output the returned result as part of a sentence.
print(outputNum)