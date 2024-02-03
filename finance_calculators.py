import math

# Give the user the options then ask them to select which one they want
print("Hello. You can use this programme to work out the amount of interest you will earn on an investement or how much you will pay on a home loan. Follow the instructions below.")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

choice = input("Enter either investment or bond from the menu above to proceed " )

# remove spaces and make all lower case to allow diffent versions of the same entry
choice = choice.strip().lower()


# Now ask follow up questions depending on the user's input
if choice == "investment":
    money = float(input("How much money are you depositing? "))
    interest = float(input("What is the interest rate? "))
    r = interest/100
    years = int(input("How many years are you investing for? "))
    interest_type = input("Do you want simple or compound interest? ")
    interest_type = interest_type.strip().lower()


# Now work out the amount the investment is worth depending on if they input compound or simple
# Include the possibility of user not entering a valid option
    if interest_type == "simple":
        amount = round(money*(1+r*years),2)
        print(f"At the end of your investment you will get back {amount}")
    elif interest_type == "compound":
        amount = round(money*math.pow((1+r),years),2)
        print(f"At the end of your investment you will get back {amount}")
    else:
        print("I'm sorry, this input is not recognised. Please restart and try again")


# Now work out the monthly payment for bond
elif choice == "bond":
    value = int(input("What is the present value of the house? "))
    interest = float(input("What is the interest rate? "))
    i = (interest/100)/12
    months = int(input("How many months do you plan on taking to repay the bond? "))
    repayment = round((i*value)/(1-(1+i)**(-months)),2)
    print(f"You will have to repay {repayment} each month")


# This is needed in case user doesn't enter a recognised option
else:
    print("I'm sorry, this input is not recognised. Please restart and try again")
