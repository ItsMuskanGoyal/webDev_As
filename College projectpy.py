print("Welcome to the coding world")



print ("Enter 5 numbers:")

a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())
sum=0

if (a%2==0):
    sum= sum+a

if (b%2==0):
    sum= sum+b

if (c%2==0):
    sum= sum+c

if (d%2==0):
    sum= sum+d

if (e%2==0):
    sum= sum+e

print(sum)

k=0
for k in range (5,10,2):
    print("Hello",k)
    print(k)


# read 10 number and min and max loops 
# compute sum and average of first n odd number 
# read n value and compute and print factorials from 1 to n


print("Enter value of n for sum and average of odd numbers")
n=int(input())
Sum=0
i5=1
while(i5<2*n):
    Sum= Sum+i5
    i5=i5+2
print("Sum of n odd numbers is:",Sum)
Average= Sum/n
print("Average of n odd numbers is:", Average)


print("Enter value of N for factorial")
N=int(input())
i2=1;
factorial=1;
while(i2<n):
    factorial= factorial*i2
    i2=i2+1
    print("value of factorial is:",factorial)




NumList = []
Number = int(input("How many element in list, Please enter num :- "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

smallest = largest = NumList[0]

for j in range(1, Number):
    if(smallest > NumList[j]):
        smallest = NumList[j]
        min_position = j
    # if(largest < NumList[j]):
    #     largest = NumList[j]
    #     max_position = j

print("The Smallest Element in this List is : ", smallest)
print("The Index position of Smallest Element in this List is : ", min_position)

# print("The Largest Element in this List is : ", largest)
# print("The Index position of Largest Element in this List is : ", max_position)






# print("Enter 10 list items ")
# lst = []

# number of elements as input
# n4 = int(input("Enter number of elements : "))
# i3=0;
# # iterating till the range
# for i3 in range(0, n4):
#     ele = int(input())
#     lst.append(ele) # adding the element
# print(lst)

# max=1;
# for i3 in range(0,n4):

#    36 65



# print("Enter value of n")
# n= int(input())
# sum= n*n
# print("Sum of n odd numbers is:", sum)
# print ("Average of n odd numbers", n)




# print("Enter 3 number to find the greatest")
# p= int(input())
# q= int(input())
# r= int(input())

# Greatest_number=0

# if(p>=q):
#     Greatest_number=p
#     if(p>=r):
#         print("Greatest number is p:",Greatest_number)
#     else:
#         Greatest_number=r
#         print("Greatest number is r:", Greatest_number)
# else:
#     Greatest_number=q
#     if(q>=r):
#         print("Greatest number is q:", Greatest_number)
#     else:
#         Greatest_number=r
#         print("Greatest number is r:", Greatest_number)


# print("Enter a,b,c from equation ax*x+bx+c=0")
# a=int(input())
# b=int(input())
# c=int(input())

# d=(b*b-4*a*c)**0.5

# if (d>=0):
#     print("Roots are real")
#     root1= (-b+d)/2*a
#     root2= (-b-d)/2*a
#     print("Roots of the equations are:",root1,root2)
# else:
#     print("Root are imaginaitve")

# print("Hello World I am Muskan Goyal from CBS")
# name= "Muskan"
# age=18
# marks=97.8
# result= True
# age= 24
# print(name)
# print(age)

# name8 =input("What is your name")
# marks8= input("Enter marks: ")
# print(int(marks8)+20)
# print(int(name8)+ "hi")


