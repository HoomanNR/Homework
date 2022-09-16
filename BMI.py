#Greetings
print("Hello , Welcome to BMI calculator")
name = input("Please enter your name to start : ")

#Getting Information
Weight = input("Enter your weight in KM : ")
Weight = float(Weight)
Height = input("Enter your height in meters : ")
Height = float(Height)

#Giving Information
BMI = Weight / Height ** 2
BMI = round(BMI , 2 )

if BMI < 18.5 :
    print(name ,  "your BMI is " , BMI , " , you're underweight!")

elif BMI < 25 :
    print(name ,  "your BMI is " , BMI , " , you're normal (:")

elif BMI < 30 :
    print(name , "your BMI is " , BMI , " , you're slightly overweight")

elif BMI < 35 : 
    print( name , "your BMI is " , BMI , " , you're overweight!")

else :
    print( name , "your BMI is " , BMI , " , you're very overweight!!!")


print("Be Healthy ...")