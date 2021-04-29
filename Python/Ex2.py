'''
1. Write a Python program to check whether two strings are equal or not.
2. Write a Python program to display reverse string.
3. Write a Python program to find the sum of digits of a given number.
4. Write a Python program to display a multiplication table.
5. Write a Python program to display all prime numbers between 1 to 10.

'''

# 1. Write a Python program to check whether two strings are equal or not.

def stringequality(word1,word2):
   if(word1==word2):
    print("Yay!, Same words! :)")
   else:
        print("1st word '",word1,"' is not same as that of 2nd word '",word2 ,"' :(")
word1=str(input("Enter a word : "))
word2=str(input("Enter another word : "))
stringequality(word1,word2)


# 2. Write a Python program to display reverse string.

def stringreverse(word):
    word= word[::-1]
    print(word)
word=str(input("Enter a word that needs to be reveresed :"))
print("The reverse of ",word,"is :")
stringreverse(word)


# 3.Write a Python program to find the sum of digits of a given number.

def Sumofdigitsofanumber (n):
    sum=0
    while (n!=0):
        sum= sum+(n%10)
        n=n//10
    return print(sum)
n=int(input("Enter a number with more than two digits :"))
Sumofdigitsofanumber(n)


#4. Write a Python program to display a multiplication table.

def  multiplicationtable(num,till):
    for i in range (1,till+1):
        print(num," x " ,i, "= ", num* i)
num=int(input("Multiplication table for the number :"))
till=int(input("Display the table till : "))
multiplicationtable(num,till)


# Write a Python program to display all prime numbers between 1 to 25

def prime(lower,upper):
    for num in range(lower,upper + 1):
     if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
lower = int(input("Start the prime numbers from : "))
upper = int(input("Print till :"))
prime(lower,upper)