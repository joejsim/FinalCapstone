import math

# Give the user the options then ask them to select which one they want
print("Hello. You can use this programme to work out the amount of interest you will earn on an investment or how much you will pay on a home loan. Follow the instructions below.")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Use a while loop to ensure a valid choice is entered
while True:
    choice = input("Enter either investment or bond from the menu above to proceed: ").strip().lower()
    if choice in ["investment", "bond"]:
        break
    else:
        print("Invalid choice. Please enter either 'investment' or 'bond'.")

# Now ask follow-up questions depending on the user's input
if choice == "investment":
    while True:
        try:
            money = float(input("How much money are you depositing? "))
            interest = float(input("What is the interest rate? "))
            years = int(input("How many years are you investing for? "))
            interest_type = input("Do you want simple or compound interest? ").strip().lower()

            if interest_type in ["simple", "compound"]:
                break
            else:
                print("Invalid choice. Please enter either 'simple' or 'compound'.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    r = interest / 100

    # Now work out the amount the investment is worth depending on if they input compound or simple
    if interest_type == "simple":
        amount = round(money * (1 + r * years), 2)
        print(f"At the end of your investment, you will get back {amount}")
    elif interest_type == "compound":
        amount = round(money * math.pow((1 + r), years), 2)
        print(f"At the end of your investment, you will get back {amount}")

elif choice == "bond":
    while True:
        try:
            value = int(input("What is the present value of the house? "))
            interest = float(input("What is the interest rate? "))
            months = int(input("How many months do you plan on taking to repay the bond? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    i = (interest / 100) / 12
    repayment = round((i * value) / (1 - (1 + i) ** (-months)), 2)
    print(f"You will have to repay {repayment} each month")

