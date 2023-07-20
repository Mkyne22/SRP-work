#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:04:43 2023

@author: marykyne
"""

'''

MATH ASSIGNMENT FOR MASS SPEC SRP



(to skip over reading this pseudocode i wrote before i began programming, go to "UNDERSTANDING THE CODE" below)

the issue:
we want to create a dataframe that ensures we dont lose unique values
we want to develop the code so there's no longer a need for intervals (5)

the rules:
there's a min (10,000) a max (12,000) and intervals of 5
the tolerance is +1 or -1 (so 10,001 would be included but not 10,002)

brainstorm:
i could make a for loop to calulate values
i could make a data frame
    for that i could make three empty lists (exact values, tolerance, unique)
    i could have the lists be empty and use the for loop to populate them
    this df could display all numbers
    
thoughts:
i have to take three empty lists, create a dictionary, then convert to df
all the numbers in the tolerance will either be one number higher/shorter than exact
    since all exact numbers will either end in 0 or 5
    i can add a rule that if the number ends in 9,1,3,4 it will be added to tolerance
 that means the unique numbers will end in 2,6,7,8

what about decimals:
    since those are considered unique values i will add them to list3,
    which will become the "unique" list
    doing this before running the official for loop ensures that it will
    populate list1 & list2 with whole numbers
    i will use the math import to complete this
    
check the columns will be organized even if they aren't in "given_nums':
    done, it outputs organized
    
what if a number is given not in range:
    i will test a number less than 10,000 (9) and greater than 12,000 (12,001)
    the 'for i in given_nums:' code will ensure that all numbers will be in range
    before anything else
    
    
    
UNDERSTANDING THE CODE:

there are five steps for this code to accomplish objective:
    1. importing all necessary libraries
        "math" is required for filtering out whole and decimal numbers
        "pandas" is required for us to create a dataframe
    
    2. organizing the given numbers
        this ensures any numbers out of range are removed before starting anything
        this also separates whole numbers and decimal numbers from imported list
            which will help when sorting "unique" values
        
    3. filtering numbers into three organized lists
        this will sort all numbers into three arrays:'exact','tolerance', and'unique'
    
    4. adjusting the length of the three lists
        since all arrays must be of equal length, the code will fill out shorter lists using NaN
        having NaN (not a number) replace empty values will allow the dataframe to be created
    
    5. converting the keys into a dictionary
        in order to convert the python lines into pandas, the lists will be grouped in a dicionary
        a dictionary is a data structure used to store and organize data in key-value pairs
    
    6. create dataframe from dictionary
        now that we have a dictionary, we can convert the code into pandas
        this will create a dataframe (similar to an excel sheet) which shows all the organized numbers in their respective columns


you can follow along these steps using the comments (grey hashtags)

'''


#1. IMPORTING ALL NECESSARY LIBRARIES

import pandas as pd

import math


# 2. ORGANIZING THE GIVEN NUMBERS

given_nums = [10000, 10001, 10002, 10000.5, 10004, 10005, 10000.9, 9, 12000, 12001]

# an empty list to store numbers between 10,000 and 12,000 from for loop directly underneath it
filtered_nums = []

# a for loop to filter out unnecessary numbers
for i in given_nums:
    if 10000 <= i <= 12000:  # Check if the number is between 10,000 and 12,000
        filtered_nums.append(i)

# empty lists to store whole (new_values) and decimal numbers
decimal_numbers = []
new_values=[]

# a for loop to separate whole and decimal numbers
for i in given_nums:
    if i == math.floor(i):  # Check if the number is an integer (whole number)
        new_values.append(i)
    else:  # If the number has a decimal part
        decimal_numbers.append(i)
        

# 3. FILTERING NUMBERS INTO THREE ORGANIZED LISTS

# empty lists that will become the three arrays
# list3 is given the "decimal_numbers" since they will be considered "unique" anyway
list1 = []
list2 = []
list3 = decimal_numbers


for i in filtered_nums:
   # Check if the number ends in 0 or 5
    last_digit = i % 10
    if i % 10 == 0 or i % 10 == 5:
        # if the number ends in 0 or 5, it will be in the "exact" array
        list1.append(i)
        
    if last_digit in (9, 1, 3, 4):
        # if the number ends in 9, 1, 3, or 4,it will be in the "tolerance" array
        list2.append(i)
        
    if last_digit in (2, 6, 7, 8):
        # if the number ends in 2, 6, 7, 8,it will be in the "unique" array (with the decimal numbers)
        list3.append(i)
        
        
# 4. ADJUSTING THE LENGTH OF THE THREE LISTS

# sets the max length by examining the length of each organized array
max_length = max(len(list1), len(list2), len(list3))

# beef up the shorter lists with NaN to make them equal in length
list1 += [float('nan')] * (max_length - len(list1))
list2 += [float('nan')] * (max_length - len(list2))
list3 += [float('nan')] * (max_length - len(list3))


# 5. CONVERTING THE KEYS INTO A DICTIONARY

# the code here combines the arrays into a dictionary where keys are column names and values are lists
data = {
    'exact': list1,
    'tolerance': list2,
    'unique': list3
}



# 6. CREATING DATAFRAME FROM DICTIONARY

# finally, this code creates a DataFrame from the dictionary using pandas
df = pd.DataFrame(data)


# this line will print the organized DataFrame
print('\n DataFrame of Organized Masses:\n')
print(df)



