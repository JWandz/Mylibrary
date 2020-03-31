# -*- coding: utf-8 -*-
"""
Function to check if string (or number) is a credit card number 
Created on Tue Mar 31 16:36:29 2020

@author: JWandz
"""
def credit_card_number(number):
    """ Number(String or Integer) --> Bool
    Function checks if provided variable is a credit card number
    """
    
    total = 0
    
    #convert numbers into strings
    if type(number) == int: 
        number = str(number)
        print(f"Provided number {number} was converted to a string")

    #Check if string contains only integers
    if not number.isdecimal():
        print(f"There is non-numeric character in {number}")
        return False
    
    #Check if len == 15 
    if len(number)>15:
        print(f"{number} is too long")
        return False
    if len(number)<15:
        print(f"{number} is too short")
        return False      
    
    #Check luhn's algorithm
    
    for num, k in enumerate(number):
        if num%2 == 1:
         
            mult = int(k) * 2
            if mult > 9:
                total = total + mult % 10 + 1
            else:
                total = total + mult
        else:
            total = total + int(k)
                
    if total%10 == 0:
        return True
    else:
        print(f"Luhn's algorithm is not valid for {number}" )
        return False

#%%Testing

#true
code = "358670790447666"
#false wrong number
code2 = "358670790147666"
#false letter inside
code3 = "358670790a47666"
#false too short
code4 = "358670790166"
#false too long
code5 = "358671110790147666"
#if number
code6 = 358670790447666

print(credit_card_number(code))
print(credit_card_number(code2))
print(credit_card_number(code3))
print(credit_card_number(code4))
print(credit_card_number(code5))
print(credit_card_number(code6))
