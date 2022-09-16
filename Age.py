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
if age == 1 :
    print("You're a newborn")

elif age == 2 :
    print("You're a toddler")

elif age < 8 :
    print("You're a youth")

elif age < 12 :
    print("You're a kid")

elif age < 19 :
    print("You're a teenager")

elif age < 40 :
    print("You're an adult")

elif age < 60 :
    print("You're middle aged")

elif age < 80 :
    print("You're aged")

else : 
    print("You're old")

print("Have nice day (:")