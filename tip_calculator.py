# create a function that taks in input
def bill_with_tip():
    print('This is a tip calculator') # introduce the app

    try: # use a try/except block to account for a value error, if the user enters a string instead of a float or integer-this will prevent the code from breaking

        # create a variable and assign float input to it for the bill amount
        bill = float(input('What is the total amount of the bill? $ '))
        # create a variable  and assign integer input to itfor how many people will be splitting the bill
        persons = int(input('How many people are in your group? '))
        # create a variable and assign float input to it for the tip
        tip = float(input('What percentage of tip do you want to leave? 0, 5, 10, 15, 20, 25 ? '))
         # return tip_calculator(persons, bill, tip) # calls a function within a function- so that the data is avaiable for each function throughoout the entire program
        return tip_calculator(persons, bill, tip)
    except ValueError:
        print('ValueError - please enter numbers')
        return bill_with_tip()
   

# create a function to return the tip and tax
def tip_calculator(persons, bill, tip):
    tip_percent = float(bill * (0.01 * tip))
    tax = float(bill * 0.10)
    total_bill = (bill + tip_percent + tax)
    round_bill = round(total_bill, 2)
    final_total = (round_bill)
    print(type(final_total))
    bill_by_person = (round((total_bill)/persons, 2))
    print(f'The total bill including tax and tip is $ {round_bill}.')
    print(f'The amount due per person is $ {bill_by_person}.')
    return more_tip(final_total) # calls a function within a function- so that the data is avaiable for each function throughoout the entire program *recursion*
    
# create a function to ask the user if they would like to leave any additional tip, if they choose yes, it will add that to the final bill, and display it
# if user does not enter 'Y' or 'N' the block will simply run again, to ask the user, and continue until a valid input (Y, N) is entered
def more_tip(final_total):
    extra_tip = input('Would you like to enter another tip? Y or N ').upper()
    if extra_tip == 'Y': 
        extra_choice = float(input('How much more would you like to leave?  '))
        bonus_total = final_total + extra_choice
        # return bonus_total
        print(f'Your total is {bonus_total}')
        return run_again()
    elif extra_tip == 'N': # if user does not want to add any additional tip, the final will display, and the loop will end
        print('Okay fine!')
        print(f'Your total is {final_total}')
        return run_again()
    else:
        print('Please enter Y or N ')
        return more_tip(final_total) # calls a function within a function- so that the data is avaiable for each function throughoout the entire program *recursion*

# create a function that runs the entire prgram again if the user chooses to do so
def run_again():
    finished = True
    while finished is True:
        finished = input('Would you like to start over? Y or N ').upper()
        if finished == 'Y':
            bill_with_tip()
        else:
            finished = False 

bill_with_tip()
