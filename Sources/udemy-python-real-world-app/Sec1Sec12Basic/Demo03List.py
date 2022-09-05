# List
# if you want to store multiple data, then you may use list
studentScore = [83, 75.5, 99]
# use the bulitins function to operate this list
mySum = sum(studentScore)
length = len(studentScore)
# get the average of the score
mean = mySum / length
print(mean)

# Important method:
studentScore.append(59.0)
print(studentScore)

# Accessing list
# The secret of Python:
print(studentScore.__getitem__(1))
# It is same as:
print(studentScore[1])

# Accessing List Slices
monday_temperatures = [9.1, 8.8, 7.5, 6.6, 9.9]
print(len(monday_temperatures))
print(monday_temperatures[3])
# List Slices
print(monday_temperatures[1:4])
# Get the first two
print(monday_temperatures[0:2]) # index 2 wont include
print(monday_temperatures[:2]) # you may shortcut the index 0
# Get the last two
print(monday_temperatures[3:5]) # 5 is max index + 1 (len)
print(monday_temperatures[3:]) # here is the shortcut from 3 to last

# Accessing List Item and Slices with Negative Numbers
# Get the last number:
print(monday_temperatures[4]) # may use len() but it will be longer
print(monday_temperatures[-1]) # use the negative number instead
# List Slices with negative number
print(monday_temperatures[-4:-2]) # it want include index -2
# Get the last two:
print(monday_temperatures[-2:])

# String is like List, so
array = ['Hello', 1, 2, 3]
print(array[0]) # Hello
print(array[0][2]) # l



# List comprehension (Note: learn this after for loop)
# sometime you need to simplify the data by removing the '.' in float to save the bytes of data.
# so you need to multiply the data below by 10 to remove the '.', Such as: 22.1 -> 221
temperatures = [221, 234, 340, 230]
# to get the desired output, may use loop to devide each item by 10, so you may:
new_temps = [temp / 10 for temp in temperatures]
print(new_temps) # [22.1, 23.4, 34.0, 23.0]
# it is same as:
new_temps = []
for temp in temperatures:
    new_temps.append(temp / 10)
print(new_temps)

# List comprehension with if condition
# sometime we need to exclude some illegal data
temperatures = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 for temp in temperatures if temp != -9999]
print(new_temps)

# List comprehension with if else condition
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temperatures]
print(new_temps)