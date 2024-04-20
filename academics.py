from functions import in_data, get_progression_outcome, multiple_outcomes_question
from histogram import draw_histogram

def academics_version(): # Function to run academics version

    heading = 'Academics Version' # Set heading
    print(heading, '\n' + '-' * len(heading) + '\n') # Print heading and underline

    # Set initial values for each outcome counter
    progress = 0
    trailer = 0
    retriever = 0
    excluded = 0

    credits_record = [] # Create empty list to store all outcomes and credits (for Part 2)
    try: # Try to create a new file to store all outcomes and credits (for Part 3)
        f = open('credits_record.txt', 'x')
    except FileExistsError: # If file already exists, open it (for Part 3)
        f = open('credits_record.txt', 'w')

    key = False # initialising key to False to enter the while loop

    while key == False: # Run the program until key is True
        
        while True: # Loop to get valid inputs from user based on total credits while calling in_data function
            
            pass_credits = in_data('p', 'PASS')
            defer_credits = in_data('d', 'DEFER')
            fail_credits = in_data('f', 'FAIL')

            if pass_credits + defer_credits + fail_credits != 120:
                print('Total incorrect\n')
                continue # If total credits is not 120, print error message and continue the loop
            else:
                break # If total credits is 120, break the loop
        
        # Get progression outcome using get_progression_outcome function
        outcome = get_progression_outcome(pass_credits, fail_credits)

        # Add outcome and credits to credits_record list (for Part 2)
        credits_record.append([outcome, pass_credits, defer_credits, fail_credits])

        # Write outcome and credits to credits_record.txt file (for Part 3)
        f.write(f'{outcome} - {pass_credits}, {defer_credits}, {fail_credits}\n')

        # Increment outcome counter based on outcome
        if outcome == 'Progress':
            progress += 1
        elif outcome == 'Progress (module trailer)':
            trailer += 1
        elif outcome == 'Module retriever':
            retriever += 1
        elif outcome == 'Exclude':
            excluded += 1
            
        print(outcome) # Print outcome
        print() # Print a blank line

        # Ask user if they want to enter another set of data using multiple_outcomes_question function
        key = multiple_outcomes_question() # Get the boolean value for key and decide whether to continue the loop or not
        print() # Print a blank line

    f.close() # Close credits_record.txt file (for Part 3)

    # Print histogram using draw_histogram function
    draw_histogram(progress, trailer, retriever, excluded)

    # Part 2 (Print all outcomes and credits from credits_record list)
    print('Part 2:')
    for record in credits_record: # Loop through each record in credits_record list
        print(f'{record[0]} - {record[1]}, {record[2]}, {record[3]}') # Print outcome and credits

    # Part 3 (Print all outcomes and credits from credits_record.txt file)
    with open('credits_record.txt') as f: # open credits_record.txt file using context manager
        data = f.read() # Read all data from credits_record.txt file

    print('\nPart 3:')
    print(data) # Print all data


'''
Author: Mahima Dharmasena
'''