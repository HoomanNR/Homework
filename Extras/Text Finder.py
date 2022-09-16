#Greetings
print("Hello , Welcome to digits and letters finder in a text")

#Getting Information
import re
Text = input("Enter your text : ")
Digits = "[0-9]+.?[0-9]*"
Letters = "[A-Z]+[a-z]*"

#Giving Information
print("")
def CountLetterAndDigits(string) :
    lcount = dcount = 0
    for c in string : 
        if c.isdigit() :
            dcount+=1
        elif c.isalpha() :
            lcount+=1
    return lcount , dcount

letters , digits = CountLetterAndDigits(Text)
print("Number of Digits in the text : " , digits)
print("Digits in the text :")
print(re.findall(Digits , Text))
print("Number of Letters in the text : " , letters)
print("Letters in the text :")
print(re.findall(Letters , Text))
print("Have a nice day ...")