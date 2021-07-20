# Compose a program that creates a one-dimensional array a containing exactly 1000 integers and then attempt to access a[1000].
# what happens when you run the program?  
# a. 1000  
# b. value of the array at the start  
# c. value of the array at the end  
# d. indexing error

import numpy as np
a = np.empty(999)
i = 0
while i <= 999:
    a[i] = int(input("enter a value for the array: "))
    i += 1
print(a[1000])    

# answer: Indexing error