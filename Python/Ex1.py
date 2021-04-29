#1. Even or Odd
def Evenorodd(n):
        if n%2 ==0 :
            print ('Even')
        else:
            print ('Odd')
n=int(input("Enter a number to find if it is even or odd : "))
print(Evenorodd(n))

#2. Factorial

def fact(num):
 fac = 1
 for i in range(1, num + 1):
    fac = fac * i
 return print("Factorial of", num ,"is" ,fac)
num = int(input("Enter a number to find it's factorial :"))
fact(num)

#3. Fibonacci series

def fib(n):
    n1=0
    n2=1
    for i in range(1, n):
        print(n1)
        n1=n1+n2
        n2=n1-n2
n=int(input("How many terms to print in fib series ?"))
fib(n)


#4. Sumofdigitsofanumber

def Sumofdigitsofanumber (n):
    sum=0
    while (n!=0):
        sum= sum+(n%10)
        n=n//10  #floor division
    return print(sum)
n=int(input("Enter a number with more than two digits :"))
Sumofdigitsofanumber(n)


#5. Armstrong number
def Armstrongnumber (n):
    sum=0
    temp=n
    while (temp>0):
        n =temp %10
        sum= n**3
        temp=temp//10
    if(sum== n):
        print("It is an armstrong number")
    else:
        print("Nope, it isnt")

n=int(input("Verify the armstrongness of a number lol :"))
Armstrongnumber(n)


#6. Extraction of particular word using the following :
    # a.List, ( list need not be always homogeneous)
    # b.Tuple, (A tuple is a sequence of immutable Python objects. Tuples are just like lists with the exception that tuples cannot be changed once declared.Tuples are usually faster than lists.)
    # c.Dictionary, (Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.)
    # e.Set (Sets are used to store multiple items in a single variable)


def printspecific ():
    #Lists
    friends = ["Tawa", "Harshi", "Bob", "Peopleoftheinternet"]
    print(friends[1])

    #Tuple
    laptops = ("Apple Macbook", "MSI", "Lenovo", "HP", "Asus")
    print(laptops[2])

    #Dictionary
    Specification = {"Category": "Laptop", "RAM": 8,"Screen":
    15.7,"Graphics": 4,  "Company": "Lenovo" ,"Model": "Ideapad Gaming"}
    print(Specification["Model"])

    #Set
    upset = {"sad", 4, "worried ", 13, "random thoughts", 360, True}
    print(upset)

printspecific()




