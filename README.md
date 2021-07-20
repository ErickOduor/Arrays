1. Compose a program that creates a one-dimensional array a containing exactly 1000 integers and then attempt to access a[1000]. what happens when you run the program?  
a. 1000  
b. value of the array at the start  
c. value of the array at the end  
d. indexing error  

Answer: Q1_array_1000.py code in the repository. trying to access the a[1000] gives the error indexing error   
  
2. what is wrong with the following code fragment?  
    a = []
    for i in range(10):
        a[i] = i * i
Answer:
- a has been initialised as a list  
- a[i] = i * i is not how you add items to a list 
- the program should be as below  
a = []  
for i in range(1, 10):  
    a.append(i*i)  

3. what does the following code fragment write?  
    a = stdarray.createID(10, 0)
    for i in range(10):
        a[i] = 9 - i
    for i in range(10):
        a[i] = a[a[i]]
    for v in a
        stdio.writeln(v)

4. what is a[] after executing the following code fragment?
    n = 10
    a = [0, 1]
    for i in range(2, n):
        a += [a[i-1] + a[i-2]]

Answer: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Bonus: Compose a program that takes an integer command-line argument n and n poker hands (five cards each) from a sheffled deck, seperated by blank lines

