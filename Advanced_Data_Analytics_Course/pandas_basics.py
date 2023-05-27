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


