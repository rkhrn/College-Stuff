'''
1. Write a python program to find the intersection of elements from two list

2. Write a python program to find the maximum and minimum number in a list of 10 elements and also find the index position of those numbers

3. Write a python program to fetch only Email ID from text file which include following fields -:
i)Name
ii)Mobile Number
iii)Roll Number
iv)Email ID

4. Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
i)percentage less than 50 (Grade C)
ii)percentage equal to 50 and less than 80 (Grade B)
iii)percentage equal to 80 and more than 80 (Grade A)

5. Write a python program to sort array element in the ascending/descending order
'''
#1. Write a python program to find the intersection of elements from two list

a=[2,True,9,'taha',4,'harsh',5,'hari']
b=[3,'harsh',5,7,2,'tawa','hari',True,False]
print(set(a).intersection(b))

#2. Write a python program to find the maximum and minimum number in a list of 10 elements and also find the index position of those numbers

List=[15,5,13,21,5,7,25,69,40,46]
print("The largest number of the list is ",max(List)," and the index position is @ ",List.index(max(List)))
print("The Smallest number of the list is",min(List)," and the index position is @ ",List.index(min(List)))

#3. Write a python program to fetch only Email ID from text file which include following fields -:
import re
file1 = open("C:\\Users\\rkhrn\\OneDrive\\Desktop\\Python Class","r")
for line in file1:
    lst = re.findall('\S+@\S+',file1)
print(lst)

def hai()

# 4. Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
# i)percentage less than 50 (Grade C)
# ii)percentage equal to 50 and less than 80 (Grade B)
# iii)percentage equal to 80 and more than 80 (Grade A)



#5. Write a python program to sort array element in the ascending/descending order
