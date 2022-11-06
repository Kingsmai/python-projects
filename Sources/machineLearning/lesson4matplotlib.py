# We can use the matplotlib library to plot our data. Plotting the data can often help us build intuition about our data.
# We first need to import matplotlib. It’s standard practice to nickname it plt.
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('Data/titanic.csv')
# We use the scatter function to plot our data. The first argument of the scatter function is the x-axis (horizontal direction) and the second argument is the y-axis (vertical direction).
plt.scatter(df['Age'], df['Fare'])
plt.show()
# This plots the Age on the x-axis and the Fare on the y-axis.
# To make it easier to interpret, we can add x and y labels.
plt.scatter(df['Age'], df['Fare'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()
# We can also use our data to color code our scatter plot. This will give each of the 3 classes a different color. We add the c parameter and give it a Pandas series. In this case, our Pandas series has 3 possible values (1st, 2nd, and 3rd class), so we'll see our datapoints each get one of three colors.
plt.scatter(df['Age'], df['Fare'], c=df['Pclass'])
plt.show()
# The purple dots are first class, the green dots are second class, and the yellow dots are third class.
# A scatter plot is used to show all the values from your data on a graph. In order to get a visual representation of our data, we have to limit our data to two features.

# Scatter Plot
# Write the code to create a scatter plot with Pclass on the y-axis and Fare on the x-axis. Color code it according to whether or not they survived. Add the labels “Fare” and “Pclass” on the x and y axes respectively.
plt.scatter(df['Fare'], df['Pclass'], c=df['Survived'])
plt.xlabel('Fare')
plt.ylabel('Pclass')
plt.show()

# Line
# Now that we can put individual datapoints on a plot, let's see how to draw the line. The plot function does just that. The following draws a line to approximately separate the 1st class from the 2nd and 3rd class. From eyeballing, we’ll put the line from (0, 85) to (80, 5). Our syntax below has a list of the x values and a list of the y values.
plt.scatter(df['Age'], df['Fare'], c=df['Pclass'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.plot([0, 80], [85, 5])
plt.show()
# You can see that the yellow (3rd class) and green (2nd class) points are mostly below the line and the purple (1st class) are mostly above. We did this manually, but in the next module we’ll learn how to do this algorithmically.
# In matplotlib, we use the scatter function to create a scatter plot and the plot function for a line.
