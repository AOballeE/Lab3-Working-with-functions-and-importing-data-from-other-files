# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:44:08 2022

@author: Aldo
"""

import employeedata

def main():
    # Loop while continue to run as long as the condition is true 
    # else if condition is false loop will end. 
    while True:
        
        # using try and except to Test this block of code for errors
        try: 
            # Here we have the two inputs to check if they exist in the database
            print('You have entered the employee database')
            print('\n')
            shinobiName = input("Enter the name of the of the employee: ")
            leafInfo = input(f"Enter the info you want to see for {shinobiName}: ")
            
            # This line of code grabs the information from the employee data
            # base and prepares for our print statement if the name exists
            # as previously used in challenege in 10.
            path = employeedata.CompanyDatabase(shinobiName, leafInfo)
            
            # Printing the inforamtion we have enetred above alone with 
            # the empooyees information. 
            print(f"{shinobiName}'s {leafInfo}: {path}")
            
            print('\n')
            # loop to see if user wants to continue to search for information.
            again = input('Would you like to try and enter another name?: ')
            
            # if users enter any of these values then loop will close. 
            if again == 'no':
                print('You have chosen to not continue.')
                break
            
            # if user wants to continue then enter one of these values and loop 
            # will continue
            else:
                # If anything else is entered then loop will repeat. 
                continue
                
        # If the key enetered is not valid then the below print statement is shown. 
        except KeyError:
            print("That key does not exist in the leafvillage database.")
if __name__=="__main__":
    main()
                
# End of code
