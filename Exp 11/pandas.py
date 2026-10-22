# Numpy 123D
# Pandas series dataframe
# Transpose 2d
# 1D 3D array print
# Add label in arr fun
# Operation on matrix -+/*
# Expo




# import numpy as np
# # 1D Array
a = np.array([10, 20, 30, 40])
print("1D Array:", a)

# # 2D Array
b = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:")
print(b)

# # 3D Array
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:")
print(c)



#series
import pandas as pd
s = pd.Series([10, 20, 30, 40])
print(s)

import pandas as pd
s = pd.Series([80, 90, 75], index=["Maths", "Science", "English"])
print(s)



# import pandas as pd
data = {
    "Name": ["Tanuja", "Shreya", "Aditi"],
    "Marks": [85, 90, 78],
    "Age": [20, 20, 19]
}

df = pd.DataFrame(data)
print(df)



#transpose of 1d,2d,3d array
import numpy as np
a = np.array([1, 2, 3, 4, 5])
for i in a:
    print(i)


import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Original Array:")
print(a)
print("Transpose:")
print(a.T)


import numpy as np
a = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(a)

print("Transpose:")
print(a.T)


# #labels in array
import pandas as pd
arr = [10, 20, 30, 40]
s = pd.Series(arr, index=["A", "B", "C", "D"])
print(s)



# #operations on matrix
import numpy as np
A = np.array([[10, 20],
              [30, 40]])
B = np.array([[2, 4],
              [5, 8]])
print("Addition:")
print(A + B)
print("Subtraction:")
print(A - B)
print("Multiplication:")
print(A * B)
print("Division:")
print(A / B)



# exponential
import numpy as np  
a = np.array([1, 2, 3, 4])
print(np.exp(a))


#functions in exponential
import numpy as np
a = np.array([1, 2, 3, 4])  
print("Exponential of a:", np.exp(a))
print("Natural logarithm of a:", np.log(a))