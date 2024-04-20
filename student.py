from functions import in_data, get_progression_outcome

def student_version(): # Function to run student version

    heading = 'Student Version' # Set heading
    print(heading, '\n' + '-' * len(heading) + '\n') # Print heading and underline

    while True: # Loop to get valid inputs from user based on total credits while calling in_data function
            
            pass_credits = in_data('p', 'PASS')
            defer_credits = in_data('d', 'DEFER')
            fail_credits = in_data('f', 'FAIL')

            if pass_credits + defer_credits + fail_credits != 120:
                print('Total incorrect\n')
                continue # If total credits is not 120, print error message and continue the loop
            else:
                break # If total credits is 120, break the loop

    print(get_progression_outcome(pass_credits, fail_credits)) # Print outcome
    
    
'''
Author: Mahima Dharmasena
'''