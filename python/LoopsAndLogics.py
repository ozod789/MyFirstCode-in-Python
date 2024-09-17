""" nameList = ["Sleepy", "Druppy", "Thomas", "John", "Edward"]
nameCount = len(nameList)
print("There are "+ str(nameCount)+" names in namelist")

nameIndex = 0
while nameIndex < nameCount:
    print(str(nameIndex) + " " + nameList[nameIndex])
    nameIndex += 1 """

guts = {
    "Name":"Guts",
    "Personality":"gruff",
    "Weapon":"Dragon Slayer",
    "Armor":"Berserker Armor"
}

for key in guts.keys():
    print(key + ": " + guts[key] )

numApples = 20

if numApples > 100:
    print("That's a lot of apples!")
elif numApples > 50:
    print("That's a very good amount of apples")
elif numApples > 30:
    print("That's a good amount of apples")
else:
    print("That's a bad amount of apples")
    

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print("Hi "+name+" !")
print("You are age is: "+str(age))