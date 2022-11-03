#CTI 110
#P1HW2 - Expenses
#JacksonL
#11/3

#input: three expenses, the budget
#processing: total the expenses, compare with budget
#output: did yougo over or u nder

def main():
    
    #our variables - type float, because of the decimal place
    gas = 0.0
    food = 0.0
    hotel = 0.0
    totalExpenses = 0.0 # gas + food + hotel
    budget = 0.0
    destination = ""

    print("This program calculates on displays travel expenses")

    print("Enter your budget: ")
    budget = float(input())

    destination = input("Where are you going? ")

    print("Ok, let's total all your expenses.")
    #print("Gas: $")
    gas = float(input("Gas: $ "))
    #print("Hotel: $")
    hotel = float(input("Hotel: $"))
    #print("Food: $")
    food = float(input("Food: $ "))
    
    #add up everything
    totalExpenses = gas + hotel + food
    #output - Did they go over budget?

    print("Your total for your trip is $ ", totalExpenses)
    print("Your budget was: $", budget)
    
    if totalExpenses > budget:
            print("You went over the budget!")
            print("by: $", totalExpenses - budget)
    else:
            print("You stayed within your budget!")
            print("money left: $", budget - totalExpenses)

            goAgain = input("Run again? y/n")
            if goAgain == "y":
                    main()
            else:
                print("Goodbye.")
        
#start the program
main()
