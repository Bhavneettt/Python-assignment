def classify_number(num):
    if num < 0:
        print("The number is negative.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")

# Taking user input
user_input = int(input("Enter an integer: "))

# Calling the function to classify the number
classify_number(user_input)
