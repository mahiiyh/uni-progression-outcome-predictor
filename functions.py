def in_data(credits_in, label): # Function to get valid inputs from user
    try:
        credits_in = int(input(f'Enter total {label} credits: ')) # Get input from user
        
        # Valid range of credits = 0, 20, 40, 60, 80, 100, 120
        if credits_in not in range(0, 121, 20):
            print('Out of range\n') # If input is not in valid range, print error message
            return in_data(credits_in, label) # Recursion to get valid input
        return credits_in # After getting valid input, return to take next input

    except ValueError:
        print('Integer required\n') # If input is not an integer, print error message
        return in_data(credits_in, label) # Recursion to get valid input

def get_progression_outcome(p, f): # Function to get progression outcome
    if p == 120:
        return 'Progress' # If pass credits is 120, return 'Progress'
    elif p == 100:
        return 'Progress (module trailer)' # If pass credits is 100, return 'Progress (module trailer)'
    elif f >= 80:
        return 'Exclude' # If fail credits is 80 or more, return 'Exclude'
    else:
        return 'Module retriever' # If none of the above, return 'Module retriever'
    
def multiple_outcomes_question(): # Function to ask user if they want to enter another set of data
    try:
        ans = (input('''Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''').lower()[0])
        if ans == 'y':
            return False # If user wants to enter another set of data, return False
        elif ans == 'q':
            return True # If user wants to quit and view results, return True
        else:
            print('Invalid input\n') # If user enters invalid input, print error message
            return multiple_outcomes_question() # Recursion to get valid input
    except IndexError:
        print('Invalid input\n') # If user enters no input, print error message
        return multiple_outcomes_question() # Recursion to get valid input
    

'''
Author: Mahima Dharmasena
'''