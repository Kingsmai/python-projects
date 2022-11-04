# Numpy is a Python package for manipulating lists and tables of numerical data.
# We can use it to do a lot of statistical calculations.
# We call the list or table of data a numpy array.

# We often will take the data from our pandas DataFrame and put it in numpy arrays.
# Pandas DataFrames are great because we have the column names and other text data that makes it human readable.
# A DataFrame, while easy for a human to read, is not the ideal format for doing calculations.
# The numpy arrays are generally less human readable, but are in a format that enables the necessary computation.
import pandas as pd

# Converting from a Pandas Series to a Numpy Array
# We often start with our data in a Pandas DataFrame, but then want to convert it to a numpy array.
# The values attribute does this for us.
df = pd.read_csv('Data/titanic.csv')
print(df['Fare'].values)
# The result is a 1-dimensional array.
# The values attribute of a Pandas Series give the data as a numpy array.


# Converting from a Pandas DataFrame to a Numpy Array
# If we have a pandas DataFrame (instead of a Series as in the last part), we can still use the values attribute, but it returns a 2-dimensional numpy array.
print(df[['Pclass', 'Fare', 'Age']].values)
# The values attribute of a Pandas DataFrame give the data as a 2d numpy array.


# Numpy Shape Attribute
# We use the numpy shape attribute to determine the size of our numpy array.
# The size tells us how many rows and columns are in our data.
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr.shape)  # (887, 3)
# Use the shape attribute to find the number of rows and number columns for a Numpy array.
# You can also use the shape attribute on a pandas DataFrame (df.shape).


# Select from a Numpy Array
print(arr[0, 1])
# This will be the 2nd column of the 1st row (remember that we start counting at 0).
# So it'll be the Fare of the 1st passenger, or 7.25.
# In Numpy Array arr[0, 1] In List arr[0][1]

# We can also select a single row, for example, the whole row of the first passenger:
print(arr[0])

# To select a single column (in this case the Age column), we have to use some special syntax:
print(arr[:, 2])
# Using different syntax within brackets, we can select single values, a whole row or a whole column.
# In slicing there is another syntax: ellipsis ...
# Say you have a higher dimensional array of 4*4*4*4 and you want to access the 4th column on all those dimensions, you may use arr[:, :, :, 3]
# using ellipsis, you can shorten it to arr[..., 3]

# To summarise (assume arr to be a numpy array and L to be a normal Python list):
# 1.) arr[x, y] is similar to L[x][y] (starting index is 0).
# 2.) arr[x] is similar to L[x].
# 3.) arr[a:b] is similar to L[a:b] (A 2-D array/list of the rows from index positions a to b, not including the one at b)
# 4.) arr[a:b, y] is similar to L[a:b][y] (A 1-D array/list of the elements/items in the rows at index a to b, not including b, of the column at index y).
# 5.) arr[:, y] is similar to L[:][y] (the whole column at index y)


# Masking
# Often times you want to select all the rows that meet a certain criteria.
# In this example, we'll select all the rows of children (passengers under the age of 18).
# We create what we call a mask first.
# This is an array of boolean values (True/False) of whether the passenger is a child or not.
mask = arr[:, 2] < 18
# A mask is a boolean array (True/False values) that tells us which values from the array we’re interested in.
# The False values mean adult and the True values mean child,
# so the first 7 passengers are adults, then 8th is a child, and the 9th is an adult.
# Now we use our mask to select just the rows we care about:
print(arr[mask])
# Generally, we don't need to define the mask variable and can do the above in just a single line


# Summing and Counting
# Let’s say we want to know how many of our passengers are children. We still have the same array definition and can take our mask or boolean values from the previous part.
arr = df[['Pclass', 'Fare', 'Age']].values
mask = arr[:, 2] < 18
# Recall that True values are interpreted as 1 and False values are interpreted as 0. So we can just sum up the array and that’s equivalent to counting the number of true values.
print(mask.sum())
# Summing an array of boolean values gives the count of the number of True values.