"""
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
"""

import csv

# open the file
cfile = open("employee_data.csv", "r")
reps = csv.reader(cfile, delimiter=",")
next(reps)


# create an empty dictionary
current_dict = {}
new_dict = {}

# use a loop to iterate through the csv file
for i in reps:
    # check if the employee fits the search criteria
    if i[9] == "TS":
        current_dict["id"] = str(i[0])
        fullname = str(i[1]) + " " + str(i[2])
        print(fullname)
        current_dict["id"]["name"] = str(fullname)
        current_dict["id"]["salary"] = int(i[5])
        new_dict["id"] = str(i[0])
        new_dict["id"]["name"] = str(fullname)
        bonus = 0.1 * int(i[5])
        new_salary = int(i[5]) + bonus
        new_dict["id"]["salary"] = int(new_salary)

#print(current_dict)
for i in current_dict:
    print(f"Employee Name: {current_dict["id"]["name"]} Current Salary ${current_dict["id"]["salary"]}")
print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per image
for i in current_dict:
    print(f"Employee Name: {new_dict["id"]["name"]} Current Salary ${new_dict["id"]["salary"]}"

print()
print("=========================================")
print()

# print out the total difference between the old salary and the new salary as per image.

cfile.close()
