#Creating bubble sort algorithm ----

def Bubble_sort(mylist):
#len(mylist) counts how many elements are in the list. 
       n = len(mylist) #n=5
#Outer Loop -----
#It controls how many passes bubble sort performs.
       for i in range(n-1): #range(4) So the loop runs 4 times maximum.
# Swapped checks whether any swapping happened during the current pass.  
         swapped = False #Initially set to False.
#Inner Loop -----
         for j in range(n-i-1):#It compares adjacent elements.
#First Pass (i = 0) ,range(5-0-1) = range(4)
#compares Index 0 and 1,Index 1 and 2,Index 2 and 3,Index 3 and 4
#   if mylist[j] > mylist[j+1]:#Compares two adjacent elements.If left element is bigger Swap them.
           if mylist[j] > mylist[j+1]:
             mylist[j], mylist[j+1] = mylist[j+1], mylist[j] #This line swaps the two elements.

             swapped = True #Indicates that a swap happened during this pass.
         if not swapped:
          break #Stop the loop immediately.
 
