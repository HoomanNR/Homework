#Greetings
print("Hello , Welcome to number detector")

#Getting Information
Number = input("Please enter an integer number : ")
Number = int(Number)

#Giving Information
print("")
if (Number % 2) == 0 :
    print("The number is even")

else : 
    print("The number is odd")

print("And Your number has" , len(str(Number)) , "characters")