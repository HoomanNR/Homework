#Greetings
print("Hi there\nWelcome to age converter with details")
name = input("Please enter your name to start : ")
name = str(name)

#Getting Information
print("Okay" , name , "Please enter the years =>")
shamsiyear = input("This Shamsi Year : ")
shamsiyear = int(shamsiyear)
miladiyear = input("This Miladi Year : ")
miladiyear = int(miladiyear)


#Getting Age
print("")
print("well done , one more step to have all your age details")
age = input("How old Are you ? ")
age = int(age)
ageMonth = input("In which Month were you born ? ")
ageMonth = int(ageMonth)
ageDay = input("In whice day were you born ? ")
ageDay = int(ageDay)

#Giving Information
print("")
print("You were born on : " )
print("Shamsi :" , shamsiyear-age , "/" , ageMonth , "/" , ageDay) 
print("Miladi :" , miladiyear-age)
print("")
print("Details :")
print("Months :" , age*12)
print("Weeks :" , 365/7*age)
print("Days :" , age*365)
print("Hours :" , age*365*24)
print("Minutes :" , age*365*24*60)
print("Seconds :" , age*365*24*60*60)
print("Have nice day!")