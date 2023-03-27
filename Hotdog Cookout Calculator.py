#Hotdog Cookout Calculator Reynol Garcia Jr 03-26-2023



#Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers.

#The program should ask the user for the number of people attending the cookout and the number of hot dogs each person will be given.

#Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.

#The program should display the following details:

# The minimum number of packages of hot dogs required
# The minimum number of packages of hot dog buns required
# The number of hot dogs that will be left over
# The number of hot dog buns that will be left over


packages_of_Hotdogs = 10
packages_Buns = 8

#Number of people you need to get hotdogs for
attending = int(input("Enter the amount of people attending: "))

#How many hot dogs each person will get, which also will be the same as buns needed unless someone does not want buns
Hot_Dog_Per_Person = int(input("Hot dogs each person gets: "))

needed_Hot_Dogs = attending * Hot_Dog_Per_Person
required_packages_Of_HotDogs = (needed_Hot_Dogs / packages_of_Hotdogs)
print("The minimum number of hot dogs packages is:",required_packages_Of_HotDogs)


required_packages_HotDog_Buns = (needed_Hot_Dogs / packages_Buns)
print("The minimum number of hot dog buns packages is: ",required_packages_HotDog_Buns)

leftOver_Hotdogs = (needed_Hot_Dogs / required_packages_Of_HotDogs-needed_Hot_Dogs)
if leftOver_Hotdogs <= 0:
    print("There are no hot dogs leftover")
else:
    print("There are ",leftOver_Hotdogs," hot dogs leftover." )

leftOver_Buns = int(input("Enter the number of extra hot dogs buns: "))
extra_Buns = (needed_Hot_Dogs / required_packages_HotDog_Buns - leftOver_Buns)
if leftOver_Buns == 0:
    print("There are no hot dog buns leftover.") 
elif extra_Buns > 0:
    print("There are ",extra_Buns,"  hot dog buns leftover.")    