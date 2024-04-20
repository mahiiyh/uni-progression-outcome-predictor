# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Author: Mahima Dharmasena
# Date: 25/11/2023

from student import student_version
from academics import academics_version

def main(): # Function to run the program
    while True: # Loop to run the program again
        while True: # Loop to get valid input from user
            try:
                version = int(input('''
 -------------------------
| Student Version   | (1) |
|-------------------+-----|
| Academics Version | (2) |
 ------------------------- 
                                    
Which version would you like to run?
Enter '1' or '2' from the above menu or '3' to quit: ''')) # Show menu and get input from user
                if version not in range(1, 4):
                    print('Invalid input\n') # If input is not in valid range, print error message
                    continue # Ask for input again
                break # If input is in valid range, break the loop and continue the program
            except ValueError:
                print('Integer required\n') # If input is not an integer, print error message
                continue
        
        print() # Print a blank line
        if version == 1:
            student_version() # If user enters 1, run student version
        elif version == 2:
            academics_version() # If user enters 2, run academics version
        elif version == 3:
            break # If user enters 3, break the loop and end the program

        # Ask user if they want to run the program again
        while True: 
            next = (input("\nEnter 'r' to run the program again or 'q' to quit: ").lower())
            if next == 'r' or next == 'q':
                break # If user enters 'r' or 'q', break the loop and continue the program
            else:
                print('Invalid input\n')
                continue # If user enters invalid input, print error message and ask for input again

        if next == 'r':
            print() # Print a blank line
            continue # If user enters 'r', continue the loop and run the program again
        if next == 'q':
            break # If user enters 'q', break the loop and end the program

    print('\nEnd of program.') # Print end of program message

# Execute main function
if __name__ == '__main__':
    main()


'''
Author: Mahima Dharmasena
'''