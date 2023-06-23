# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:06:37 2022

@author: Aldo
"""

import employeedata

def main(leafVillage, Shinobi, employee):
    print('You have entered the employee database')
    print('\n')
    # Does the user want to start a search? 
    search = input('Do you want to check the database for an employees information? ')
    
    # If the user enteres any vlaues for yes such as these then loop will continue. 
    if search == 'yes' or 'Yes' or 'y' or 'Y':
        shinobiName = input("Enter the name of the of the employee: ")
        
        if shinobiName in employee:
            leafInfo = input(f"Enter the info you want to see for {shinobiName}: ")
            path = employeedata.CompanyDatabase(shinobiName, leafInfo)
            
            if leafInfo == 'Salary' or 'salary':
                
                print([employeedata][shinobiName]['Salary'])
            elif leafInfo == 'Title' or 'title':
                
                print(f"{shinobiName}'s {leafInfo}: {path}") 
            elif leafInfo == 'Address' or 'address':
                
                print(f"{shinobiName}'s {leafInfo}: {path}") 
            elif leafInfo == 'Phone' or 'phone':
                
                print(f"{shinobiName}'s {leafInfo}: {path}")
            else: 
                print('The description you enetred was not valid to a name, try again.')
        else:
            print('The Leaf Shinobi name you entered does not exist in the database, you might ' 
                  'want to try a different Leaf village member name to see a result printed. ')
            
    elif search == 'No' or 'no' or 'n' or 'n':
         print('You have chosen to not search anything.')
           
if __name__=="__main__":
    main(leafVillage, Shinobi, employee)