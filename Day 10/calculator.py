def calculate(num1, num2, operator):
  if operator == "-":
      return num1 - num2
  elif operator == "+":
      return num1 + num2
  elif operator == "*":
      return num1 * num2
  elif operator == "/":
      return num1 / num2
  else:
      return "Invalid operator"


def calculator():
  operations = ["+", "-", "*", "/"]
  num1 = int(input("Enter the first number: "))
  cont = True

  while cont:
      num2 = int(input("Enter the next number: "))

      # Display available operators
      print("Available operators:")
      for operator in operations:
          print(operator)

      operator = input("Enter the operator: ")
      result = calculate(num1, num2, operator)
      print(f"Result: {result}")

      choice = input("Do you want to continue? (yes/no/restart): ").lower()
      if choice == "no":
          cont = False
          print(f"Final result is {result}")
      elif choice == "restart":
          print("Restarting the calculator...")
          calculator()  # Recursively start over
          return  # Exit the current recursion
      else:
          num1 = result


# Start the calculator
calculator()
