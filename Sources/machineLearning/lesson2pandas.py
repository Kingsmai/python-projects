# We will be working with a dataset of Titanic passengers. For each passenger, we’ll have some data on them as well as whether or not they survived the crash.

import pandas as pd

# We add a line in the code below to force python to display all 6 columns. Without the line, it will abbreviate the results.
# pd.options.display.max_columns = 6

# The read_csv function takes a file in csv format and converts it to a Pandas DataFrame.
df =pd.read_csv('Data/titanic.csv')

# The head method returns the first 5 rows of the DataFrame.
print(df.head())

print()

# In pandas, we can use the describe method. It returns a table of statistics about the columns.
# use df.describe(include = "all") It'll add some additional stats like 'top', 'freq' and evaluate all the columns.
# If any column isn't compatible to show a specific stat (like for string columns, mean doesn't make any sense), NaN (Not a Number) will appear.

# Let's review what each of these statistics means:
# Count: This is the number of rows that have a value. In our case, every passenger has a value for each of the columns, so the value is 887 (the total number of passengers).
# Mean: Recall that the mean is the standard average.
# Std: This is short for standard deviation. This is a measure of how dispersed the data is.
# Min: The smallest value
# 25%: The 25th percentile
# 50%: The 50th percentile, also known as the median.
# 75%: The 75th percentile
# Max: The largest value
print(df.describe(include='all'))


# Selecting a Single Column
col = df['Fare']
# The result is what we call a Pandas Series.
# A series is like a DataFrame, but it's just a single column.
print(col)

# Note that: a series don't show its heading/ header... Just values.
# If U want series with the header... Use double square brackets.
col = df[["Fare"]]
print(col)


# Selecting Multiple Columns
small_df = df[['Age', 'Sex', 'Survived']]
print(small_df.head()) 
# When selecting a single column from a Pandas DataFrame, we use single square brackets.
# When selecting multiple columns, we use double square brackets.


# Creating a Column
# We often want our data in a slightly different format than it originally comes in. For example, our data has the sex of the passenger as a string ("male" or "female").
# This is easy for a human to read, but when we do computations on our data later on, we’ll want it as boolean values (Trues and Falses).
# We create a Pandas Series that will be a series of Trues and Falses (True if the passenger is male and False if the passenger is female).
# Now we want to create a column with this result. To create a new column, we use the same bracket syntax (df['male']) and then assign this new value to it.
df['male'] = df['Sex'] == 'male'
df['First Class'] = df['Pclass'] == 1
print(df.head())
# Often our data isn’t in the ideal format.
# Luckily Pandas makes it easy for us to create new columns based on our data so we can format it appropriately.


