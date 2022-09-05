# For loop
monday_temperatures = [9.1, 8.8, 7.6]

# To loop the item in List
for temperature in monday_temperatures:
    print(round(temperature))

# Also can loop for Strings
for letter in "Hello":
    print(letter)

# loop for Dictionary
student_grades = {'Maria': 83, 'Simon': 75.5, 'Albert': 99}
# print out item in Tuple
for grade in student_grades.items():
    print(grade)
# print out keys
for grade in student_grades.keys():
    print(grade)
# print out values
for grade in student_grades.values():
    print(grade)



# Bonus code: Dictionary loop and String formatting
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

# a Better way
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))



# While loop
username = ''
while username != 'pypy':
    username = input("Enter username: ")

# Break and Continue in while
while True:
    username = input("Enter Username: ")
    if username == 'pypy':
        break
    else:
        continue