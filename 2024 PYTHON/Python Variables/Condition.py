# And, Or, Not
print("***************************Comparison Operators**************************************************")

temp=''
temp = input("Input Temperature(example, 30): ")
if int(temp) > 30:
    print("It's a hot day")
elif int(temp )== 30:
    print("It's about to get hot!\nWhat a day!")
elif int(temp )<= 5:
    print("It's a chilly day")
elif int(temp )>=10 and int(temp )<=20:
    print("It's a cold day")
elif int(temp )<= 10:
    print("It's about to get chilly day!\nWhat a day!") 
# elif int(temp )<-1:
#     print("It's Freezing Outside!")          
else:
    print("It's neither hot nor cold")