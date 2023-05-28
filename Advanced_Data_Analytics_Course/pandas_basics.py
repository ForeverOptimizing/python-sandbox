import numpy as np
import pandas as pd


# Creating a DataFrame with a dictionary
data = {'col1': [1,2], 'col2': [3,4]}
df = pd.DataFrame(data=data)


# Creates a 2d array. A list of lists
ex1  =  np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ex1)


# Creating a DataFrame of a Numpy array resembling a list of lists
# Each sublist represents a row in the table
# Also included are separate keyword arguments for the columns and index
df2 = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),
                 columns=['a','b','c'], index=['x','y','z'])

print(df2)


# Selecting parts of a DataFrame

titanic = df
titanic.Age
titanic[['Age']]
# Selects a column
titanic.iloc[0]
# Selects a row
titanic.iloc[[0]]
# Returns rows 0-2
titanic.iloc[0:3]

# Returns rows 0-2 showing only columns 3 and 4
titanic.iloc[0:3, [3,4]]

# Selects all rows for an index column
titanic.iloc[:, [3]]

# Single entry from single column
titanic.iloc[0,3]


# loc[] Used to select pandas rows and columns by name
# selecting rows 1-3 from the Name column
titanic.loc[1:3, ['Name']]

# Add a new column to a DataFrame
titanic['Age_plus_100'] = titanic['Age'] + 100
