# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:29:54 2022

@author: Aldo
"""

# This will be the employee data file for Lab3

def CompanyDatabase(LeafVillage,Shinobi):
    # Creating our database of Ninjas
    employee = {'Sasuke':{'Salary': '$150,000', 'Title': 'Rogue Ninja',
                'Address': '2743 PlanetMars BLVD', 'Phone': '485-565-5455'},
                'Sakura':{'Salary': '$345,000', 'Title': 'Shinobi Medic',
                'Address': '5865 Moon BLVD', 'Phone': '542-344-5456'},
                'Naruto':{'Salary': '$500,000', 'Title': 'Hokage', 'Address': 
                '8675 Leaf Village', 'Phone': '233-232-2332'}}
    # Loop to see if key name is present in database and if so you
    # print the key along with the value of the key but mine are changed to 
    # an anime series. 
    if LeafVillage in employee:
        print(employee[LeafVillage][Shinobi])
    
    # If the key is not on database then you get the statement printed below. 
    else:
        print('The Leaf Shinobi name you entered does not exist in the database, you might ' 
              'want to try a different Leaf village member name to see a result printed. ')
        

# End of code