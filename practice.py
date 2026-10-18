try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("Calculation successful!")

finally:
    print("Program finished.")
